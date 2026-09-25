# Career Implications — NRIの技術者・PMにとって何を意味するか

> 基準日: 2026-09-25  
> **Public-safe:** 特定個人の健康、家族、所属部署、顧客、評価、勤務状況、非公開案件などは扱わない。

## Executive take

2026年のNRIでキャリア価値を高める最も確度の高い方向は、**既存の専門性を捨てて「AI専門家」になることではなく、既存専門性へAIを組み込むこと**である。

特に相性が良いのは、

- Cloud × AI Platform
- Security × AI Governance
- PM × AI Delivery / ROI
- Architecture × Modernization × AI
- Domain × AI

である。

NRIの戦略上も、モデルそのものより、顧客業務・既存システム・セキュリティ・本番運用までつなぐ能力が重視されている。

---

## 1. 「AI専業」より「AIを使える専門家」が強い

2026年のフロンティアモデルは更新速度が速く、個別モデルの使い方だけを専門性にすると陳腐化が早い。

一方、

- 金融業務
- クラウドアーキテクチャ
- セキュリティ
- 大規模システム
- PM
- モダナイゼーション

のような専門性は、モデルが変わっても残る。

### Career principle

```text
Durable skill + AI
    >
AI tool skill only
```

AIは「主専攻」ではなく、既存の強みを増幅するレイヤーとして持つ方がリスクが低い。

---

## 2. Cloud Engineer / Architectにとっての機会

NRIのAXでは、単一LLMを導入するだけでなく、企業システムへ安全に組み込む必要がある。

今後価値が高いテーマは、

- AI workload architecture
- Amazon Bedrock / Google Vertex AI等のマネージドAI基盤
- Model gateway / routing
- Agent runtime
- RAG / enterprise search
- Identity / workload identity
- Private connectivity
- Data governance
- Observability
- FinOps for AI
- Multi-cloud AI

### Strong position

**「クラウド基盤を作れる人」から「企業AIを本番で安全に動かすクラウドアーキテクト」へ拡張する。**

これはNRIのマルチモデル / マルチクラウド方針とも整合する。

---

## 3. Security Engineerにとっての機会

セキュリティはNRIの中計で独立した成長領域。

AIが普及するほど、

- Agentがどの権限を持つか
- どのデータへアクセスできるか
- 外部Toolをどこまで呼べるか
- AI判断をどう監査するか
- Model / MCP / Plugin等をどう信頼するか

という新しい攻撃面が増える。

### 特に価値が高い組み合わせ

1. IAM × Agent Identity
2. Cloud Security × AI Platform
3. AppSec × LLM / Agent
4. SOC × Agentic automation
5. GRC × AI Governance
6. Zero Trust × autonomous workload
7. AI red teaming / evaluation

### Career implication

セキュリティ専門性はAIによって薄まるより、対象範囲が広がる可能性が高い。

**Security × AIは防御的なスキルではなく、AXを実現するための事業スキルになる。**

---

## 4. PMにとっての機会

AI導入案件は従来のシステム案件より不確実性が高い。

モデル能力、品質、コスト、規制、データ、利用者行動が短期間で変わる。

このためPMには、固定計画を管理する能力だけでなく、

- hypothesis driven delivery
- short ROI cycle
- experiment design
- vendor / model selection
- risk acceptance
- human-in-the-loop design
- outcome based contract / pricing理解

が重要になる。

AFTが短いサイクルでROI検証を行うのは、この変化を象徴している。

### Strong position

**「進捗管理が上手いPM」から「不確実なAI案件を事業成果へ着地させるPM」へ。**

---

## 5. Architecture / Modernizationは有望

AIが古いシステムを一瞬で置き換えるわけではない。

NRI経営陣も、日本にはレガシーシステムが多く残り、今後10〜15年は需要が強いとの見方を示している。

AIの本格利用には、

- API化
- data access
- identity
- event driven architecture
- observability
- cloud migration
- data modernization

等が必要になる。

### Career implication

**Modernizationは「古い技術の仕事」ではなく、AI導入の前提条件になり得る。**

レガシー理解とモダンアーキテクチャの両方を持つ人材は価値が高い。

---

## 6. Domain knowledgeを軽視しない

AIモデルは一般知識を急速に吸収する。

その結果、価値が上がるのは、公開Webに存在しない

