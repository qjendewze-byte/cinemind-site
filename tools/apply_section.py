"""docs/published-seo/<ID>-<slug>.md の節を、公開済み記事に差し込むためのJSONを作る。

使い方: python3 tools/apply_section.py docs/published-seo/94-passengers.md current.json out.json
  current.json … REST API (context=edit) で取った現在の記事
  out.json     … POST /wp/v2/posts/<ID> に送る本文
"""
import html
import json
import re
import sys


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    return t


def to_blocks(md):
    lines, out, i = md.strip().split('\n'), [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith('### '):
            out.append('<!-- wp:heading {"level":3} -->\n<h3 class="wp-block-heading">%s</h3>\n<!-- /wp:heading -->' % inline(ln[4:]))
            i += 1
            continue
        if ln.startswith('|'):
            tbl = []
            while i < len(lines) and lines[i].startswith('|'):
                tbl.append(lines[i])
                i += 1
            cells = [[c.strip() for c in r.strip('|').split('|')] for r in tbl]
            h = ''.join('<th>%s</th>' % inline(c) for c in cells[0])
            b = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % inline(c) for c in r) for r in cells[2:])
            out.append('<!-- wp:table -->\n<figure class="wp-block-table"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></figure>\n<!-- /wp:table -->' % (h, b))
            continue
        if ln.startswith('- '):
            items = []
            while i < len(lines) and lines[i].startswith('- '):
                items.append(lines[i][2:])
                i += 1
            li = ''.join('<!-- wp:list-item -->\n<li>%s</li>\n<!-- /wp:list-item -->\n' % inline(x) for x in items)
            out.append('<!-- wp:list -->\n<ul class="wp-block-list">%s</ul>\n<!-- /wp:list -->' % li)
            continue
        if ln.strip():
            out.append('<!-- wp:paragraph -->\n<p>%s</p>\n<!-- /wp:paragraph -->' % inline(ln.strip()))
        i += 1
    return '\n\n'.join(out)


src = open(sys.argv[1]).read()
head, body = src.split('\n---\n', 1)
meta = dict(re.findall(r'^(\w+):\s*(.+)$', head, re.M))
cur = json.load(open(sys.argv[2]))
raw = cur['content']['raw']

# 記事の節の見出しレベル（h2がなければh3）に合わせる
lv = 2 if re.search(r'<h2[\s>]', raw) else 3
attr = '' if lv == 2 else ' {"level":3}'
section = '<!-- wp:heading%s -->\n<h%d class="wp-block-heading">%s</h%d>\n<!-- /wp:heading -->\n\n%s\n\n' % (
    attr, lv, inline(meta['section_heading']), lv, to_blocks(body).replace('"level":3', '"level":%d' % (lv + 1)).replace('<h3', '<h%d' % (lv + 1)).replace('</h3>', '</h%d>' % (lv + 1)))

# insert_after の見出しの節の終わり（＝次の同レベル見出しブロックの直前）に差し込む
target = meta['insert_after'].strip()
heads = [m for m in re.finditer(r'<!-- wp:heading[^>]*-->\s*<h%d[^>]*>(.*?)</h%d>' % (lv, lv), raw, re.S)]
idx = next(k for k, m in enumerate(heads) if target in re.sub('<[^>]+>', '', m.group(1)))
pos = heads[idx + 1].start() if idx + 1 < len(heads) else len(raw)
new = raw[:pos] + section + raw[pos:]

json.dump({
    'title': meta['title'].strip(),
    'excerpt': meta['excerpt'].strip(),
    'content': new,
    'meta': {'ssp_meta_description': meta['meta_description'].strip()},
}, open(sys.argv[3], 'w'), ensure_ascii=False)
print('inserted after:', re.sub('<[^>]+>', '', heads[idx].group(1)), '| before:',
      re.sub('<[^>]+>', '', heads[idx + 1].group(1)) if idx + 1 < len(heads) else '(end)')
