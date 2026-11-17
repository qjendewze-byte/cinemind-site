# 作業ボード

更新: 2026-11-17（統括）

## 承認待ち

| ID | 記事 | 備考 |
|---|---|---|
| 554 | 運営者情報ページ（固定ページ） | 【要記入】4か所あり。ユーザー「後でいい」（2026-11-14）。催促しない |

## 作り直し中

（なし）

## 候補（作るかどうか未定）

- 「アイアンマン2 イワン なぜ」など、Search Consoleに出始めた具体的な疑問（2026-10-07 データ）

## 保留

| ID | 記事 | 理由 |
|---|---|---|
| 504 | 現実逃避したい時に見る映画 | 検索の需要が確認できない |
| 545 | 何も考えずに見れる映画 | 同上 |
| 500 | MI1リライト | 狙う価値が低い |

## 定期

- Search Console: 2〜3週間ごとにユーザーからデータをもらい、統括が見る（次回目安: 10月下旬）
- 公開前の再確認: 637・638 は公開直前に出演発表・上映時間を確認（docs/handoff.md）

## メモ


- AWS移行中（docs/aws-migration.md）。旧サーバーのデータは 2026-10-16 に書き出し済み。切り替えまで旧WordPressに書き込まない（書き込んだら切り替え前に書き出し直す）

- 638 を公開したら、542（メッセージ）の末尾にブログカード（postId 638）を足す
- 637 の「運営者情報」へのリンク（/about/）は、554 を公開するまでリンク切れ


## 公開済み（2026-10-30）

MCU新規13本を公開（ID 658〜670、ユーザー指示「下書きはいいから公開しろ」）。アイキャッチ未設定。残り: captain2（471）へ guardians1 のカード、blackpanther へ infinitywar のカード（いずれも公開済み記事の変更）

## 公開・更新（2026-11-14、ユーザー指示「どんどんサイト改善しろ」）

- 公開: 544、個別8本（538, 535, 539, 536, 537, 540, 541, 542）、637、638
- 差し替え: MCU9本（404〜471）。更新前は docs/backup/published-before-2026-11-14/
- 時点情報を2026年11月に更新、「この記事で分かること」を削除（個別8本）。更新前は docs/backup/published-before-2026-11-14b/
- アイキャッチ: 文字だけの形式（tools/make_eyecatch.py、要 `arch -x86_64 /usr/bin/python3`）を全公開記事に。差し替え前のメディアIDは docs/backup/eyecatch-before-2026-11-14.txt
- カード: captain2→guardians1、blackpanther→infinitywar、arrival→dune3-prep、endgame→doomsday-prep
- 637 の運営者情報リンク（/about/）は 554 未公開のため削除
- 637・638 は12月上旬に上映時間などを再確認
- エックスサーバーに書き込んだので、AWS 切り替え前にデータを書き出し直す
- 公開: MCU見る順番ハブ（499、articles/mcu-order.md、事実9・編集8）、ファー・フロム・ホーム（756、articles/ffh.md、事実9・編集8）
- 差し替え: マイ・インターン（149、感想型 → 「プラダを着た悪魔の続編？」、事実9・編集8）
- カード: endgame・spiderman-homecoming → ffh
- SWELL のブログカードはキャッシュ（transient swell_card_id*）される。アイキャッチやタイトルを変えたら、一時スニペットで消す（scratchpad の snip.json と同じ内容）
- 12/18 のドゥームズデイ公開後、mcu-order の「38本」「39本目」を更新

## Search Console 対策（2026-11-17）

- 分析: docs/gsc/analysis-2026-11-17.md（表示は1日100前後、CTR 0.83%、順位8.8）
- 表示の多い11本（ironman2, hulk1, captain2, ironman3, ironman1, ultron, antman2, captain1, infinitywar, civilwar, guardians2）の title・meta・excerpt を検索語に合わせて書き直し、検索語に答える節を追加（案 docs/gsc/proposals-2026-11-17.md、事実確認 9点 docs/gsc/factcheck-2026-11-17.md）。アイキャッチも新 title に合わせた
- MCU全23本の末尾に「MCU全体の見る順番」（mcu-order へのカード）
- 次回: 2〜3週間後に Search Console で11本の CTR と順位を比べる。旧記事（MI・SF単発）は表示ほぼゼロ（noindex 等の問題はなし）

## サイト構造（2026-11-17、docs/seo-plan.md の段階2）

- カテゴリ「MCU」（ID 30、/category/mcu/）を新設し、MCU記事25本に付与。パンくずが「HOME > MCU」になった
- ヘッダーメニュー: 「MCU」（子に「MCU 見る順番」499、「ドゥームズデイの予習」637）を追加。記事0本のカテゴリ（邦画・ドキュメンタリー・ホラー・アニメ・泣きたい夜）を外した
- キャッチコピー「見る順番と前作とのつながりがわかる映画ガイド」、トップの見出し・説明文も変更
- 変更前は docs/backup/structure-before-2026-11-17/。新しいMCU記事を公開したらカテゴリ30も付ける
