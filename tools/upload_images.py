"""原稿の [[IMG:<ファイル名>|代替テキスト]] の画像を WordPress のメディアにアップロードする。

使い方: WPU="$WP_USER" WPP="$WP_APP_PASSWORD" python3 tools/upload_images.py articles/<slug>.md
アップロード済みの対応は articles/img/uploaded.json に残し、同じファイル名・同じ中身なら再アップロードしない。
"""
import hashlib
import json
import os
import re
import subprocess
import sys

MAP = 'articles/img/uploaded.json'
src = open(sys.argv[1]).read()
done = json.load(open(MAP)) if os.path.exists(MAP) else {}
auth = os.environ['WPU'] + ':' + os.environ['WPP']
for name, alt in re.findall(r'\[\[IMG:([^|\]]+)\|([^\]]*)\]\]', src):
    path = 'articles/img/' + name
    h = hashlib.sha1(open(path, 'rb').read()).hexdigest()
    if name in done and done[name]['sha1'] == h:
        print('skip', name)
        continue
    r = subprocess.run(['curl', '-s', '-u', auth, '-X', 'POST',
                        '-H', 'Content-Disposition: attachment; filename="%s"' % name,
                        '-H', 'Content-Type: image/png', '--data-binary', '@' + path,
                        'https://cinemind.jp/wp-json/wp/v2/media'], capture_output=True, text=True)
    m = json.loads(r.stdout)
    if 'id' not in m:
        sys.exit('upload failed: %s %s' % (name, r.stdout[:200]))
    subprocess.run(['curl', '-s', '-u', auth, '-X', 'POST', '-H', 'Content-Type: application/json',
                    '--data', json.dumps({'alt_text': alt}, ensure_ascii=False),
                    'https://cinemind.jp/wp-json/wp/v2/media/%d' % m['id']], capture_output=True)
    done[name] = {'id': m['id'], 'url': m['source_url'], 'sha1': h}
    print('uploaded', name, m['id'])
json.dump(done, open(MAP, 'w'), ensure_ascii=False, indent=1)
