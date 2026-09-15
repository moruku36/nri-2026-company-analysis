# Skills Roadmap — 2026〜2028に優先したいスキル

> 基準日: 2026-09-15  
> Public information only.

## Executive take

NRIの公開戦略から逆算すると、2026〜2028で優先度が高いのは「AIツールの操作」ではなく、**AIを企業システム・業務・セキュリティ・収益へ接続する能力**である。

以下はNRIの人事制度や必須資格ではなく、本レポートによる公開情報ベースのスキル優先順位。

---

## Priority A — 最優先

### 1. AI-native Architecture

理解したい要素:

- LLM / multimodal model
- model routing
- RAG / enterprise search
- agent architecture
- tool calling
- MCP等の接続方式
- memory / context management
- evaluation
- fallback
- human approval
- observability

ゴールは「APIを呼べる」ことではなく、**企業で安全・安定・低コストに運用できる設計**を説明できること。

---

### 2. Cloud + AI Platform

AWS / Azure / Google Cloud等のクラウド基礎に加え、

- managed AI platform
- private endpoint
- IAM
- data access
- encryption
- secret management
- GPU / inference cost
- logging
- DR / resilience

まで理解する。

NRIの戦略はベンダーフリー / マルチモデル寄りであるため、1クラウドだけでなく**共通設計原則**を持つことが重要。

---

### 3. AI Security / Governance

優先テーマ:

- AI threat modeling
- prompt injection
- data leakage
- agent privilege
- tool abuse
- model / plugin / MCP supply chain
- audit log
- policy enforcement
- human-in-the-loop
- AI red teaming
- regulatory / governance framework

AIが自律化するほど、IdentityとAuthorizationが重要になる。

---

### 4. Outcome / ROI Design

AFTの方向性では、技術実装だけでなく短周期のROI検証が重要。

身につけたい能力:

- baseline設定
- KPI設計
- cost / benefit
- quality metrics
- adoption metrics
- risk reduction
- experiment design

AI案件は「精度が90%」だけでは事業価値を説明できない。

---

## Priority B — 強い差別化になる

### 5. Modernization

AI導入前提として、

- API design
- event-driven architecture
- container / serverless
- legacy decomposition
- data modernization
- migration strategy
- strangler pattern
- automated testing

を理解する。

AIを既存業務へ入れるには、古いシステムとの接続が避けられない。

---

### 6. Domain Knowledge

最低1領域を深く持つ。

例:

- Financial services
- Insurance
- Retail
- Manufacturing
- Public / social infrastructure
- Cybersecurity operations

Domain knowledgeはLLMに質問すれば出る表層知識ではなく、

- exception
- regulation
- operational constraint
- legacy reason
- stakeholder structure

まで理解すること。

---

### 7. AI-assisted Software Engineering

使うだけではなく、開発プロセスを再設計する。

- coding agent
- automated review
- test generation
- specification generation
- reverse engineering
- documentation
- CI/CD integration
- security scanning

重要なのは、AI生成量ではなく**品質 / 工数 / defect率の変化を測ること**。

---

### 8. Observability / Evaluation

AIシステムは通常のアプリより挙動が非決定的。

必要になるのは、

- trace
- token / latency / cost
- response evaluation
- hallucination / failure
- tool execution log
- user feedback
- drift

の観測。

Production AIでは評価基盤が重要なインフラになる。

---

## Priority C — 人間側の価値を守る

### 9. Problem Framing

曖昧な経営課題を、AIで解ける問題へ分解する。

### 10. Technical Decision Writing

「何を選んだか」ではなく、

- options
- constraints
- trade-offs
- decision
- consequence

を短く説明する。

### 11. Facilitation / Conflict Resolution

AIが提案を大量生成しても、ステークホルダー間の利害は消えない。

### 12. Accountability

AI出力をそのまま採用せず、最終判断の根拠を説明できる。

---

## Role-based roadmap

### Cloud / Platform

**2026**
- LLM / Agent基礎
- AWS / Azure / GCPのAIサービス比較
- IAM / Private Network

**2027**
- Enterprise RAG
- Agent runtime
- Multi-model architecture
- AI FinOps / Observability

**2028**
- Organization-wide AI platform
- governance-as-code
- reusable architecture / platform engineering

---

### Security

**2026**
- OWASP LLM / Agent系リスク
- AI governance基礎
- prompt / tool threat model

**2027**
- agent identity
- AI red teaming
- AI SOC automation
- audit / monitoring

**2028**
- enterprise AI security architecture
- autonomous-agent control plane
- cross-cloud AI governance

---

### PM / Delivery

**2026**
- GenAIをPM業務へ活用
- AI案件のKPI / ROI
- model risk理解

**2027**
- FDE型の短周期デリバリー
- agentic workflow案件
- outcome-based planning

**2028**
- portfolio-level AX management
- AI investment prioritization
- organization transformation

---

### Architecture / Modernization

**2026**
- legacy discovery with AI
- API / event architecture
- IaC / CI/CD

**2027**
- AI-assisted modernization
- data / identity modernization
- automated migration / testing

**2028**
- AI-native enterprise architecture
- reusable modernization platform

---

## Portfolio evidence > qualification only

資格は基礎知識の証明として有効だが、AI時代には以下の証跡を残す方が強い。

### Architecture Decision Record

なぜそのモデル / クラウド / IAM設計を選んだか。

### Before / After

AI導入前後の工数・品質・コスト。

### Threat Model

AI Agentの権限と攻撃面。

### Evaluation

AI出力をどう測定したか。

### Reusable asset

Terraform module、policy、evaluation harness、runbook等。

### Postmortem

何が失敗し、何を改善したか。

---

## Avoid overfitting to one model

2026年はフロンティアモデルの更新が非常に速い。

したがって、

- Claude固有機能
- GPT固有API
- Gemini固有UI

だけを覚えるのではなく、

- context
- tools
- agents
- eval
- identity
- security
- observability

という共通概念を理解する。

NRIの公開戦略も、特定モデルを固定するよりベンダーフリー / 最適技術の組み合わせを強調している。

---

## Suggested learning allocation

技術者の学習時間を100とした場合の一例:

| 領域 | 配分 |
|---|---:|
| Core specialty (Cloud / Security / PM / Architecture) | 35 |
| AI / Agent architecture | 25 |
| Hands-on implementation | 20 |
| Domain / business | 10 |
| Communication / decision / ROI | 10 |

ポイントは、AIだけで100にしないこと。

---

## Final principle

2026〜2028の強い人材像は、

> AIをたくさん使う人

ではなく、

> **AIを使って、以前より大きな責任範囲を安全に持てる人**

である。

## Sources

- NRI「中期経営計画（2026-2028）」  
  https://ir.nri.com/jp/ir/library/businessplan.html
- NRI「NRI AFT」  
  https://www.nri.com/jp/news/newsrelease/20260803_1.html
- NRI「Anthropic Japanとのパートナーシップを拡大」  
  https://www.nri.com/jp/news/info/20260224_1.html
- NRI「AIをマネジメントする新たなホワイトカラー職の開発と育成」  
  https://www.nri.com/jp/knowledge/publication/chitekishisan_202604/05.html
