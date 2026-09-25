#!/usr/bin/env python3
"""Generate a 1200x630 link-preview (Open Graph) card.

Example:
    python3 scripts/og-image.py --title "Brevyx" \
        --line "Break & eye-rest reminders" --line "for Linux (Ubuntu)" \
        --tags "Rust · GTK4 · 20-20-20 rule" \
        --art ../projects/blink-eye/assets/icons/brevyx-512.png \
        --out static/brevyx-og.png

Use "\\n" in --title to split a long title over two lines.
Requires Pillow (python3 -m pip install pillow).
"""
import argparse

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1200, 630
FONT = "/usr/share/fonts/truetype/ubuntu/Ubuntu[wdth,wght].ttf"


def font(size, weight):
    try:
        f = ImageFont.truetype(FONT, size)
    except OSError:
        return ImageFont.load_default(size)
    try:
        f.set_variation_by_axes([100, weight])
    except Exception:
        pass
    return f


def hex_rgb(value):
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def load_art(path, shape):
    art = Image.open(path).convert("RGBA")
    art.thumbnail((440, 500), Image.LANCZOS)
    if shape == "none":
        return art
    mask = Image.new("L", art.size, 0)
    draw = ImageDraw.Draw(mask)
    if shape == "circle":
        side = min(art.size)
        art = art.crop(((art.width - side) // 2, (art.height - side) // 2,
                        (art.width + side) // 2, (art.height + side) // 2))
        mask = Image.new("L", art.size, 0)
        ImageDraw.Draw(mask).ellipse([0, 0, *art.size], fill=255)
    else:  # rounded
        draw.rounded_rectangle([0, 0, *art.size], 24, fill=255)
    art.putalpha(mask)
    return art


def card(out, art, title, lines, tags, top, bottom, site):
    bg = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(bg)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    bg = bg.convert("RGBA")

    if art is not None:
        ax, ay = W - art.width - 70, (H - art.height) // 2
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(glow).ellipse([ax - 20, ay - 20, ax + art.width + 20, ay + art.height + 20],
                                     fill=(120, 140, 255, 70))
        bg = Image.alpha_composite(bg, glow.filter(ImageFilter.GaussianBlur(60)))
        bg.alpha_composite(art, (ax, ay))

    d = ImageDraw.Draw(bg)
    x = 80
    two_lines = "\n" in title
    tf = font(80 if two_lines else 92, 700)
    ty = 90 if two_lines else 150
    d.multiline_text((x, ty), title, font=tf, fill="white", spacing=4)
    y = d.multiline_textbbox((x, ty), title, font=tf, spacing=4)[3] + 45
    for ln in lines:
        d.text((x, y), ln, font=font(38, 400), fill=(215, 222, 240))
        y += 52
    if tags:
        d.text((x, y + 30), tags, font=font(28, 500), fill=(150, 170, 230))
    d.text((x, H - 80), site, font=font(28, 500), fill=(170, 180, 205))
    bg.convert("RGB").save(out, optimize=True)


def main():
    p = argparse.ArgumentParser(description="Generate a 1200x630 Open Graph card.")
    p.add_argument("--title", required=True)
    p.add_argument("--line", action="append", default=[], help="Tagline line (repeat for more)")
    p.add_argument("--tags", default="")
    p.add_argument("--art", help="Icon or screenshot shown on the right")
    p.add_argument("--shape", choices=["none", "rounded", "circle"], default="none",
                   help="none for transparent icons, rounded for screenshots, circle for photos")
    p.add_argument("--top", default="#0e1430", help="Gradient top colour")
    p.add_argument("--bottom", default="#28184e", help="Gradient bottom colour")
    p.add_argument("--site", default="sheheem.in")
    p.add_argument("--out", required=True)
    a = p.parse_args()

    art = load_art(a.art, a.shape) if a.art else None
    card(a.out, art, a.title.replace("\\n", "\n"), a.line, a.tags,
         hex_rgb(a.top), hex_rgb(a.bottom), a.site)
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
