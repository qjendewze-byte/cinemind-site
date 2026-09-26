import re, sys, json, html

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    return t

src = open(sys.argv[1]).read()
body = src.split('---', 2)[2].lstrip('\n')
lines = body.split('\n')
out, i = [], 0
# 先頭のH1は記事タイトルなので本文から除く
while i < len(lines):
    ln = lines[i]
    if ln.startswith('# '):
        i += 1; continue
    if ln.strip().startswith('[[CARD:'):
        pid = ln.strip()[7:-2]
        out.append('<!-- wp:loos/post-link {"postId":"%s"} /-->' % pid)
        i += 1; continue
    if ln.startswith('### '):
        out.append('<!-- wp:heading {"level":3} -->\n<h3 class="wp-block-heading">%s</h3>\n<!-- /wp:heading -->' % inline(ln[4:]))
        i += 1; continue
    if ln.startswith('## '):
        out.append('<!-- wp:heading -->\n<h2 class="wp-block-heading">%s</h2>\n<!-- /wp:heading -->' % inline(ln[3:]))
        i += 1; continue
    if ln.startswith('|'):
        tbl = []
        while i < len(lines) and lines[i].startswith('|'):
            tbl.append(lines[i]); i += 1
        cells = [[c.strip() for c in r.strip('|').split('|')] for r in tbl]
        head, rows = cells[0], cells[2:]
        h = ''.join('<th>%s</th>' % inline(c) for c in head)
        b = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % inline(c) for c in r) for r in rows)
        out.append('<!-- wp:table -->\n<figure class="wp-block-table"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></figure>\n<!-- /wp:table -->' % (h, b))
        continue
    if ln.startswith('- '):
        items = []
        while i < len(lines) and lines[i].startswith('- '):
            items.append(lines[i][2:]); i += 1
        li = ''.join('<!-- wp:list-item -->\n<li>%s</li>\n<!-- /wp:list-item -->\n' % inline(x) for x in items)
        out.append('<!-- wp:list -->\n<ul class="wp-block-list">%s</ul>\n<!-- /wp:list -->' % li)
        continue
    if ln.strip():
        out.append('<!-- wp:paragraph -->\n<p>%s</p>\n<!-- /wp:paragraph -->' % inline(ln.strip()))
    i += 1

content = '\n\n'.join(out)
meta = dict(re.findall(r'^(title|slug|meta_description):\s*(.+)$', src.split('---')[1], re.M))
json.dump({"content": content, "title": meta["title"], "slug": meta["slug"],
           "status": "draft", "meta": {"ssp_meta_description": meta["meta_description"]}},
          open(sys.argv[2], "w"), ensure_ascii=False)
print("ブロック数:", len(out))
print("本文:", len(content), "文字")
print("タイトル:", meta["title"])
