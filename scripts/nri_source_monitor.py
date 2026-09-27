#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import ssl
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

SCHEMA_VERSION = 1
USER_AGENT = "Mozilla/5.0 (compatible; NRICompanyAnalysisSourceMonitor/1.0)"


class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.href = None
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            href = dict(attrs).get("href")
            if href:
                self.href = href.strip()
                self.text = []

    def handle_data(self, data):
        if self.href is not None:
            self.text.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self.href is not None:
            self.links.append((self.href, " ".join(self.text)))
            self.href = None
            self.text = []


def args():
    p = argparse.ArgumentParser()
    p.add_argument("--config", default=".github/source-monitor.json")
    p.add_argument("--state", default="data/source-monitor-state.json")
    p.add_argument("--report", default="sources/latest-source-monitor.md")
    p.add_argument("--issue-body", default="/tmp/nri-source-monitor-issue.md")
    p.add_argument("--timeout", type=int, default=25)
    return p.parse_args()


def load_json(path, default):
    path = Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def normalize(value):
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def canonical(base, href):
    if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
        return None
    u = urlsplit(urljoin(base, href))
    if u.scheme not in ("http", "https"):
        return None
    query = []
    for k, v in parse_qsl(u.query, keep_blank_values=True):
        kl = k.lower()
        if kl.startswith("utm_") or kl in {"gclid", "fbclid", "mc_cid", "mc_eid"}:
            continue
        query.append((k, v))
    return urlunsplit((u.scheme.lower(), u.netloc.lower(), u.path or "/", urlencode(query), ""))


def fetch(url, timeout, max_bytes):
    req = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "ja,en-US;q=0.8,en;q=0.6",
        },
    )
    with urlopen(req, timeout=timeout, context=ssl.create_default_context()) as resp:
        raw = resp.read(max_bytes + 1)
        if len(raw) > max_bytes:
            raise ValueError("response too large")
        charset = resp.headers.get_content_charset() or "utf-8"
        body = raw.decode(charset, errors="replace")
        return body, {
            "status": int(getattr(resp, "status", 200)),
            "etag": resp.headers.get("ETag", ""),
            "last_modified": resp.headers.get("Last-Modified", ""),
        }


def extract(source, body):
    parser = AnchorParser()
    parser.feed(body)
    allow = [re.compile(x, re.I) for x in source.get("patterns", [])]
    deny = [re.compile(x, re.I) for x in source.get("exclude_patterns", [])]
    found = []
    seen = set()
    for href, raw_title in parser.links:
        url = canonical(source["url"], href)
        if not url or url in seen:
            continue
        title = normalize(raw_title)
        searchable = title + " " + url
        if allow and not any(p.search(searchable) for p in allow):
            continue
        if deny and any(p.search(searchable) for p in deny):
            continue
        found.append({"title": title or url, "url": url})
        seen.add(url)
        if len(found) >= int(source.get("max_items", 40)):
            break
    return found


def fingerprint(body):
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", body, flags=re.I | re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = normalize(re.sub(r"<[^>]+>", " ", text))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def targets(source):
    return ", ".join(source.get("targets", [])) or "-"


def build_report(ts, initialized, rows, candidates, failures):
    lines = [
        "# Latest Source Monitor",
        "",
        "> 自動生成: " + ts.strftime("%Y-%m-%d %H:%M JST"),
        "> 分析本文・結論は自動で書き換えません。新規一次情報を検知したらレビュー候補として記録します。",
        "",
        "## Summary",
        "",
        "- Checked sources: " + str(len(rows)),
        "- Fetch OK: " + str(sum(1 for x in rows if x["status"] == "ok")),
        "- New review candidates: " + str(len(candidates)),
        "- Critical source failures: " + str(len(failures)),
        "- Mode: " + ("incremental diff" if initialized else "baseline refresh"),
        "",
        "## New review candidates",
        "",
    ]
    if not candidates:
        lines.append("今回、新規リンクとして判定された候補はありません。")
    for item in candidates:
        lines += [
            "### " + item["source_name"],
            "",
            "- [" + item["title"] + "](" + item["url"] + ")",
            "- Priority: " + item["priority"],
            "- Suggested targets: " + item["targets"],
            "",
        ]

    lines += [
        "",
        "## Source status",
        "",
        "| Source | Priority | Status | Matched | Suggested targets |",
        "|---|---|---|---:|---|",
    ]
    for row in rows:
        status = row["status"]
        if row.get("message"):
            status += " (" + row["message"].replace("|", "/") + ")"
        lines.append(
            "| [" + row["name"].replace("|", "/") + "](" + row["url"] + ") | "
            + row["priority"] + " | " + status + " | "
            + str(len(row.get("items", []))) + " | "
            + row["targets"].replace("|", "/") + " |"
        )

    lines += ["", "## Current matched items", ""]
    for row in rows:
        lines += ["### " + row["name"], ""]
        if not row.get("items"):
            lines += ["- No matched items.", ""]
            continue
        for item in row["items"][:10]:
            lines.append("- [" + item["title"] + "](" + item["url"] + ")")
        lines.append("")

    lines += [
        "## Review rule",
        "",
        "1. 一次情報を開いて公表日、対象期間、数値定義を確認する。",
        "2. sources 配下のEvidenceを更新する。",
        "3. 影響する分析ファイルだけを更新する。",
        "4. 会社計画、自己評価、第三者評価、分析を分ける。",
        "5. READMEの基準日は分析本文を実際に更新したときだけ変更する。",
        "",
    ]
    return "\n".join(lines) + "\n"


