# IBM / Deloitte — 2026 Competitive Analysis

基準日: 2026-09-15

この2社はNRIと競合するが、攻め方が異なる。

- IBM：**AI Agentの運用・統制プラットフォーム**を取りに来る
- Deloitte：**経営・業務再設計・Risk/Governance**の上流を取りに来る

NRIから見ると、IBMは下から、Deloitteは上から価値領域を圧縮する存在。

---

# Part A — IBM

## 1. 2026年の中心テーマ：Agentic Control Plane

IBMはThink 2026でwatsonx Orchestrateを拡張し、企業内に増殖するAI Agentを一元管理する **Agentic Control Plane** を前面に出した。

対象はIBM製Agentだけではなく、

- 自社開発Agent
- 他社製Agent
- 複数フレームワーク
- 複数環境

を含む。

運用レイヤーでは、

- 可視化
- Guardrail
- Identity / Credential
- Audit Log
- Agent Catalog
- Monitoring
- Scheduling

等を提供する。

### NRIへの意味

Agentic AIが本番化すると、価値は「Agentを作れること」から「数百・数千Agentを安全に運用できること」へ移る。

IBMはこの共通基盤を製品として取りに来ている。

もしこのレイヤーがwatsonx等で標準化されれば、NRIが独自に作る統制・運用機能の一部はコモディティ化する可能性がある。

---

## 2. Governanceをリアルタイム運用へ統合

IBMはwatsonx.governanceとOrchestrateを結び、Agentの挙動を

- Risk
- Control
- Mitigation
- Business KPI

と関連付け、運用中に継続監視する方向へ進んでいる。

### NRIとの競合

NRI SecureもAgenticBlueやAI Governance支援で同じ課題を扱っている。

違いは、IBMが横断製品として売るのに対し、NRIは顧客固有システム・業務・セキュリティ運用まで入り込む点。

NRIはIBM製品を競合ではなく部品として使う選択もできるため、全面対立ではない。

---

## 3. IBMの強み

- Hybrid Cloud / Mainframe / Middlewareとの接続
- 大企業の既存ITに深く入っている
- Agent Orchestrationをプロダクトとして提供
- AI Governance / Assuranceの製品群
- Red Hat等を含むOpen / Hybrid戦略

### NRIの優位

IBMは汎用基盤に強いが、日本企業の業務・制度・商習慣を個別に理解する部分ではNRIが優位を作りやすい。

NRIはIBMのようなHorizontal Platformを自前で全面構築するより、**顧客コンテキストと業務Agentの設計に集中する方が合理的**。

---

# Part B — Deloitte

## 4. Agentic BPR

Deloitte Japanは2026年6月、「Agentic BPR」を打ち出した。

発想は、既存業務へAI Agentを追加するのではなく、**AI Agentが存在することを前提に業務プロセスそのものを再設計する**というもの。

これはNRIのAXコンサルと非常に近い。

### 競争ポイント

Deloitteは経営・組織・Finance・HR・Risk等まで含む業務変革に強く、システム部門だけでなくCXOアジェンダから入りやすい。

NRIは実装・既存IT・長期運用まで一体で提供できる点で対抗する。

---

## 5. Google Cloud Agentic Transformation Practice

2026年4月、DeloitteはGoogle Cloud / Gemini Enterpriseを軸に専任のAgentic Transformation Practiceを設置。

Deloitte Ascend等の自社アセットとGoogle AIを組み合わせ、Agentic AIを大企業・公共へ展開する。

### NRIへの意味

「コンサル会社は実装できない」という古い区分は通用しなくなっている。

Deloitteもクラウド・Agent・Engineeringまで降りてきているため、NRIのコンサル/IT境界の優位性は以前より小さい。

---

## 6. 2026-09-02：Open Model Engineering

Deloitteは9月2日、**Open Model Engineering practice**を発表。

狙いは、オープンモデルとプロプライエタリモデルを組み合わせ、

- Deployment flexibility
- Cost predictability
- Sovereignty
- Data / IP control
- Model behavior transparency

を重視する企業AIを構築すること。

さらにFY2027に向けFDEの採用・育成・認定を進めるとしている。

### NRIとの比較

NRIもマルチモデル / マルチクラウドを掲げるが、Deloitteは「Open Model Engineering」という分かりやすい市場メッセージでVendor neutralityを商品化している。

NRIもモデル選定・ソブリンAI・閉域環境等を、個別技術論ではなく明確なサービス体系として見せる余地がある。

---

## 7. Deloitte自身の業務もAgent化

2026年6月、Deloitteは監査プラットフォームOmniaに複数AI Agentが連携する仕組みを導入。

約85,000人のAudit & Assuranceプロフェッショナルを対象に、Agentを日常ワークフローへ埋め込む。

### 意味

Deloitteも「Customer Zero」、つまり自社業務をAIで変え、その知見を顧客へ提供するモデルを強化している。

これはNRIのClaude社内導入、AI駆動開発、AgenticBlueと同じ競争ロジック。

---

## 8. NRIへの示唆

### IBMからの示唆

Agent運用・監視・権限管理は独自開発に固執しない。

標準Control Planeを使いながら、NRI固有の価値を

- 金融規制
- 業務ルール
- 顧客固有権限
- SOC / Security運用

に上乗せする方が有利。

### Deloitteからの示唆

AFTを「AI導入サービス」と見せるだけでは弱い。

経営層に対して、

> どの業務を消すか / 再設計するか / 人とAgentの責任分界をどう変えるか

まで提言できる必要がある。

## Sources

### IBM
- Think 2026 AI recap  
  https://www.ibm.com/think/news/think-2026-ai-recap
- Agentic Control Plane / watsonx Orchestrate, 2026-05-05  
  https://www.ibm.com/new/announcements/manage-all-your-ai-agents-in-one-place-with-watsonx-orchestrate
- IBM Think 2026 announcement  
  https://newsroom.ibm.com/2026-05-05-think-2026-ibm-delivers-the-blueprint-for-the-ai-operating-model-as-the-ai-divide-widens
- watsonx governance / assurance  
  https://www.ibm.com/think/perspectives/ai-governance-to-assurance-what-we-shared-think-2026

### Deloitte
- Agentic BPR, 2026-06-18  
  https://www.deloitte.com/jp/ja/services/consulting/perspectives/agentic-bpr.html
- Google Cloud Agentic Transformation Practice, 2026-04-22  
  https://www.deloitte.com/global/en/about/press-room/ai-transformation-gemini-enterprise-google-cloud.html
- Open Model Engineering, 2026-09-02  
  https://www.deloitte.com/global/en/about/press-room/deloitte-launches-open-model-engineering-practice.html
- Deloitte Omnia Agentic Intelligence, 2026-06-24  
  https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html
