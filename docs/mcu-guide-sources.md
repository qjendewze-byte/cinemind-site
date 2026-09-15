# MCU見る順番ガイド：事実確認の記録

`articles/mcu-viewing-order.md` の執筆にあたり確認した事実と、その出典。作成日 2026-09-15。

**制約事項：** このセッションでは WebFetch が環境のネットワークポリシーによりほぼ全てのドメイン（Wikipedia、Rotten Tomatoes、IMDb、Marvel公式など）で `EGRESS_BLOCKED` エラーとなり、使用できなかった。そのため、事実確認はすべて WebSearch（検索結果の要約と引用元リンク）で行っている。検証セッションは、下記の出典URLについて可能であれば個別にアクセスして裏取りすることを推奨する。

## 検証済み事項

### サイト内リンク9本の実在確認
`curl` で以下9URLすべてが200を返すことを確認済み（ironman1, hulk1, ironman2, thor1, captain1, avengers, ironman3, thor2, captain2）。

### 公開済み作品の範囲
2026年9月15日時点で、MCU劇場公開映画は38本（フェーズ1〜6）。フェーズ6の「アベンジャーズ：ダウンズデイ」は2026年12月公開予定のため、本記事では未公開として除外した。「スパイダーマン：ブランド・ニュー・デイ」は日本公開2026年7月31日で、基準日より前のため収録した。
- 出典: WebSearch結果（Plex, GamesRadar+, macmyths.com 等の集計記事、複数のsonypictures.jp/映画.comプレスリリース）

### 上映時間（分）
英語圏の一般的な上映時間表記（時間・分）をWebSearchで取得し、分に換算した。国際版と日本公開版で上映時間が異なるという情報は見つからなかったため、同一として扱った。

| 作品 | 上映時間 | 出典（検索でヒットした主なページ） |
|---|---|---|
| アイアンマン | 126分 | en.wikipedia.org/wiki/Iron_Man_(2008_film), convertunits.com |
| インクレディブル・ハルク | 114分 | boxofficemojo.com, IMDb technical specifications |
| アイアンマン2 | 125分 | IMDb technical specifications, boxofficemojo.com |
| マイティ・ソー | 115分 | murphysmultiverse.com（Marvel Studios Movie Runtimes） |
| キャプテン・アメリカ／ザ・ファースト・アベンジャー | 124分 | marvelcinematicuniverse.fandom.com, IMDb |
| アベンジャーズ | 143分 | IMDb technical specifications, boxofficemojo.com |
| アイアンマン3 | 130分 | murphysmultiverse.com |
| マイティ・ソー／ダーク・ワールド | 112分 | murphysmultiverse.com |
| キャプテン・アメリカ／ウィンター・ソルジャー | 136分 | murphysmultiverse.com |
| ガーディアンズ・オブ・ギャラクシー | 122分 | murphysmultiverse.com |
| アベンジャーズ／エイジ・オブ・ウルトロン | 141分 | britannica.com, murphysmultiverse.com |
| アントマン | 117分 | murphysmultiverse.com |
| シビル・ウォー／キャプテン・アメリカ | 147分 | screenrant.com, murphysmultiverse.com |
| ドクター・ストレンジ | 115分 | murphysmultiverse.com |
| ガーディアンズ・オブ・ギャラクシー：リミックス | 136分 | murphysmultiverse.com |
| スパイダーマン：ホームカミング | 133分 | murphysmultiverse.com |
| マイティ・ソー バトルロイヤル | 130分 | murphysmultiverse.com |
| ブラックパンサー | 134分 | murphysmultiverse.com |
| アベンジャーズ／インフィニティ・ウォー | 149分 | murphysmultiverse.com |
| アントマン&ワスプ | 118分 | murphysmultiverse.com |
| キャプテン・マーベル | 123分 | murphysmultiverse.com |
| アベンジャーズ／エンドゲーム | 181分 | murphysmultiverse.com |
| スパイダーマン：ファー・フロム・ホーム | 129分 | murphysmultiverse.com |
| ブラック・ウィドウ | 134分 | marvelwatchlist.com |
| シャン・チー／テン・リングスの伝説 | 132分 | marvelwatchlist.com |
| エターナルズ | 156分 | marvelcinematicuniverse.fandom.com |
| スパイダーマン：ノー・ウェイ・ホーム | 148分 | marvelcinematicuniverse.fandom.com |
| ドクター・ストレンジ／マルチバース・オブ・マッドネス | 126分 | marvelwatchlist.com |
| ソー：ラブ＆サンダー | 119分 | marvelwatchlist.com |
| ブラックパンサー／ワカンダ・フォーエバー | 161分 | dexerto.com |
| アントマン&ワスプ：クアントマニア | 125分 | moviescalculator.com |
| ガーディアンズ・オブ・ギャラクシー：VOLUME 3 | 149分 | moviescalculator.com |
| マーベルズ | 105分 | moviescalculator.com |
| デッドプール＆ウルヴァリン | 128分 | IMDb news (ni65207083 / ni65249336) |
| キャプテン・アメリカ：ブレイブ・ニュー・ワールド | 118分 | moviescalculator.com |
| サンダーボルツ* | 126分 | IMDb news |
| ファンタスティック4：ファースト・ステップ | 115分 | themovieblog.com, marvelcinematicuniverse.fandom.com |
| スパイダーマン：ブランド・ニュー・デイ | 145分 | IMDb (tt22084616) |

