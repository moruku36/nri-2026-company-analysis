# NRI 2026 Company Analysis

> 株式会社野村総合研究所（NRI）の2026年の方向性・経営・AI戦略・市場評価を、公開情報から継続的に分析する個人向けリサーチリポジトリ。
>
> **基準日: 2026-09-15**

## このリポジトリの目的

このリポジトリは、2026年のNRIについて「会社は実際にどこへ向かおうとしているのか」を、IR資料だけでなく、経営陣の発言、AI関連施策、業績・株価、競合企業、外部報道・市場評価まで横断して把握することを目的とする。

単なるニュースの時系列整理ではなく、以下を区別して読む。

- **Fact**: NRIや第三者が公表した事実
- **Management message**: 経営陣が株主・社員・市場へ伝えているメッセージ
- **Interpretation**: 複数の公開情報から読み取れる方向性
- **Outside view**: 記者、アナリスト、投資家、一般ユーザーなど外部からの評価
- **Implication**: NRIで働く個人の視点から見た意味

---

## Executive Summary — first scan

### 1. 2026年の中心テーマは「DXの続き」ではなく、AXへの移行

2026年4月に公表された中期経営計画（2026-2028）では、AIによるビジネス変革が成長領域として明示されている。さらに5月の中計フォローアップでは「企業のAX（AI変革）動向とNRIの戦略・取り組み」「コンソリューションとプラットフォームで牽引するAXシフト」が独立した投資家向けテーマになった。

現時点では、NRIはAIを単なる社内生産性向上策としてではなく、**次のコンサルティング／ITサービス需要を作る経営テーマ**として位置付けている、と読むのが妥当である。

### 2. 8月以降、AX戦略が「現場実装」の形に具体化

2026年8月3日、NRIは **NRI AFT（AI Field Transformer）** を発表した。

特徴は、構想策定だけで終わらず、FDE（Forward Deployed Engineer）が顧客現場に入り、ROI検証を高速に回しながら、業務の暗黙知を形式知化しAIエージェントへ取り込む点にある。

これは従来型の「AI PoC支援」より踏み込んだモデルであり、NRIが持つ

- コンサルティング
- 業界・業務知識
- システム実装力
- 顧客との長期関係
- セキュリティ／運用能力

をAI時代向けに再結合しようとしている動きとして重要である。

### 3. 社長メッセージでもAIは「ツール」から「パートナー」へ

柳澤花芽社長は2026年6月の発信で、AIの位置付けが生産性向上のための道具や壁打ち相手から、経営にも関わる「パートナー」へ広がっているとの認識を示している。

個別技術の導入論よりも、**AIを前提に組織・経営・価値創造のあり方を組み替える**方向へ経営メッセージが寄っている点を今後詳しく検証する。

### 4. AI推進と同時に、セキュリティ・ガバナンスを事業機会として取り込む

NRI Secureは2026年8月27日、AIなどのエマージングテクノロジーを対象としたセキュリティガバナンス構築支援サービスを開始した。

NRIグループ全体を見ると、AIを「導入する側」だけではなく、**AI導入で新たに発生する統制・セキュリティ・運用需要まで含めて取り込む構図**になっている。

### 5. 8〜9月のフロンティアモデル競争への直接反応は要追加調査

2026年8〜9月のOpenAI、Anthropic等の最新モデル登場後について、9月15日時点の一次スキャンでは、特定モデル名を挙げてNRI全社の戦略変更を示した公式発表はまだ明確には確認できていない。

ただし、同時期にはAFT、AIセキュリティガバナンス、AI時代の経営に関する発信が継続しているため、**モデル単位の追随より「マルチモデルを前提に、企業変革・実装・統制を握る」戦略なのか**を後続調査で検証する。

---

## 最終レポート構成

```text
nri-2026-company-analysis/
├── README.md                         # 全体像・結論・読み方
├── 01-management/
│   ├── strategy-2026-2028.md         # 中期経営計画と経営戦略
│   ├── president-messages.md         # 柳澤社長・経営陣の発言分析
│   └── timeline-2026.md              # 2026年重要イベント時系列
├── 02-financial-market/
│   ├── financial-performance.md      # 業績・事業別動向
│   ├── stock-price.md                # 株価・バリュエーション・イベント分析
│   └── shareholder-message.md        # 株主・投資家向け説明の変化
├── 03-ai-ax/
│   ├── ai-strategy.md                # NRIのAI/AX戦略
│   ├── frontier-model-impact.md       # OpenAI/Anthropic等の最新モデル影響
│   ├── ai-products-services.md        # AFT・AI Agent・LLM等のサービス
│   ├── internal-ai-transformation.md # NRI自身のAI活用・働き方変革
│   └── ai-security-governance.md     # AIセキュリティ・統制
├── 04-business/
│   ├── consulting.md
│   ├── financial-it.md
│   ├── industrial-it.md
│   ├── platforms.md
│   └── global-business.md
├── 05-competition/
│   ├── competitor-map.md             # 競争環境の全体像
│   └── competitor-comparison.md      # Accenture/NTT DATA/IBM等との比較
├── 06-external-view/
│   ├── media-analyst-view.md          # 記者・アナリスト評価
│   ├── investor-view.md               # 市場・投資家の見方
│   └── public-reputation.md           # 一般公開情報上の評判・論点
├── 07-people-work/
│   ├── talent-organization.md         # 人材戦略・組織・採用
│   └── implications-for-moruku.md     # 個人視点での示唆
├── 08-synthesis/
│   ├── strengths-risks.md             # 強み・弱み・機会・リスク
│   ├── scenarios-2027-2030.md         # 今後のシナリオ
│   └── final-assessment.md            # 総合評価
└── sources/
    ├── official-sources.md            # NRI一次情報
    ├── external-sources.md            # 報道・競合・第三者資料
    └── research-log.md                # 調査履歴・未確認事項
```

## 調査原則

1. NRI公式IR・ニュースリリース・経営陣発言を一次情報として優先する。
2. 経営計画上の「言っていること」と、実際のサービス・投資・採用・提携等の「やっていること」を分けて評価する。
3. AIについてはモデル性能競争だけでなく、顧客導入、ROI、組織変革、ソフトウェア開発、生産性、セキュリティ、ガバナンスまで見る。
4. 株価は価格推移だけでなく、決算・中計・AI発表等のイベントとの関係を分析する。
5. 競合比較は国内SIerだけに限定せず、Accenture、IBM、Deloitte等のグローバル企業も含める。
6. 外部評価は肯定・否定の両面を収集し、NRI自身の主張と混同しない。
7. 重要な判断には可能な限り出典と日付を残す。

## 初期一次情報

- NRI IR — 中期経営計画（2026-2028）  
  https://ir.nri.com/jp/ir/library/businessplan.html
- NRI IR — 決算短信・説明会資料  
  https://ir.nri.com/jp/ir/library/financial.html
- NRI — NRI AFT（AI Field Transformer）提供開始（2026-08-03）  
  https://www.nri.com/jp/news/newsrelease/20260803_1.html
- NRI — 柳澤花芽社長「AI活用経営と多様性」（2026-06-19）  
  https://www.nri.com/jp/media/journal/20260619.html
- NRI Secure — エマージングテクノロジーに関するセキュリティガバナンス構築支援（2026-08-27）  
  https://www.nri.com/jp/news/newsrelease/20260827_1.html
- NRI — The AI-Augmented Society: 203X（2026-05-28）  
  https://www.nri.com/jp/knowledge/report/20260528_1.html

---

## Status

**Commit 1 / Research initialized**

次回以降、各章を小さなコミット単位で追加し、その都度内容をレビューする。
