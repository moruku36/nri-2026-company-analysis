# AI / Frontier Model Sources

最終更新: 2026-09-25

このファイルは `03-ai-ax/` の主要出典を整理する。

## NRI一次情報

| 日付 | 資料 | 主な論点 | URL |
|---|---|---|---|
| 2026-02-24 | Anthropic Japanとのパートナーシップ拡大 | Claude for Enterprise社内導入、Claude Code、Cowork検証、日本企業向け支援 | https://www.nri.com/jp/news/info/20260224_1.html |
| 2026-03-27 | 業界・タスク特化型LLM | GENIAC、金融業務、GPT-5.2比較、AIエージェント | https://www.nri.com/jp/news/newsrelease/20260327_1.html |
| 2026-05-14 | 社会レジリエンスAI | 暗黙知、AIエージェント、自律的な予見・対応 | https://www.nri.com/jp/news/newsrelease/20260514_1.html |
| 2026-08-03 | NRI AFT | FDE、現場常駐、高速ROI検証、AX | https://www.nri.com/jp/news/newsrelease/20260803_1.html |
| 2026-08-06 | NeoSOC + AgenticBlue | AI SOC、複数AI、AI統制基盤 | https://www.nri.com/jp/news/info/20260806_1.html |
| 2026-08-27 | エマージングテクノロジーのセキュリティガバナンス | AI等の先端技術の統制 | https://www.nri.com/jp/news/newsrelease/20260827_1.html |
| 2026-09-16 | 三菱重工との業務プロセス改革 | AIガバナンス策定と共同アプリ開発・実装 | https://www.nri.com/jp/news/info/20260916_1.html |
| 2026-09-17 | フロンティアAI対応脆弱性診断 | Amazon Bedrockを用いた国内データ処理体制 | https://www.nri.com/jp/news/info/20260917_1.html |
| 2026 | エージェント時代のAIガバナンス | 経営・プロセス・技術の3層ガードレール | https://www.nri.com/jp/news/event/2026_ai_governance.html |
| 常設 | NRI AI | NRI全体のAIケイパビリティ、パートナー | https://ai.nri.com/ |

## Anthropic関連

| 資料 | 用途 | URL |
|---|---|---|
| NRI customer story | 日本語文書レビュー50%短縮、内部ベンチマーク、AI生産革新 | https://claude.com/customers/nri |
| Claude Fable 5.1 / Mythos 5.1 | 2026-09-01の最新モデル更新 | https://www.anthropic.com/claude-fable-and-mythos-5-1 |
| Claude Fable | 現行Fable系と更新履歴 | https://www.anthropic.com/claude/fable |
| Claude Mythos | サイバー・バイオ特化モデルと更新履歴 | https://www.anthropic.com/claude/mythos |
| Model deprecations | 現行モデル / 廃止状況 | https://docs.anthropic.com/en/docs/about-claude/model-deprecations |

## OpenAI関連

| 日付 | 資料 | 用途 | URL |
|---|---|---|---|
| 2026-08-06 | GPT-5.6 August Updates | 8月のモデル更新 | https://deploymentsafety.openai.com/gpt-5-6-august-update |
| 2026-08-21更新 | GPT-5.6 | API価格変更、モデル構成 | https://openai.com/index/gpt-5-6/ |
| 2026-09-03 | GPT-6 Astra | サイバー能力を含む新世代モデル | https://openai.com/index/gpt-6-astra/ |
| 2026-09-10 | Agents API | Codexハーネスを用いるクラウドエージェントAPI | https://openai.com/index/introducing-the-agents-api/ |
| 2026-09-22 | GPT-6 Sol / Luna | GPT-6モデルファミリー拡大、GPT-5.6比でAPI価格を引き下げ | https://openai.com/index/introducing-gpt-6-sol-and-luna/ |
| 常設 | Model Release Notes | モデル更新履歴 | https://help.openai.com/en/articles/9624314 |

## 過去のパートナー基盤

| 資料 | 用途 | URL |
|---|---|---|
| NRI × AWS 生成AI戦略協業 | AI共創モデル、Bedrock、エンタープライズAI | https://www.nri.com/jp/news/newsrelease/20251016_2.html |
| NRI × Google Cloud | Vertex AI、Gemini Enterprise、業種別AIエージェント | https://www.nri.com/jp/news/newsrelease/20251029_2.html |

## Research note — 2026-09-25

以下のキーワードでNRI公式サイトおよび一般Web検索を実施したが、9月25日時点で、9月16日の顧客業務改革実装支援と9月17日の診断サービスにおける国内データ処理体制を確認した。一方、特定のフロンティアモデル名に結び付けたNRI全社戦略の変更は確認できない。

- GPT-6 Astra + NRI / 野村総合研究所
- Claude Fable 5.1 + NRI / 野村総合研究所
- Claude Mythos 5.1 + NRI / 野村総合研究所
- GPT-5.6 + NRI / 野村総合研究所

したがって `frontier-model-impact.md` では、

- 「NRIは対応していない」と断定しない
- 「公開情報では直接的な戦略変更を確認できない」と表現する
- NRIの既存のマルチモデル / 業務別評価方針との整合性を分析する

という扱いにする。

## Source policy

- ベンダー自身の性能主張は第三者評価と同一視しない。
- 最新モデルの性能ランキング自体より、NRIの事業構造への影響を重視する。
- 「検索で見つからない」ことを「社内で利用していない」根拠にはしない。
