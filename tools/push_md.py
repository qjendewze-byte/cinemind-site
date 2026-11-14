"""articles/<slug>.md の内容で既存記事（下書き・公開済みとも）を更新する。更新前は docs/backup/<dir>/ に保存。
[[CARD:slug]] は slug から記事IDに置き換える。--publish を付けると公開状態にする。
使い方: python3 tools/push_md.py <backup-dir名> [--publish] <id>:<slug> ...（環境変数 WP_USER / WP_APP_PASSWORD）"""
import sys, os, json, re, subprocess
API = "https://cinemind.jp/wp-json/wp/v2/posts"
def req(url, data=None):
    cmd = ["curl", "-s", "-u", f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}", url]
    if data is not None:
        cmd += ["-X", "POST", "-H", "Content-Type: application/json", "--data-binary", "@-"]
    return json.loads(subprocess.run(cmd, input=data, capture_output=True, check=True).stdout)
args = sys.argv[1:]; bdir = f"docs/backup/{args.pop(0)}"; os.makedirs(bdir, exist_ok=True)
publish = "--publish" in args; args = [a for a in args if a != "--publish"]
tmp = os.environ.get("TMPDIR", "/tmp"); ids = {}
def card(m):
    k = m.group(1)
    if k.isdigit(): return m.group(0)
    if k not in ids:
        r = req(f"{API}?slug={k}&_fields=id,status")
        assert r and r[0]["status"] == "publish", ("未公開のカード", k)
        ids[k] = r[0]["id"]
    return '"postId":"%d"' % ids[k]
for pair in args:
    pid, slug = pair.split(":")
    cur = req(f"{API}/{pid}?context=edit&_fields=id,status,slug,title,content,excerpt,meta")
    assert cur["slug"] == slug, (pid, cur["slug"])
    json.dump(cur, open(f"{bdir}/{slug}.json", "w"), ensure_ascii=False)
    out = f"{tmp}/{slug}.json"
    subprocess.run(["python3", "tools/md2gb.py", f"articles/{slug}.md", out], check=True, capture_output=True)
    d = json.load(open(out)); fm = open(f"articles/{slug}.md").read().split("---")[1]
    m = re.search(r"^excerpt:\s*(.+)$", fm, re.M)
    if m: d["excerpt"] = m.group(1)
    d["content"] = re.sub(r'"postId":"([^"]+)"', card, d["content"])
    d["status"] = "publish" if publish else cur["status"]
    r = req(f"{API}/{pid}", json.dumps(d).encode())
    print(pid, slug, r["status"], len(r["content"]["raw"]))
