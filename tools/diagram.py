"""図の中身（JSON）からPNGを描く。

このMacのPILはx86_64版なので、arch -x86_64 /usr/bin/python3 で実行する。

使い方: arch -x86_64 /usr/bin/python3 tools/diagram.py articles/img/<slug>-<名前>.json articles/img/<slug>-<名前>.png

JSONの形は2種類。

1) 相関図 type=relations（詳しくは relations() の説明）
{
  "type": "relations", "title": "PART2までの相関図",
  "groups": [
    {"name": "アトレイデス家", "color": "#2f6f9f",
     "nodes": [{"id": "paul", "label": "ポール", "sub": "ティモシー・シャラメ", "desc": "主人公", "row": 0}]}
  ],
  "edges": [{"from": "chani", "to": "paul", "label": "恋人", "both": true}]
}
グループは横に並び、各グループの人物は縦に並ぶ（row で段を指定）。線はどの人物どうしでも引ける。
線が箱を横切らないように、row と列の順番で配置を工夫すること。

2) 流れ図 type=flow
{
  "type": "flow", "title": "見る順番",
  "steps": [{"label": "DUNE/デューン 砂の惑星", "sub": "2021年・155分", "note": "まずこれ"}],
  "side": [{"label": "デューン/砂の惑星（1984）", "sub": "別の作品。観なくていい"}]
}
steps は上から下へ矢印でつながる。side は右側に点線の枠で並ぶ（本筋ではないもの）。
"""
import json
import math
import sys

from PIL import Image, ImageDraw, ImageFont

FONT_R = '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'
FONT_B = '/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc'
INK = (40, 40, 40)
SUB = (110, 110, 110)
LINE = (150, 150, 150)
S = 2  # 高解像度で描いて縮小する倍率


def font(path, size):
    return ImageFont.truetype(path, size * S)


def hex2rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def tint(rgb, k):
    return tuple(int(c + (255 - c) * k) for c in rgb)


def text_w(d, t, f):
    return d.textbbox((0, 0), t, font=f)[2]


def arrow(d, x1, y1, x2, y2, color, dashed=False, width=2):
    w = width * S
    if dashed:
        n = max(1, int(math.hypot(x2 - x1, y2 - y1) / (10 * S)))
        for i in range(0, n, 2):
            a, b = i / n, min(1, (i + 1) / n)
            d.line((x1 + (x2 - x1) * a, y1 + (y2 - y1) * a, x1 + (x2 - x1) * b, y1 + (y2 - y1) * b), fill=color, width=w)
    else:
        d.line((x1, y1, x2, y2), fill=color, width=w)
    ang = math.atan2(y2 - y1, x2 - x1)
    L = 10 * S
    for s in (0.45, -0.45):
        d.line((x2, y2, x2 - L * math.cos(ang + s), y2 - L * math.sin(ang + s)), fill=color, width=w)


def draw_title(d, W, title, y, size=22):
    f = font(FONT_B, size)
    d.text(((W - text_w(d, title, f)) / 2, y), title, font=f, fill=INK)


def clip(box, tx, ty):
    """箱の中心から (tx,ty) へ向かう線が、箱の縁と交わる点"""
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    hw, hh = (box[2] - box[0]) / 2, (box[3] - box[1]) / 2
    k = min(hw / abs(dx) if dx else 1e9, hh / abs(dy) if dy else 1e9)
    return cx + dx * k, cy + dy * k


