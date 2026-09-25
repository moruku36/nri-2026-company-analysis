# AI Products / Services — 2026

基準日: 2026-09-25

## 1. NRI AFT（AI Field Transformer）

2026年8月3日提供開始。

特徴は、AX支援チームとFDEが顧客現場へ入り、構想策定から実装・運用まで一気通貫で支援する点。

### 主な要素

- 日本企業固有の業務知識・商習慣への理解
- 経営と現場をつなぐコンサルティング
- 現場常駐型のFDE
- 高速なROI検証
- 暗黙知の形式知化
- AIエージェントへの知識反映
- セキュアなAIプラットフォーム

```mermaid
flowchart TD
    subgraph Client["顧客エンタープライズ"]
        Mgmt["<b>経営層 / 事業部門長</b><br>経営課題・ROI要求・変革方針"]
        Field["<b>業務現場 / 実務担当者</b><br>現場オペレーション・業務暗黙知・既存システム"]
    end

    subgraph NRI_AFT["NRI AFT (AI Field Transformer) 体制"]
        Consultant["<b>AXコンサルタント</b><br>構想策定・ROIモデリング・変革合意形成"]
        FDE["<b>FDE (Forward Deployed Engineer)</b><br>現場常駐・高速プロトタイプ・暗黙知コード化"]
        Platform["<b>セキュアAI基盤 & ガバナンス</b><br>AgenticBlue・統制ログ・マルチクラウド接続"]
    end

    Mgmt <--> Consultant
    Field <--> FDE
    Consultant <--> FDE
    FDE <--> Platform
```

### 分析

AFTはAI PoC支援のブランドではなく、AI時代向けのデリバリーモデル再設計として見る方が重要。

---

## 2. Anthropic / Claude導入支援

2026年2月にパートナーシップを拡大。

提供対象はLLM利用だけでなく、

- Claude
- Claude Code
- Claude for Enterprise
- Claude Cowork検証
- コンサルティング
- 導入 / 実装
- 運用支援

まで広がる。

NRI自身もClaude for Enterpriseを導入し、自社利用で得たノウハウを顧客支援へ還流するモデル。

---

## 3. AI共創モデル

2025年からAWS・Google Cloud等との共創モデルを強化。

### AWS

生成AI分野で戦略的協業し、AI導入支援、特化型AIエージェント、業界・タスク特化LLM、AIセキュリティ等を展開。

### Google Cloud

Vertex AI / Gemini Enterprise等を使い、業種・業務別AIエージェントを開発する体制を整備。

### 分析

特定クラウドへロックインするより、「顧客要件に応じて複数クラウド / モデルを組み合わせるSIer」としての立場を維持しようとしている。

---

## 4. 業界・タスク特化型LLM

2026年3月、GENIAC第3期の成果として、金融業務に特化したLLM構築手法を発表。

特定の金融実務タスクではGPT-5.2を上回る精度を確認したとしている。

### 重要な点

これは「NRIが巨大基盤モデル競争へ参入する」という意味ではない。

むしろ、

> 汎用LLM + 顧客 / 業界特化モデル + エージェント

という構成で、専門業務の精度を上げる戦略。

---

## 5. 社会レジリエンスAI

2026年5月、東京大学田中研究室の知見を基に構想を発表。

熟練者の知見・業務データを入力として、AIエージェントが

- 変化検知
- 要因分析
- 対策提案

を自律的に行い、継続的に精度を高める。

### 分析

NRIのAI戦略に一貫しているのは「暗黙知の形式知化」。

AFTでも社会レジリエンスAIでも、人間の経験知をAIへ移植することが重要テーマになっている。

---

## 6. AgenticBlue / AI SOC

2026年8月6日、NRI SecureがNeoSOCに独自AI統制基盤「AgenticBlue」を導入。

AIが、

- アラートトリアージ
- 一次調査
- 分析
- 脅威重要度判定
- 報告作成

まで自動化する。

AgenticBlueは、

- アクセス制御
- 認証情報管理
- 機密データ保護
- AI判断過程の記録 / 可視化
- 複数AIによる相互検証

