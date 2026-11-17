# 事実確認 2026-11-17（GSC対策の書き直し 11本）

対象: `git diff articles/` で変わった部分のみ（title・meta・excerpt・追加本文）。元からあった部分は確認済みのため対象外。
記事の md は直接修正済み。【要確認】は11本からすべて消した。

## 点数（事実面）

**9 / 10**（修正後）。修正前は 7 / 10（日本語台詞の未確認2件、題名表記1件、未確認の推測1件、根拠の弱い記述1件）。

配信情報は差分に入っていなかった（grep で確認）。

## ファイルごとの修正

### ironman3.md
- 【要確認】最後のナレーションの日本語の言い回し → 字幕・吹替とも一次情報で確認できなかったので、原語の表記にした。「最後のナレーションは、原語では "I am Iron Man." で終わるので」。
  - 根拠（原語の台詞）: https://cornellsun.com/article/2013/05/iron-man-3-the-perfect-superhero-ending
- 「ペッパーは、トニーが用意した治療でエクストリミスの影響が抜けて、元の体に戻ります」→「トニーの助けで安定します」。英語版Wikipediaのあらすじは "Potts's Extremis effects are stabilized" で、「元の体に戻る」とまでは言えない。meta も同様に「ペッパーの体も治療で安定します」に。
  - 根拠: https://en.wikipedia.org/wiki/Iron_Man_3
- そのほか（スーツの全破壊、破片の手術、リアクターを海へ、エンドクレジット後のバナー、『エイジ・オブ・ウルトロン』冒頭のヒドラ基地襲撃と日本公開7月4日、ハーレーの葬儀出演）は問題なし。
- 注意書き: 冒頭に「その後」の節がラストと『エンドゲーム』に触れると追記されていて、範囲は合っている。title にも（ネタバレあり）、meta 冒頭にも ※ネタバレあり があり問題なし。

### antman2.md
- 【要確認】ローディの台詞 → 日本語字幕は確認できず。原語は Rhodes の "And ever since Hank Pym got snapped out of existence, this is it."（続けてスコットが "We've got enough for one round trip each. That's it. No do-overs."）。「もう作れない」とは言っていないので、「ハンク・ピムが指パッチンで消えてからは手元にあるこれだけだ、という意味のことを言い」＋原語を併記。
  - 根拠: https://clip.cafe/avengers-endgame-2019/rhodes-time-travel-suit-not-bad/ 、https://scrapsfromtheloft.com/movies/avengers-endgame-transcript/
- 節見出し「ピム粒子はなぜ作れない？」→「なぜ足りない？」、meta「ピム粒子が作れない理由」→「エンドゲームでピム粒子が足りない理由」。作中は「作れない」と言い切っていない。
- 「ピム粒子を作れるのはハンクだけ」「クロスはわずかな資料から似たものを作るところまで」→ 根拠が弱いので削除し、「ピム粒子はハンクが開発したもの。『アントマン』でハンクは悪用を恐れて作り方を長年明かしていなかった」だけ残した。
- excerpt: title から（ネタバレあり）が外れたのに、excerpt で結末（3人が塵になる）を出していたので、冒頭に「※ネタバレあり。」を追加。
- 1970年のキャンプ・リーハイでハンクの研究室から粒子を持ち出す件は問題なし。注意書きにピム粒子の場面が追記されていて範囲は合っている。

### guardians2.md
- 【要確認】『ホリデー・スペシャル』の日本語題名 → 『ガーディアンズ・オブ・ギャラクシー ホリデー・スペシャル』（コロンなし・半角スペース）に。正式には頭に「マーベル・スタジオ スペシャル・プレゼンテーション」がつくが、本文では通称で十分と判断。
  - 根拠: https://eiga.com/movie/98331/ 、https://virtualgorillaplus.com/drama/the-guardians-of-the-galaxy-holiday-special-explained/
- 冒頭でクラグリンが話す・回想がアニメで、ルーカーを撮影した映像をもとに描いた（ロトスコープ）件は正しい。
  - 根拠: https://screenrant.com/gotg-holiday-special-brought-yondu-back-rotoscoping-animation/ 、https://slashfilm.com/1117015/the-guardians-of-the-galaxy-holiday-special-pays-tribute-to-the-rotoscope-ghost-of-animations-past
- 【要確認】『VOLUME 3』にヨンドゥが出るか → **出る**。クラグリンがヤカの矢を扱えずにいるところへ、頭の中の幻としてヨンドゥ（マイケル・ルーカー）が短く出てくる。生き返りではない。そのとおりに書き直した。
  - 根拠: https://nerdist.com/article/guardians-of-the-galaxy-vol-3-brings-former-major-character-yondu-michael-rooker-for-brief-cameo/ 、https://www.disneylatino.com/novedades/como-es-la-aparicion-de-yondu-en-guardianes-de-la-galaxia-vol-3
- meta・excerpt でヨンドゥの死を出しているが、記事が答える問いそのもので、title に（ネタバレあり）があるのでこのまま。

### ironman2.md
- 吹き替え: 劇場公開版（DVD・BD収録）佐古真弓、テレビ朝日版 冬馬由美（2012年10月7日『日曜洋画劇場』初回放送）は正しい。修正なし。
  - 根拠: https://ja.wikipedia.org/wiki/アイアンマン2
- 米倉涼子は『アベンジャーズ』が吹き替え初挑戦、も正しい。修正なし。
  - 根拠: https://eiga.com/news/20120524/5/
- title から（ネタバレあり）が外れたが、正体は記事が答える問いそのもので、本文冒頭の注意書きもあるため据え置き。

### captain2.md
- excerpt「バッキーが出る11作品を公開順に」→ 11本目は未公開の『ドゥームズデイ』（2026年12月18日公開予定）なので、「ドラマと公開予定の『ドゥームズデイ』を含めて11作品です」に。

### captain1.md
- 追加の結末の節は、元の「結末（ネタバレあり）」の節を前に移しただけで内容は同じ。冒頭の注意書きが記事全体（中盤と結末）にかかっていて範囲は合っている。
- excerpt: title から（ネタバレあり）が外れたのに結末（北極の氷に沈む）を出していたので、冒頭に「※ネタバレあり。」を追加。

### infinitywar.md
- 追加の1文（『エンドゲーム』で5年後、バナーが指を鳴らして戻る）は正しい。注意書きにもこの1文が『エンドゲーム』に触れると追記されている。修正なし。

### ironman1.md / hulk1.md / ultron.md / civilwar.md
- 修正なし。間の3本（マイティ・ソー、ファースト・アベンジャー、アベンジャーズ）の順番、『3』がニューヨークの戦いから7か月後（ironman3 の既存本文と同じ）、ロス将軍・スターンズの初登場、ウルトロンの由来、ソコヴィア協定の監督主体（国連）は、いずれも既存本文と一致していて問題なし。
- ultron・civilwar は title から（ネタバレあり）が外れたが、meta 冒頭に ※ネタバレあり があり、excerpt は結末を出していないので据え置き。

## 範囲外で気づいたこと

- `articles/page-about.md` に【要確認：実際に参加しているプログラム名】が残っている（今回の対象外なので触っていない）。
