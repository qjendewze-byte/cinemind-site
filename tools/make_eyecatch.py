"""文字だけのアイキャッチ画像（1536x1024 PNG）を作る。既存のアイキャッチ（クリーム地・太い黒文字）に色を合わせている。
使い方: python3 tools/make_eyecatch.py <出力先dir> <slug>|<作品名>|<問い> ...（作品名・問いの中の / で改行）"""
import sys, os
from PIL import Image, ImageDraw, ImageFont
F = "/System/Library/Fonts/ヒラギノ角ゴシック W%d.ttc"
W, H, M = 1536, 1024, 110
BG, INK, SUB, ACC = (246, 234, 204), (34, 30, 28), (70, 64, 58), (196, 72, 52)
def fit(draw, lines, w, size, weight):
    while size > 30:
        f = ImageFont.truetype(F % weight, size)
        if max(draw.textlength(l, font=f) for l in lines) <= w: return f, size
        size -= 4
    return f, size
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for spec in sys.argv[2:]:
    slug, work, q = spec.split("|")
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.rectangle([M, 150, M + 120, 162], fill=ACC)
    wl, ql = work.split("/"), q.split("/")
    fw, sw = fit(d, wl, W - 2 * M, 132, 8)
    fq, sq = fit(d, ql, W - 2 * M, 76, 6)
    y = 230
    for l in wl:
        d.text((M, y), l, font=fw, fill=INK); y += int(sw * 1.3)
    y += 40
    for l in ql:
        d.text((M, y), l, font=fq, fill=SUB); y += int(sq * 1.45)
    d.text((M, H - 190), "CINEMIND", font=ImageFont.truetype(F % 6, 34), fill=SUB)
    im.save(f"{out}/{slug}.png", optimize=True)
    print(slug)
