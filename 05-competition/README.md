# 05. Competition / 競合分析

基準日: 2026-09-25

このディレクトリでは、NRIの競争相手を「SIer」「コンサル」「AIベンダー」という会社分類だけで見るのではなく、**AI時代に企業変革のどのレイヤーを取りに来ているか**で比較する。

## まず読む順番

1. [competitor-map.md](./competitor-map.md) — 主要6社とNRIの横並び比較
2. [accenture.md](./accenture.md) — 最も直接的なFDE / Agentic AI競合
3. [ntt-data.md](./ntt-data.md) — 国内大企業・金融・公共で重なる競合
4. [ibm-deloitte.md](./ibm-deloitte.md) — AI基盤・ガバナンス / 経営変革で重なる競合
5. [fujitsu-hitachi.md](./fujitsu-hitachi.md) — 国内テック大手・Physical AIとの比較
6. [nri-relative-position.md](./nri-relative-position.md) — NRIの勝ち筋・弱点・注視点

## 結論を先に

### 1. 最も直接的な脅威はAccenture

2026年9月8日、AccentureとGoogle CloudはGemini Enterpriseの専任組織を発表し、**1,000人規模のForward Deployed Engineer（FDE）体制**を構築するとした。

NRIが8月に開始したNRI AFTも「FDEが顧客現場に入り、業務知識を取り込みながらAIを本番実装する」という考え方であり、競争軸はかなり近い。

ただし、NRIは日本企業の業務・商習慣・既存システム・長期顧客関係を防御線にできる。

### 2. NTT DATAは「最も似ている競合」

NTT DATAもAI戦略を経営戦略そのものと位置づけ、Smart AI Agent構想、業界別エージェント、MCP連携、グローバルAIサービスを展開している。

NRIとの違いは、NTT DATAの方がグローバルITサービス・インフラ・マネージドサービスのスケールが大きい一方、NRIは国内金融を中心とする高収益な業務知識・共同利用型サービス・コンサル起点の密着力を持つ点。

### 3. IBMは「人月競争」ではなく、AI運用基盤を取りに来ている

IBMはwatsonx Orchestrateを、複数ベンダーのAIエージェントを横断的に運用・監視・統制する **Agentic Control Plane** として展開している。

もしAIエージェントの運用・ガバナンス層がIBM等の標準製品に集約されると、SIer側の独自価値は上流・業務知識・既存システム統合へさらに寄る。

### 4. DeloitteはNRIの「上流」に強く侵入する

DeloitteはAgentic BPR、Google Cloudとの専任プラクティス、Open Model Engineeringを展開。AI導入を単なるIT導入ではなく、業務・組織・統制の再設計として売っている。

NRIのAXコンサルと競合する一方、NRIは実装後の長期運用やミッションクリティカルシステムで差別化しやすい。

### 5. Fujitsu / Hitachiは「自社技術 + Physical AI」が強い

FujitsuはKozuchi、Takane、Multi AI Agent Framework、HitachiはLumada 3.0 / HMAX / Physical AIを軸にする。

特にHitachiはAnthropicと戦略提携し、約29万人へのAI展開、10万人規模のAI人材育成、Frontier AI Deployment Centerを打ち出した。

NRIが比較的強いのは情報系・金融・企業ITであり、工場・設備・モビリティ等のPhysical AIではHitachi/Fujitsuの方が構造的に強い。

---

## 競争の本質

2026年の競争は「どの会社が一番良いLLMを持っているか」ではない。

```text
Frontier Model / Cloud
        ↓
AI Agent Platform / Control Plane
        ↓
Industry Knowledge / Business Process
        ↓
Legacy System / Data / Security
        ↓
FDE / Consulting / Implementation
        ↓
Production Operation / Governance
        ↓
Business Outcome / ROI
```

各社はこのスタックの複数層を取りに来ている。

NRIの勝ち筋は、モデルや汎用AI基盤で正面勝負することではなく、**日本企業の業務・暗黙知・既存システム・セキュリティ・長期運用をまとめて握ること**にある。

詳細出典は [`../sources/competitor-sources.md`](../sources/competitor-sources.md) を参照。
