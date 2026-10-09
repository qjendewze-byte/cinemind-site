"""articles/<slug>.md を WordPress の下書き（既存ID）に反映する。更新前の内容は docs/backup/<dir>/ に保存。
使い方: python3 tools/update_drafts.py <backup-dir名> <id>:<slug> ...（環境変数 WP_USER / WP_APP_PASSWORD）"""
import sys, os, json, re, subprocess
def req(url, data=None):
    cmd = ["curl", "-s", "-u", f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD']}", url]
    if data:
        cmd += ["-X", "POST", "-H", "Content-Type: application/json", "--data-binary", "@-"]
    return json.loads(subprocess.run(cmd, input=data, capture_output=True, check=True).stdout)
bdir = f"docs/backup/{sys.argv[1]}"; os.makedirs(bdir, exist_ok=True)
tmp = os.environ.get("TMPDIR", "/tmp")
for pair in sys.argv[2:]:
    pid, slug = pair.split(":")
    base = f"https://cinemind.jp/wp-json/wp/v2/posts/{pid}"
    cur = req(base + "?context=edit&_fields=id,status,title,content,excerpt,meta")
    assert cur["status"] == "draft", (pid, cur["status"])
    json.dump(cur, open(f"{bdir}/{slug}.json", "w"), ensure_ascii=False)
    out = f"{tmp}/{slug}.json"
    subprocess.run(["python3", "tools/md2gb.py", f"articles/{slug}.md", out], check=True, capture_output=True)
    d = json.load(open(out)); src = open(f"articles/{slug}.md").read()
    m = re.search(r"^excerpt:\s*(.+)$", src.split("---")[1], re.M)
    if m: d["excerpt"] = m.group(1)
    r = req(base, json.dumps(d).encode())
    print(pid, slug, r["status"], len(r["content"]["raw"]))
