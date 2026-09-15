# 03. AI / AX Strategy

基準日: 2026-09-15

このディレクトリでは、NRIの2026年AI戦略を「どのモデルを使っているか」ではなく、**AIで顧客企業とNRI自身の仕事・収益モデルをどう変えようとしているか**という観点で整理する。

## まず読む順番

1. [ai-strategy.md](./ai-strategy.md) — NRIのAI/AX戦略の全体像
2. [frontier-model-impact.md](./frontier-model-impact.md) — 2026年8〜9月のOpenAI / Anthropic最新モデル以降の影響
3. [ai-products-services.md](./ai-products-services.md) — AFT、業界特化LLM、AIエージェント等の具体施策
4. [internal-ai-transformation.md](./internal-ai-transformation.md) — NRI自身のAI導入と生産革新
5. [ai-security-governance.md](./ai-security-governance.md) — AIセキュリティ・統制

## 結論を5行で

- 2026年のNRIは、生成AI導入支援から **AX（AI Transformation）支援**へ事業定義を広げている。
- 差別化の中心は基盤モデルそのものではなく、**業界知識、顧客固有の暗黙知、既存システム、実装、セキュリティ、運用**を統合する能力。
- Anthropicとの関係は深いが、戦略全体はClaude一本ではなく **マルチモデル / マルチクラウド**。
- 8〜9月にClaude Fable 5.1 / Mythos 5.1、GPT-6 Astra等が登場した後も、9月15日時点では個別モデル追随より **現場実装・ROI・ガバナンス**に軸足を置く姿勢が続く。
- AIは顧客向け成長領域であると同時に、NRI自身の開発原価・人員構成・利益率を変える **自己変革の手段**でもある。

## 2026年のAI戦略を一枚で見る

```text
Frontier Models / Cloud
  ├─ Anthropic Claude
  ├─ AWS / Amazon Bedrock
  ├─ Google Cloud / Gemini
  ├─ OpenAI 等
  └─ 業界・タスク特化型LLM
          ↓
   NRI Integration Layer
  ├─ 業界・業務知識
  ├─ コンサルティング
  ├─ 顧客固有コンテキスト
  ├─ 既存システム理解
  ├─ AIプラットフォーム
  ├─ セキュリティ / ガバナンス
  └─ FDE / AFT
          ↓
 Customer AX
  ├─ 業務効率化
  ├─ AIエージェント
  ├─ モダナイゼーション
  ├─ AIネイティブシステム
  └─ 事業モデル変革

同時並行:
NRI自身 → Claude等を開発・コンサル・社内業務へ投入 → 生産性 / 利益率改善
```

## 特に追うKPI

- AI関連売上：2028年度 3,000億円以上
- AI関連投資：2026〜2028年度 合計800億円
- AIコンサル案件数 / 成長率
- AI駆動開発の適用率
- 開発・テスト工数削減率
- AI技術者育成人数
- AFT/FDE案件の実績とROI
- AIセキュリティ / ガバナンス案件

詳細出典は [`../sources/ai-frontier-sources.md`](../sources/ai-frontier-sources.md) を参照。
