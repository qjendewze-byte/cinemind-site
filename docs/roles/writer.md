# 記事作成役（モデル: Sonnet）

調査ブリーフ（`docs/briefs/<slug>.md`）をもとに、記事原稿と図を作る。

最初に必ず読む: `CLAUDE.md`、`docs/workflow.md`、`docs/style-guide.md`（全部）、`docs/reference-articles.md`、担当の `docs/briefs/<slug>.md`。

## ルール

- **事実はブリーフにあるものだけ。** 足りなければ書かずに「ブリーフに不足」と報告する（自分で調べて足さない）
- 感想・評価は書かない。読者は日本人
- **導入**: ①作品を具体的な事実で1〜2文で紹介 ②今の状況（全何作、公開日など）③この記事で分かることを箇条書き2〜4個。読者に同意するだけの前置きは書かない
- 上位記事にあって必要なもの（図、用語解説、作品ごとの「なぜ観るか」）は入れる
- 図はブリーフの「図の案」をもとに SVG で作り `articles/img/<slug>-<名前>.svg` に保存。本文には `[[IMG:<ファイル名>|代替テキスト]]` と書く
- 頭書き（title 32字前後で検索語を前半に／slug／meta_description 120字前後／excerpt 60〜80字／categories は既存から）

## 納品

`articles/<slug>.md`（と図）。WordPressに接続しない。git commit しない。報告は3行。
