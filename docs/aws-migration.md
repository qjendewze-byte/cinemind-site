# cinemind.jp を AWS（Lightsail）へ移す手順書

作成: 2026-10-15（統括）。メールは使っていない（運営者確認済み）。

## 今の構成（2026-10-15 時点）

| 項目 | 内容 |
|---|---|
| サーバー | エックスサーバー sv16676（nginx）、IP 85.131.213.57 |
| DNS | エックスサーバーのネームサーバー（ns1〜ns5.xserver.jp） |
| WordPress | テーマ SWELL 2.19.0、投稿40・固定ページ4 |
| 有効なプラグイン | Jetpack、SEO SIMPLE PACK、Contact Form 7、Code Snippets、pochipp、Useful Blocks、WP Multibyte Patch、WP Revisions Control、XML Sitemap Feed、CloudSecure WP Security、AI Provider for Anthropic、CoWriter |
| メール | 使っていない（MX はあるが不要） |

## 移した後の構成

| 項目 | 内容 | 費用の目安 |
|---|---|---|
| サーバー | Lightsail 東京リージョン、WordPress（Bitnami）、2GB メモリのプラン | 月 $12 |
| 固定IP | Lightsail の静的IP（インスタンスにつないでいる間は無料） | 0 |
| DNS | Lightsail の DNS ゾーン | 0 |
| SSL | Let's Encrypt（Bitnami の bncert-tool、自動更新） | 0 |
| バックアップ | Lightsail の自動スナップショット（毎日、7世代） | 月 $1 前後 |

1GB のプラン（月 $7）でも動くが、Jetpack や SWELL の管理画面で重くなりやすいので 2GB にする。

## 手順

**誰がやるか**: 「私」＝統括（Claude）、「運営者」＝あなた

1. **AWS にログインする**（運営者）: どの AWS アカウントを使うか決め、ターミナルで `aws login` を実行する
2. **サーバーを作る**（私）: Lightsail の WordPress インスタンス、静的IP、DNS ゾーンを作る。DNS ゾーンには今のレコード（A、www）を写す
3. **移行用プラグインを入れる**（私）: 今のサイトと新しいサーバーの両方に All-in-One WP Migration を入れる
4. **書き出す**（運営者）: 今のサイトの管理画面で「エクスポート → ファイル」を押し、.wpress ファイルを保存する
5. **新しいサーバーに置く**（私）: 新しいサーバーのバックアップ置き場に .wpress ファイルを置く
6. **復元する**（運営者）: 新しいサーバーの管理画面で「バックアップ → 復元」を押す
7. **確かめる**（私）: hosts ファイルで新しいサーバーを見て、全ページ、画像、SWELL のブロック、REST API（記事の入稿）を確かめる
8. **SWELL を確かめる**（運営者）: SWELL のユーザー認証が外れていれば、もう一度認証する
9. **ネームサーバーを切り替える**（運営者）: ドメインの管理画面で、ネームサーバーを Lightsail の4つに変える。値は私が渡す
10. **SSL を入れる**（私）: DNS が切り替わったら Let's Encrypt を入れ、http から https へ転送する
11. **後片付け**（私）: エックスサーバー専用のプラグイン（CloudSecure、TypeSquare）を外し、Bitnami のバナーを消す
12. **様子を見る**（両方）: 1〜2週間はエックスサーバーを解約しない。問題がなければ運営者が解約する（ドメインの契約は残す）

止まる時間: ネームサーバーが切り替わるまでの間（数時間〜1日）は、新旧どちらかのサーバーに表示される。中身は同じなので見え方は変わらない。この間は記事を更新しない。

## 気をつけること

- **お問い合わせフォーム（Contact Form 7）の通知メール**: Lightsail からはそのままではメールが送れない。通知が必要なら、あとで Amazon SES につなぐ
- **アプリケーションパスワード**: データベースごと移るので、そのまま使える（WP_USER / WP_APP_PASSWORD は変えない）
- **Search Console と Jetpack**: ドメインが同じなので、設定し直す必要はない。Jetpack は切り替え後に接続を確認する
- **戻し方**: うまくいかなければ、ネームサーバーをエックスサーバーに戻す。エックスサーバーはまだ解約していないので、すぐ戻る

## 進み具合（2026-10-16）

- AWS アカウント: cinemind（454805670657、Organizations の配下）。CLI は `--profile cinemind`（SSO、デバイスコードでログイン: `aws sso login --profile cinemind --use-device-code --no-browser`）
- サーバー: Lightsail `cinemind-wp`（ap-northeast-1a、blueprint wordpress_ls_1_0＝WordPress 7.1、Debian 12、PHP 8.2、Apache、small_3_0 月$12、自動スナップショット毎日 18:00 UTC）
- 固定IP: `cinemind-ip` 35.74.53.76。SSH(22) は作業する場所のIPとブラウザ接続だけに開けている
- SSH: `aws lightsail get-instance-access-details --instance-name cinemind-wp --protocol ssh` で一時鍵を取り、ユーザー admin で入る
- 移行のやり方: All-in-One WP Migration（運営者の操作が要る）はやめ、Code Snippets に一時的な REST の書き出し機能を足して、DB（SQL）と wp-content（zip）を取り出した。取り出した後、機能とファイルは旧サーバーから削除済み
  - 注意: `$wpdb->_real_escape()` は `%` を `{64桁の16進}` に置き換えるので、取り込む前に `%` に戻した（戻さないとパーマリンクなどが壊れる）
- 新サーバーで変えた設定: `/etc/apache2/conf-available/wordpress-htaccess.conf`（AllowOverride All）、`/var/www/html/.htaccess`（WordPress の書き換えと Authorization の受け渡し）、`/var/www/wp-config.php` の WP_HOME / WP_SITEURL を https://cinemind.jp に固定（元は wp-config.php.orig）
- 確認: 公開中の26ページ、トップ、カテゴリ、サイトマップ、フィード、robots.txt、REST（アプリケーションパスワード）が旧サーバーと同じ
- DNS ゾーン: Lightsail（cinemind.jp と www の A → 35.74.53.76）。ネームサーバー: ns-1056.awsdns-04.org / ns-811.awsdns-37.net / ns-1713.awsdns-22.co.uk / ns-401.awsdns-50.com
- ドメインの有効期限は **2026-10-31**（JPRS の whois）。更新を忘れないこと
- 残り: ネームサーバー切り替え（運営者）→ Let's Encrypt（cinemind.jp と www）→ エックスサーバー専用プラグインの整理 → 1〜2週間後に旧サーバー解約
