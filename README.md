# 田中 克茂（ossudesu）

介護福祉士として14年間、現場と運営サポート（シフト作成・送迎表作成・職員面談など）を担当してきました。手作業の多さと、判断の根拠が個人の頭の中に溜まっていく状況に課題を感じ、独学でPythonとデータ分析に取り組んでいます。

技術記事：https://zenn.dev/ossudesu

## 進め方について

- 都合のよい数字は作りません。狙った結果が出なかった検証も、そのまま公開しています
- 制限事項と、確かめられていないことは README に明記します
- 現場で使っていたものを公開するときは、利用者・施設の情報が残っていないかを点検してから出します

## どこから見るか

**データ分析に興味がある方**

- [keiba_app](https://github.com/ossudesu-lab/keiba_app) — 地方競馬の予測モデルと回収率の検証。約8,827頭分のデータで8項目を検証し、「単純な手法では市場に勝てない」という結論に至った記録です
- [ec_cohort_rfm_analysis](https://github.com/ossudesu-lab/ec_cohort_rfm_analysis) — 公開データでのコホート分析とRFM分析。人数の多い離反済み層より、戻る見込みの高い離反しかけ層を優先すべき理由を整理しました

**業務システムに興味がある方**

- [kaigo_system](https://github.com/ossudesu-lab/kaigo_system) — ショートステイの予約・入浴計画・稼働レポートを扱う業務システム。設計から実装まで。現場の例外をシステムが止めないこと、紙運用と併存できることを設計方針にしています

**生成AIに興味がある方**

- [kaigo_rag](https://github.com/ossudesu-lab/kaigo_rag) — 外部APIを使わない、ローカル完結のRAG
- [kaigo_agent](https://github.com/ossudesu-lab/kaigo_agent) — 上のRAGの実用性が低いと判断したあとに作った、道具を選んで繰り返すエージェント

## 使っているもの

Python / pandas / scikit-learn / matplotlib / FastAPI / SQLite / Ollama / Git
