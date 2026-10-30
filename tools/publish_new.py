"""articles/<slug>.md を新規記事として公開する。まず下書きで全部作ってIDを得て、[[CARD:slug]] をIDに置き換えてから公開。
使い方: python3 tools/publish_new.py <slug> ...（環境変数 WP_USER / WP_APP_PASSWORD）"""
import sys, os, json, re, subprocess
API = "https://cinemind.jp/wp-json/wp/v2/posts"
def req(url, data=None):
    cmd = ["curl", "-s", "-u", f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}", url]
    if data is not None:
        cmd += ["-X", "POST", "-H", "Content-Type: application/json", "--data-binary", "@-"]
    return json.loads(subprocess.run(cmd, input=data, capture_output=True, check=True).stdout)
CATS = {"SF": 19, "アクション": 20, "洋画": 27}
tmp = os.environ.get("TMPDIR", "/tmp")
ids, docs = {}, {}
for slug in sys.argv[1:]:
    out = f"{tmp}/{slug}.json"
    subprocess.run(["python3", "tools/md2gb.py", f"articles/{slug}.md", out], check=True, capture_output=True)
    d = json.load(open(out)); fm = open(f"articles/{slug}.md").read().split("---")[1]
    d["excerpt"] = re.search(r"^excerpt:\s*(.+)$", fm, re.M).group(1)
    d["categories"] = [CATS[c.strip()] for c in re.search(r"^categories:\s*(.+)$", fm, re.M).group(1).split(",")]
    d["status"] = "draft"
    r = req(API, json.dumps(d).encode())
    ids[slug] = r["id"]; docs[slug] = d
    print("draft", slug, r["id"])
def card(m):
    k = m.group(1)
    if k.isdigit(): return m.group(0)
    if k not in ids:
        ids[k] = req(f"{API}?slug={k}&_fields=id")[0]["id"]
    return '"postId":"%d"' % ids[k]
for slug in sys.argv[1:]:
    c = re.sub(r'"postId":"([^"]+)"', card, docs[slug]["content"])
    r = req(f"{API}/{ids[slug]}", json.dumps({"content": c, "status": "publish"}).encode())
    print("publish", slug, r["id"], r["status"], r["link"])
