# Role Shifts in the AI Era — AIで仕事の価値はどこへ移るか

> 基準日: 2026-09-15  
> Public information only.

## Executive take

AIによってNRIの仕事が一律に減るとは考えにくい。公開情報から見えるのは、**定型的な実行作業の価値が下がり、課題設定・設計・判断・統合・責任の価値が上がる**という役割再配分である。

NRI自身も、AI駆動開発で生まれた余力を上流工程や新規案件へ移す考えを投資家へ説明している。

---

## 1. 価値が下がりやすい仕事

### 定型コーディング

AIコード生成・変換・テスト生成が進むほど、仕様が明確で反復性の高い実装は自動化しやすい。

NRI自身もAI駆動開発の初期段階でコーディング / テスト工程へAIを適用し、工数削減を確認している。

### 定型テスト

テストケース生成、テストコード作成、結果整理等はAI / 自動化の適用余地が大きい。

### 定型資料作成

- 議事録
- 定例報告
- 調査要約
- 既存テンプレートへの転記
- 初稿作成

などは生成AIのコモディティ領域になる。

### 手順化された運用

Runbookに落とせる監視、一次調査、レポート作成などはAgentic AIの対象になりやすい。

NRI SecureのAgenticBlueは、SOCにおいてトリアージから一次調査、分析、報告作成までAI化する例を示している。

### 情報中継だけのPM / PMO

「担当者から聞いた内容を別の担当者へ伝える」「進捗を転記する」「会議を設定する」ことが中心ならAI代替圧力は高い。

---

## 2. 価値が上がりやすい仕事

### Problem Framing / 課題設定

AIは与えられた問いへの回答は得意だが、

- 本当に解くべき問題は何か
- どこまで自動化すべきか
- 何を自動化してはいけないか

を決めるには顧客・業務・経営への理解が必要。

### Architecture

AI時代はアーキテクチャが単純になるとは限らない。

むしろ、

- 複数モデル
- 複数クラウド
- データ基盤
- 既存システム
- Agent / MCP等の接続
- Identity
- Security
- Observability
- Cost

を統合する設計が必要になる。

### AI Governance / Security

AIエージェントが自律的に外部システムを操作するほど、

- 権限設計
- データ境界
- 監査ログ
- Human-in-the-loop
- モデルリスク
- プロンプトインジェクション対策
- サプライチェーンリスク

の重要性が増す。

### Domain Knowledge

NRIがAFTで繰り返し強調しているのは、日本企業固有の業務知識・商習慣・暗黙知。

モデル能力が上がるほど、誰でも使える汎用知識より、**顧客固有の文脈を構造化できる人**が重要になる。

### Outcome / ROI Design

PoCを作るだけではなく、

- 何円削減できるか
- 売上がどう増えるか
- リードタイムがどう変わるか
- リスクがどう減るか

まで定義し、継続的に測定する能力が価値を持つ。

### Final Decision / Accountability

NRIの研究では、人の役割を「AIをマネジメントする」方向へ再定義し、

1. 業務設計
2. AIへの指示
3. 出力の解釈と選定
4. 最終決定と責任

という4つの能力を提示している。

これはNRIの社内人事制度そのものではないが、AI時代のホワイトカラー像として示唆が大きい。

---

## 3. Software Engineerはどう変わるか

### Before

```text
Requirement
   ↓
Design
   ↓
Coding
   ↓
Test
   ↓
Release
```

人間が各工程を順番に実行。

### After

```text
Problem / Requirement
        ↓
Architecture & Constraints
        ↓
AI Agent / Coding Agent
        ↓
Human Review / Verification
        ↓
Automated Test / Security / Policy
        ↓
Production Feedback
        ↺
```

人間の役割は「書く」から、

- 制約を与える
- 構造を決める
- 検証する
- 判断する
- 改善ループを設計する

へ移る。

### Implication

コードを書けなくてよい、ではない。

**AIが出したコードを評価できるレベルの技術理解**はむしろ必要になる。

---

## 4. Cloud Engineer / Architectはどう変わるか

クラウド構築そのものはIaCとAIでさらに自動化される。

一方で価値は、