def relations(spec):
    """groups は列。group に "col"（列）と "row"（開始行）を書くと格子配置になる。人物はその行から下へ1行ずつ並ぶ（人物の row は無視）。
    各人物は row（0始まり、省略時は順番）で縦位置を指定できる。
    人物に desc を書くと、俳優名（sub）の下にもう1行出る。
    edges はどの人物どうしでも引ける（直線。ラベルは白地で線の中ほどに置く）。
    edge に "at": 0.3 などを付けると、ラベルの位置を線の始点寄り(0)〜終点寄り(1)に動かせる。"""
    groups = spec['groups']
    colw = spec.get('col_width', 250) * S
    boxw = spec.get('box_width', 200) * S
    rowh = spec.get('row_height', 112) * S
    top = 70 * S
    head = (spec.get('font', {}).get('head', 15) + 31) * S
    has_desc = any(n.get('desc') for g in groups for n in g['nodes'])
    fz = spec.get('font', {})
    zn, zs, zh, zl = fz.get('name', 15), fz.get('sub', 12), fz.get('head', 15), fz.get('label', 12)
    boxh = int((zn + 12 + zs + 10 + (zs + 10 if has_desc else 0) + 6) * S)
    fb, fs, fh, fl = font(FONT_B, zn), font(FONT_R, zs), font(FONT_B, zh), font(FONT_R, zl)
    hh = (zh + 16) * S  # 見出しの帯の高さ
    pos, colors, headers = {}, {}, []
    stacked = any('col' in g for g in groups)
    if stacked:
        # 格子配置: 勢力ごとに col（列）と row（開始行）を指定。人物はその行から下へ並ぶ
        ncols = max(g.get('col', 0) for g in groups) + 1
        cell = head + boxh + 22 * S
        last = 0
        for g in groups:
            ci, r0 = g.get('col', 0), g.get('row', 0)
            c = hex2rgb(g.get('color', '#666666'))
            cx = 20 * S + ci * colw + colw / 2
            headers.append((cx, top + r0 * cell, g['name'], c))
            for k, n in enumerate(g['nodes']):
                y = top + (r0 + k) * cell + head
                pos[n['id']] = (cx - boxw / 2, y, cx + boxw / 2, y + boxh)
                colors[n['id']] = c
                last = max(last, r0 + k)
        W = colw * ncols + 40 * S
        H = top + (last + 1) * cell + 10 * S
    else:
        rows = 0
        for g in groups:
            for i, n in enumerate(g['nodes']):
                n.setdefault('row', i)
                rows = max(rows, n['row'] + 1)
        W = colw * len(groups) + 40 * S
        H = top + head + rows * rowh + 20 * S
        for gi, g in enumerate(groups):
            c = hex2rgb(g.get('color', '#666666'))
            cx = 20 * S + gi * colw + colw / 2
            headers.append((cx, top, g['name'], c))
            for n in g['nodes']:
                y = top + head + n['row'] * rowh
                pos[n['id']] = (cx - boxw / 2, y, cx + boxw / 2, y + boxh)
                colors[n['id']] = c
    img = Image.new('RGB', (int(W), int(H)), 'white')
    d = ImageDraw.Draw(img)
    draw_title(d, W, spec.get('title', ''), 20 * S)
    # 線を先に描き、箱とラベルを上に重ねる
    labels = []
    for e in spec.get('edges', []):
        a, b = pos[e['from']], pos[e['to']]
        ac = ((a[0] + a[2]) / 2, (a[1] + a[3]) / 2)
        bc = ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)
        x1, y1 = clip(a, *bc)
        x2, y2 = clip(b, *ac)
        arrow(d, x1, y1, x2, y2, LINE, dashed=e.get('dashed', False))
        if e.get('both'):
            arrow(d, x2, y2, x1, y1, LINE, dashed=e.get('dashed', False))
        if e.get('label'):
            t = e['label']
            k = e.get('at', 0.5)
            labels.append((x1 + (x2 - x1) * k, y1 + (y2 - y1) * k, t))
    for nid, box in pos.items():
        n = next(n for g in groups for n in g['nodes'] if n['id'] == nid)
        c = colors[nid]
        cx = (box[0] + box[2]) / 2
        d.rounded_rectangle(box, 8 * S, fill=tint(c, 0.88), outline=c, width=2 * S)
        y0 = box[1] + 8 * S
        d.text((cx - text_w(d, n['label'], fb) / 2, y0), n['label'], font=fb, fill=INK)
        y0 += (zn + 10) * S
        if n.get('sub'):
            d.text((cx - text_w(d, n['sub'], fs) / 2, y0), n['sub'], font=fs, fill=SUB)
            y0 += (zs + 8) * S
        if n.get('desc'):
            d.text((cx - text_w(d, n['desc'], fs) / 2, y0), n['desc'], font=fs, fill=c)
    for cx, y, name, c in headers:
        if not name:  # 見出しなしの枠
            continue
        d.rounded_rectangle((cx - boxw / 2, y, cx + boxw / 2, y + hh), 8 * S, fill=c)
        d.text((cx - text_w(d, name, fh) / 2, y + 7 * S), name, font=fh, fill='white')
    for mx, my, t in labels:
        tw = text_w(d, t, fl)
        lh = (zl + 8) * S
        d.rounded_rectangle((mx - tw / 2 - 6 * S, my - lh / 2, mx + tw / 2 + 6 * S, my + lh / 2), 4 * S,
                            fill='white', outline=(215, 215, 215), width=1 * S)
        d.text((mx - tw / 2, my - lh / 2 + 3 * S), t, font=fl, fill=INK)
    return img