を備える。

### 分析

これは「AIセキュリティをコンサルする」だけでなく、NRI自身の運用サービスをAIネイティブ化する実例。

---

## 7. AIガバナンス支援

2026年8月27日、NRI SecureはAI等のエマージングテクノロジーを対象に、セキュリティガバナンス構築支援を開始。

9月16日には三菱重工とAI等を用いた業務プロセス改革で共同検討・実装支援を開始。技術動向調査、AIガバナンス策定、デジタルアプリケーションの共同開発を含む。9月17日にはフロンティアAI対応脆弱性診断で国内データ処理体制を公表した。詳細は[AIセキュリティ・ガバナンス](./ai-security-governance.md)と[公式資料一覧](../sources/official-sources.md)を参照。

AIエージェント普及により、従来の情報セキュリティ統制だけでは足りなくなることを前提にしている。

9月には「エージェント時代のAIガバナンス」をテーマに、経営・プロセス・技術の3層ガードレールを打ち出している。

### 2026年8月 IR Dayで示された商用化状況

8月26日のIR Day質疑応答で、NRIはフロンティアAI対応脆弱性診断サービスが既に売上計上されていると説明した。利用モデルはClaude MythosではなくClaude Opusで、ベンダーフリー方針のもと他モデルも継続評価している。導入社数は非開示だが、金融ビジネスプラットフォームサービスには導入済みと説明している。

AI-IPについては、AI-IP案件の売上を既存事業と分けて集計しておらず、定量目標や案件比率の算出が難しい一方、中計2028の増収に寄与し、その比率は中計期間後も高まるとの会社見通しが示された。基盤領域では受託案件の半数超でIPを活用する一方、業務プロセスを部品化したAI-IPの顧客適用は数社にとどまるとの説明であり、成熟度を分けて評価する必要がある。

出典：[IR Day質疑応答](https://ir.nri.com/jp/ir/library/outline/main/01/teaserItems1/013/linkList/010/link/260826pre_qa.pdf)。

---

## 8. サービス群を構造化すると

```mermaid
flowchart TD
    subgraph S1["① 戦略・構想"]
        A1["AXコンサルティング"]
        A2["NRI AFT (現場伴走)"]
        A3["業界別・社会レジリエンス構想"]
    end

    subgraph S2["② AI基盤 / モデル調達"]
        B1["Anthropic Claude"]
        B2["Google Cloud (Gemini) / AWS Bedrock"]
        B3["金融・業界特化型LLM (GENIAC)"]
    end

    subgraph S3["③ 実装・開発"]
        C1["FDE (現場常駐開発)"]
        C2["AIエージェント構築"]
        C3["AIネイティブ・モダナイゼーション"]
    end

    subgraph S4["④ 運用・高度化"]
        D1["AI SOC (AgenticBlue)"]
        D2["ミッションクリティカル保守運用"]
        D3["継続的ROI改善サイクル"]
    end

    subgraph S5["⑤ 統制・ガバナンス"]
        E1["AIセキュリティ (NRI Secure)"]
        E2["エージェント時代のAIガバナンス (3層ガードレール)"]
    end

    S1 --> S2 --> S3 --> S4 --> S5
```

## 評価

NRIのAIサービス群は点在して見えるが、2026年になるとかなり一本のストーリーになってきた。

**「構想 → 実装 → エージェント化 → 運用 → 統制」まで全部取る**ことが狙い。

今後の課題は、これらが個別サービスの寄せ集めではなく、案件として本当に横断的に連携できるか。

## Sources

- https://www.nri.com/jp/news/newsrelease/20260803_1.html
- https://www.nri.com/jp/news/info/20260224_1.html
- https://www.nri.com/jp/news/newsrelease/20260327_1.html
- https://www.nri.com/jp/news/newsrelease/20260514_1.html
- https://www.nri.com/jp/news/info/20260806_1.html
- https://www.nri.com/jp/news/newsrelease/20260827_1.html
- https://www.nri.com/jp/news/event/2026_ai_governance.html