- 顧客固有業務
- 業界慣行
- 制度対応
- 過去の設計理由
- 例外処理
- 運用上の暗黙知

を理解できる人。

### Career implication

「技術だけに寄せる」より、少なくとも1つの業界 / 業務ドメインを深く持つ方がNRIの差別化戦略と合う。

---

## 7. 価値が下がりやすいキャリアパターン

### Coordination-only PM

技術・業務判断をせず、日程調整・報告・転記だけを行う。

### Tool operator

特定製品のGUI操作や手順だけに依存する。

### Certification collector

資格数は多いが、本番設計・障害・トレードオフを説明できない。

### Prompt-only specialist

プロンプト技法だけを専門にする。

### Document-only role

資料作成自体が価値の中心になっている。

### Interpretation

AI時代に残りやすいのは、**「作業ができる人」ではなく「なぜそうするかを決められる人」**である。

---

## 8. 価値が上がりやすいキャリアパターン

### T-shaped → π-shaped

1つの専門軸だけでなく、2つの深い専門をAIで接続する。

例:

```text
Cloud        Security
  │             │
  └──── AI ─────┘
        │
 Business / Domain
```

または、

```text
PM          Architecture
 │              │
 └──── AI ──────┘
        │
 Outcome / ROI
```

### Why

AIが浅い知識を補完するため、複数領域を接続してトレードオフを判断できる人の価値が上がる。

---

## 9. 12〜24か月で作ると強い実績

公開情報ベースの一般的な技術者向け推奨として、次のような実績はAI時代との整合性が高い。

### 1. AIを使った生産性改善を定量化

例:

- 設計レビュー時間 -30%
- IaC作成時間 -50%
- テスト作成時間 -40%
- 調査リードタイム -60%

重要なのはAIを使った事実より**Before / Afterを測ること**。

### 2. Enterprise AI architectureを1つ説明できるようにする

- model
- data
- IAM
- network
- security
- logging
- cost
- fallback

まで含める。

### 3. AI Agentの安全な実装経験

単純チャットではなく、Tool利用、権限、監査、Human approvalを含める。

### 4. ModernizationとAIをつなげる

既存システムをAPI化 / データ化し、AIから安全に利用する構成を理解する。

### 5. Outcomeを説明する

技術成果だけでなく、

- cost
- quality
- speed
- risk
- revenue

のどれに効いたかを説明する。

---

## 10. 「役職」より先に作るべきキャリア資産

AI時代に持ち運びやすい資産は、社内タイトルより以下。

- Architecture judgment
- Domain knowledge
- Security judgment
- Delivery record
- AI-enabled productivity
- Outcome / ROI record
- Vendor-neutral knowledge
- Technical writing / reusable IP

これらは部署や会社が変わっても残る。

---

## 11. NRIという環境を活かしやすいテーマ

NRIは公開情報上、

- 大規模ミッションクリティカルシステム
- 金融プラットフォーム
- クラウド
- セキュリティ
- コンサルティング
- AIベンダーとの協業
- 自社IP

を同時に持つ。

このため、AIモデル研究そのものより、**AIを大企業の本番環境へ入れる経験**を積む場として強みがある。

キャリア上は、このNRI固有の環境を利用して

> Enterprise AI implementation experience

を獲得できるかが重要になる。

---

## 12. Watch items

今後、以下が確認できれば人材戦略の実効性を判断しやすい。

- AI高度人材3,000名の定義 / 認定方法
- AFT / FDEの人材規模
- AI駆動開発の適用率
- 社員1人当たりのAI利用度
- 上流工程への人員再配置実績
- AIによる粗利 / 生産性改善
- AI時代の若手育成プログラム
- Security × AI人材の育成状況
- 新しい専門職 / 評価制度

## Sources

- NRI「中期経営計画（2026-2028）」  
  https://ir.nri.com/jp/ir/library/businessplan.html
- NRI「2026年5月 機関投資家スモールミーティング 第1部 Q&A」  
  https://ir.nri.com/jp/ir/library/smallmtg.html
- NRI「NRI AFT」  
  https://www.nri.com/jp/news/newsrelease/20260803_1.html
- NRI「Anthropic Japanとのパートナーシップを拡大」  
  https://www.nri.com/jp/news/info/20260224_1.html