### 日本公開日
「日本公開日」で個別に検索し、日本語のニュース記事（映画.com、シネマトゥデイ、ソニー・ピクチャーズ公式、マーベル公式、各種プレスリリース）で確認した。

| 作品 | 日本公開日 | 出典 |
|---|---|---|
| インクレディブル・ハルク | 2008/8/1 | eiga.com/movie/53199, 複数のプレスリリース記事で日付を相互確認 |
| アイアンマン | 2008/9/27 | eiga.com/movie/53456, sonypictures.jp/corp/press/2008-05-07 |
| アイアンマン2 | 2010/6/11 | 検索結果の集計（映画.com等） |
| マイティ・ソー | 2011/7/2 | 検索結果の集計 |
| キャプテン・アメリカ／ザ・ファースト・アベンジャー | 2011/10/14 | 検索結果の集計 |
| アベンジャーズ | 2012/8/14 | 検索結果の集計 |
| アイアンマン3 | 2013/4/26 | marvel.disney.co.jp/movie/ironman3 |
| マイティ・ソー／ダーク・ワールド | 2014/2/1 | cinematoday.jp/movie/T0018430 |
| キャプテン・アメリカ／ウィンター・ソルジャー | 2014/4/19 | eiga.com/movie/77787, natalie.mu/eiga/film/161215 |
| ガーディアンズ・オブ・ギャラクシー | 2014/9/13 | natalie.mu/eiga/film/161217 |
| アベンジャーズ／エイジ・オブ・ウルトロン | 2015/7/4 | eiga.com/movie/77790 |
| アントマン | 2015/9/19 | youpouch.com記事, cinematoday.jp/movie/T0016025 |
| シビル・ウォー／キャプテン・アメリカ | 2016/4/29 | cinematoday.jp/movie/T0020636 |
| ドクター・ストレンジ | 2017/1/27 | ja.wikipedia.org（アメリカ公開2016年11月とは異なる） |
| ガーディアンズ・オブ・ギャラクシー：リミックス | 2017/5/12 | hmv.co.jp記事 |
| スパイダーマン：ホームカミング | 2017/8/11 | 検索結果の集計 |
| マイティ・ソー バトルロイヤル | 2017/11/3 | marvel.disney.co.jp/movie/thor-br |
| ブラックパンサー | 2018/3/1 | fansvoice.jp/2017/08/25/black-panther-ja-release-date |
| アベンジャーズ／インフィニティ・ウォー | 2018/4/27 | marvel.disney.co.jp/movie/avengers-iw |
| アントマン&ワスプ | 2018/8/31 | 検索結果の集計 |
| キャプテン・マーベル | 2019/3/15 | cinematoday.jp/news/N0104590 |
| アベンジャーズ／エンドゲーム | 2019/4/24 | marvel.disney.co.jp/movie/avengers-endgame（日米同時公開ではなく日本先行） |
| スパイダーマン：ファー・フロム・ホーム | 2019/6/28 | spice.eplus.jp/articles/236747 |
| ブラック・ウィドウ | 2021/7/9 | eiga.com/movie/92166 |
| シャン・チー／テン・リングスの伝説 | 2021/9/3 | theriver.jp/shang-chi-eternals-jp-release |
| エターナルズ | 2021/11/5 | theriver.jp/shang-chi-eternals-jp-release |
| スパイダーマン：ノー・ウェイ・ホーム | 2022/1/7 | sonypictures.jp/corp/press/2021-11-04（米国公開は2021年12月、日本は年をまたぐ） |
| ドクター・ストレンジ／マルチバース・オブ・マッドネス | 2022/5/4 | game.watch.impress.co.jp/docs/news/1378950 |
| ソー：ラブ＆サンダー | 2022/7/8 | eiga.com/news/20220419/14 |
| ブラックパンサー／ワカンダ・フォーエバー | 2022/11/11 | fansvoice.jp/2022/07/24/bpwf-release |
| アントマン&ワスプ：クアントマニア | 2023/2/17 | screenonline.jp記事（日米同時公開） |
| ガーディアンズ・オブ・ギャラクシー：VOLUME 3 | 2023/5/3 | theriver.jp/gotg3-jp-release（日本が米国より2日先行） |
| マーベルズ | 2023/11/10 | fansvoice.jp/2023/03/15/the-marvels-release（日米同時公開） |
| デッドプール＆ウルヴァリン | 2024/7/24 | av.watch.impress.co.jp/docs/news/1600895（世界最速公開、米国より2日先行） |
| キャプテン・アメリカ：ブレイブ・ニュー・ワールド | 2025/2/14 | av.watch.impress.co.jp/docs/news/1608704（日米同時公開） |
| サンダーボルツ* | 2025/5/2 | marvel.disney.co.jp/news/20240923_01（日米同時公開） |
| ファンタスティック4：ファースト・ステップ | 2025/7/25 | cinematoday.jp/movie/T0030742（日米同時公開） |
| スパイダーマン：ブランド・ニュー・デイ | 2026/7/31 | sonypictures.jp/corp/press/2026-03-18-0（日米同時公開） |