def flow(spec):
    """縦の流れ図。spec の font（name/sub/note）と box_width で文字と幅を変えられる。"""
    steps, side = spec['steps'], spec.get('side', [])
    fz = spec.get('font', {})
    zn, zs = fz.get('name', 15), fz.get('sub', 12)
    boxw = spec.get('box_width', 320) * S
    boxh = int((zn + 12 + zs + 18) * S)
    gap = 34 * S
    top = 70 * S
    W = (boxw + 60 * S) + ((280 * S + 40 * S) if side else 0)
    H = top + max(len(steps), len(side)) * (boxh + gap) + 30 * S
    img = Image.new('RGB', (int(W), int(H)), 'white')
    d = ImageDraw.Draw(img)
    draw_title(d, W, spec.get('title', ''), 20 * S)
    fb, fs = font(FONT_B, zn), font(FONT_R, zs)
    c = hex2rgb(spec.get('color', '#2f6f9f'))
    x0 = 30 * S
    for i, st in enumerate(steps):
        y = top + i * (boxh + gap)
        d.rounded_rectangle((x0, y, x0 + boxw, y + boxh), 8 * S, fill=tint(c, 0.88), outline=c, width=2 * S)
        d.text((x0 + 16 * S, y + 10 * S), st['label'], font=fb, fill=INK)
        if st.get('sub'):
            d.text((x0 + 16 * S, y + (zn + 20) * S), st['sub'], font=fs, fill=SUB)
        if st.get('note'):
            tw = text_w(d, st['note'], fs)
            d.text((x0 + boxw - tw - 12 * S, y + (zn + 20) * S), st['note'], font=fs, fill=c)
        if i < len(steps) - 1:
            arrow(d, x0 + boxw / 2, y + boxh, x0 + boxw / 2, y + boxh + gap - 2 * S, c)
    sx = x0 + boxw + 40 * S
    for i, st in enumerate(side):
        y = top + i * (boxh + gap)
        bw = 280 * S
        for k in range(0, int(bw), 12 * S):  # 点線の枠
            d.line((sx + k, y, sx + min(k + 6 * S, bw), y), fill=LINE, width=2 * S)
            d.line((sx + k, y + boxh, sx + min(k + 6 * S, bw), y + boxh), fill=LINE, width=2 * S)
        d.line((sx, y, sx, y + boxh), fill=LINE, width=2 * S)
        d.line((sx + bw, y, sx + bw, y + boxh), fill=LINE, width=2 * S)
        d.text((sx + 14 * S, y + 10 * S), st['label'], font=fb, fill=SUB)
        if st.get('sub'):
            d.text((sx + 14 * S, y + (zn + 20) * S), st['sub'], font=fs, fill=SUB)
    return img


spec = json.load(open(sys.argv[1]))
img = {'relations': relations, 'flow': flow}[spec['type']](spec)
# 高解像度のまま保存する（記事ではタップで拡大できるようにする）
img.save(sys.argv[2], optimize=True)
print(sys.argv[2], img.size)