- Multi-cloud / Hybrid architecture
- AI platform architecture
- IAM / workload identity
- Data residency
- FinOps
- Observability
- Resilience
- Model / Agent runtime
- Secure connectivity

へ移る。

特に企業AIでは、モデルより周辺インフラの設計が本番導入のボトルネックになりやすい。

したがってクラウド専門性は消えるより、**AIアプリケーションの基盤専門性へ拡張する**。

---

## 5. Security Engineerはどう変わるか

セキュリティは2026〜2028のNRI成長領域そのもの。

AI時代には従来の

- Network
- Endpoint
- IAM
- SOC
- Application Security

に加え、

- AI Governance
- Agent Identity
- AI red teaming
- Prompt / Context security
- Model / tool supply chain
- AI auditability
- Autonomous action control

が加わる。

### Implication

**Security × AIは、NRI内でも市場全体でも希少性が高い組み合わせ**になりやすい。

---

## 6. PM / Project Managerはどう変わるか

PMの価値は「管理作業」から「意思決定設計」へ移る。

### AIへ委譲しやすい

- 会議要約
- WBS更新補助
- ステータスレポート
- リスク候補抽出
- 課題一覧の整理
- 文書ドラフト

### 人間側に残りやすい

- スコープ / 優先順位決定
- 顧客期待値調整
- トレードオフ判断
- 高リスク判断
- 契約 / 責任境界
- ROI
- 複数チーム / ベンダー間の設計
- AI出力に対する最終責任

### Strong PM

今後強いPMは、

> project administrator

ではなく、

> business / technology / risk integrator

に近づく。

---

## 7. Consultantはどう変わるか

調査・資料作成そのものは急速にAI化する。

コンサルタントの差別化は、

- 問いを作る
- 経営者と合意形成する
- 業務を再設計する
- AI実装チームへつなぐ
- 実装後の成果まで追う

へ移る。

AFTが「構想から実装・運用まで」を強調するのは、この境界が薄くなることを示している。

---

## 8. Junior / 若手育成の難しさ

AIが下流作業を代替すると、従来若手が

- コードを書く
- テストする
- 調査する
- 資料を作る

ことで身につけた基礎経験が減る。

これは生産性向上の裏側にある重要な組織課題。

### 必要になる育成方法

- AI生成物をレビューする訓練
- 小さな本番責任を早く持たせる
- Architecture / Securityレビューへの参加
- AI利用ログを教材化
- Failure caseの共有
- Domain knowledgeの体系化

「AIに全部やらせる」のではなく、**AIを使いながら基礎理解を形成する育成設計**が必要になる。

---

## 9. 役割の価値マップ

| 仕事 | AI代替圧力 | 将来価値 | 理由 |
|---|---|---|---|
| 定型コーディング | 高 | 低下 | Coding Agent |
| 定型テスト | 高 | 低下 | 自動生成 / 自動実行 |
| 定型資料 | 高 | 低下 | GenAI |
| 手順運用 | 高 | 低下 | Agentic automation |
| 調整だけのPMO | 高 | 低下 | AI workflow |
| Architecture | 中 | 上昇 | 複雑な統合判断 |
| Cloud + AI Platform | 中 | 上昇 | AI本番基盤 |
| Cybersecurity | 低〜中 | 上昇 | 攻撃面拡大 |
| AI Governance | 低 | 大幅上昇 | 規制 / 統制 |
| Domain expertise | 低 | 上昇 | 顧客固有コンテキスト |
| FDE / AX delivery | 中 | 上昇 | 現場実装 |
| Outcome / ROI design | 低 | 上昇 | 価値証明 |
| Final decision | 低 | 上昇 | 責任は人間側 |

---

## Sources

- NRI「2026年5月 機関投資家スモールミーティング 第1部 Q&A」  
  https://ir.nri.com/jp/ir/library/smallmtg.html
- NRI「AIをマネジメントする新たなホワイトカラー職の開発と育成」2026-04  
  https://www.nri.com/jp/knowledge/publication/chitekishisan_202604/05.html
- NRI「NRI AFT」2026-08-03  
  https://www.nri.com/jp/news/newsrelease/20260803_1.html
- NRI Secure「NeoSOCへのAgenticBlue導入」2026-08-06  
  https://www.nri.com/jp/news/info/20260806_1.html