### フェーズ区分
Plex、GamesRadar+等の集計記事より、フェーズ1=6本、フェーズ2=6本、フェーズ3=11本、フェーズ4=7本、フェーズ5=6本、フェーズ6=2本（公開済み分）で合計38本。この本数の内訳は、個別に積み上げた上表の作品数と一致することを確認済み。

### 時系列順（作中の時間軸順）
- フェーズ1〜3（インフィニティ・サーガ）の時系列順は、複数の情報源（Rotten Tomatoes、GamesRadar+、Marvel公式Disney+タイムライン記事）で一致しており、長年ほぼ変わっていない定番の並びである。「キャプテン・アメリカ：ザ・ファースト・アベンジャー」が最も古く、「スパイダーマン：ファー・フロム・ホーム」で一区切りする24作品（フェーズ1〜3の23本＋「ブラック・ウィドウ」）という構成で確認した。
- 「ブラック・ウィドウ」が「シビル・ウォー」直後の時系列に位置するという情報は、複数の集計記事で一致。
- 「ファンタスティック4：ファースト・ステップ」については、Disney+公式のタイムラインが本作を全166タイトル中165番目（＝映画単体としてはほぼ最後）に配置しているという報道を確認した（yahoo.com, comingsoon.net, superherohype.com, thedirect.com）。作中は1960年代の並行世界が舞台だが、マルチバース・サーガ全体における物語上の役割を優先した配置とされている。
- フェーズ4以降（ブラック・ウィドウを除く）の詳細な作中年代については、情報源間で記述が一致しない、または不明瞭な部分があった（例：「アントマン&ワスプ：クアントマニア」の作中設定年について、検索結果に矛盾する記述があった）。そのため、本記事ではフェーズ4以降を「公式に厳密な時系列順は示されていない」「おおむね公開順と一致する」という表現にとどめ、個々の作品に確認できない具体的な年代を割り当てることは避けた。

## 確認できなかった事項

- フェーズ4以降の一部作品（クアントマニア、ブレイブ・ニュー・ワールド、サンダーボルツ等）の正確な作中設定年。検索結果に情報源間の矛盾があり、確定できなかった。本文では「おおむね公開順と一致する」という表現で対応し、断定を避けた。
- 上映時間の「日本公開版」が国際版と異なるかどうか。差異を示す情報は見つからなかったため、同一と仮定した。

## WebFetchが使えなかった点について

本来はWikipedia等の一次情報に近いページを直接開いて裏取りする想定だったが、このセッションの環境ではWebFetchが `en.wikipedia.org` `editorial.rottentomatoes.com` `www.imdb.com` `www.marvel.com` `www.gamesradar.com` `macmyths.com` を含むほぼ全ドメインで `EGRESS_BLOCKED` となり使用できなかった。代わりにWebSearchの検索結果要約とそこに含まれる引用元URLを事実確認の根拠とした。検証セッションでWebFetchが使える場合は、上記の出典URLに直接アクセスして再確認することを推奨する。