def build_issue(ts, candidates, failures):
    lines = [
        "Monthly source monitor detected items requiring review (" + ts.strftime("%Y-%m-%d %H:%M JST") + ").",
        "",
        "The automation does not rewrite analytical conclusions automatically. Verify each primary source first.",
        "",
    ]
    if candidates:
        lines += ["## New candidates", ""]
        for x in candidates:
            lines += [
                "- " + x["source_name"] + ": [" + x["title"] + "](" + x["url"] + ")",
                "  - priority: " + x["priority"],
                "  - suggested targets: " + x["targets"],
            ]
        lines.append("")
    if failures:
        lines += ["## Critical source failures", ""]
        for x in failures:
            lines.append("- " + x["name"] + ": " + x["message"] + " - " + x["url"])
        lines.append("")
    lines += [
        "## Review checklist",
        "",
        "- [ ] Verify publication date and source authenticity",
        "- [ ] Separate fact, management claim, external reaction and analysis",
        "- [ ] Update the relevant source list",
        "- [ ] Update only affected analysis documents",
        "- [ ] Add evidence links and research-log notes",
        "- [ ] Update README baseline date only if the analysis changed",
        "",
        "Generated dashboard: sources/latest-source-monitor.md",
        "",
    ]
    return "\n".join(lines)


def write_outputs(needs_review, ts, count, failures):
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write("needs_review=" + ("true" if needs_review else "false") + "\n")
        f.write("month=" + ts.strftime("%Y-%m") + "\n")
        f.write("candidate_count=" + str(count) + "\n")
        f.write("critical_failure_count=" + str(failures) + "\n")


def main():
    a = args()
    config = load_json(a.config, {})
    if config.get("schema_version") != SCHEMA_VERSION:
        raise SystemExit("unsupported config schema")

    old = load_json(a.state, {"schema_version": 1, "initialized": False, "sources": {}})
    initialized = bool(old.get("initialized", False))
    old_sources = old.get("sources", {})
    ts = datetime.now(ZoneInfo("Asia/Tokyo"))

    new_state = {
        "schema_version": 1,
        "initialized": True,
        "last_run_jst": ts.isoformat(timespec="seconds"),
        "sources": {},
    }
    rows = []
    candidates = []
    failures = []

    for source in config.get("sources", []):
        sid = source["id"]
        previous = old_sources.get(sid, {})
        previously_seen = set(previous.get("seen_urls", []))
        row = {
            "name": source["name"],
            "url": source["url"],
            "priority": source.get("priority", "normal"),
            "targets": targets(source),
            "status": "ok",
            "message": "",
            "items": [],
        }
        try:
            body, meta = fetch(source["url"], a.timeout, int(source.get("max_bytes", 5000000)))
            items = extract(source, body)
            current_urls = {x["url"] for x in items}
            if not items:
                row["status"] = "warning"
                row["message"] = "0 matched links"
            if initialized:
                for item in items:
                    if item["url"] not in previously_seen:
                        candidates.append(
                            {
                                "source_name": source["name"],
                                "title": item["title"],
                                "url": item["url"],
                                "priority": source.get("priority", "normal"),
                                "targets": targets(source),
                            }
                        )
            seen = sorted(previously_seen | current_urls)[-500:]
            new_state["sources"][sid] = {
                "url": source["url"],
                "last_status": meta["status"],
                "etag": meta["etag"],
                "last_modified": meta["last_modified"],
                "content_sha256": fingerprint(body),
                "seen_urls": seen,
                "current_items": items,
            }
            row["items"] = items
        except (HTTPError, URLError, TimeoutError, ValueError, OSError) as exc:
            row["status"] = "error"
            row["message"] = (type(exc).__name__ + ": " + str(exc))[:200]
            new_state["sources"][sid] = previous or {
                "url": source["url"],
                "seen_urls": [],
                "current_items": [],
                "last_error": row["message"],
            }
            if source.get("priority") == "critical":
                failures.append(row)
        rows.append(row)

    Path(a.report).parent.mkdir(parents=True, exist_ok=True)
    Path(a.report).write_text(build_report(ts, initialized, rows, candidates, failures), encoding="utf-8")
    save_json(a.state, new_state)
    Path(a.issue_body).write_text(build_issue(ts, candidates, failures), encoding="utf-8")

    needs_review = initialized and bool(candidates or failures)
    write_outputs(needs_review, ts, len(candidates), len(failures))
    print(json.dumps({
        "initialized_before": initialized,
        "checked": len(rows),
        "new_candidates": len(candidates),
        "critical_failures": len(failures),
        "needs_review": needs_review,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
