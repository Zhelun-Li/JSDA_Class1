#!/usr/bin/env python3
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OUTPUT = ROOT / "JSDA_mobile.pdf"
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

PAGE_W = 720
PAGE_H = 1280
MARGIN_X = 54
MARGIN_TOP = 54
MARGIN_BOTTOM = 64
BG = (255, 255, 255)
INK = (30, 35, 42)
MUTED = (86, 96, 108)
ACCENT = (33, 88, 145)
CODE_BG = (245, 247, 250)


def font(name, size):
    path = FONT_DIR / name
    return ImageFont.truetype(str(path), size)


FONTS = {
    "h1": font("DejaVuSans-Bold.ttf", 42),
    "h2": font("DejaVuSans-Bold.ttf", 36),
    "h3": font("DejaVuSans-Bold.ttf", 32),
    "h4": font("DejaVuSans-Bold.ttf", 29),
    "body": font("DejaVuSans.ttf", 27),
    "bold": font("DejaVuSans-Bold.ttf", 27),
    "caption": font("DejaVuSans.ttf", 23),
    "code": font("DejaVuSansMono.ttf", 22),
    "table": font("DejaVuSansMono.ttf", 20),
}


class MobilePdf:
    def __init__(self):
        self.pages = []
        self.page = None
        self.draw = None
        self.y = 0
        self.new_page()

    def new_page(self):
        if self.page is not None:
            self.pages.append(self.page)
        self.page = Image.new("RGB", (PAGE_W, PAGE_H), BG)
        self.draw = ImageDraw.Draw(self.page)
        self.y = MARGIN_TOP

    def finish(self):
        if self.page is not None:
            self.pages.append(self.page)
        first, rest = self.pages[0], self.pages[1:]
        first.save(OUTPUT, "PDF", resolution=150.0, save_all=True, append_images=rest)

    def ensure(self, height):
        if self.y + height > PAGE_H - MARGIN_BOTTOM:
            self.new_page()

    def text_height(self, text, fnt):
        box = self.draw.textbbox((0, 0), text or "Ag", font=fnt)
        return box[3] - box[1]

    def text_width(self, text, fnt):
        box = self.draw.textbbox((0, 0), text, font=fnt)
        return box[2] - box[0]

    def clean_inline(self, text):
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        text = text.replace("<br>", " ")
        return text.strip()

    def wrap(self, text, fnt, max_width):
        text = self.clean_inline(text)
        words = text.split()
        if not words:
            return [""]
        lines = []
        current = words[0]
        for word in words[1:]:
            candidate = f"{current} {word}"
            if self.text_width(candidate, fnt) <= max_width:
                current = candidate
            else:
                lines.append(current)
                current = word
        lines.append(current)
        return lines

    def paragraph(self, text, fnt=None, fill=INK, spacing=12, indent=0):
        fnt = fnt or FONTS["body"]
        width = PAGE_W - 2 * MARGIN_X - indent
        lines = self.wrap(text, fnt, width)
        line_h = int(self.text_height("Ag", fnt) * 1.45)
        self.ensure(line_h * len(lines) + spacing)
        for line in lines:
            self.draw.text((MARGIN_X + indent, self.y), line, font=fnt, fill=fill)
            self.y += line_h
        self.y += spacing

    def heading(self, text, level):
        fnt = FONTS.get(f"h{min(level, 4)}", FONTS["h4"])
        gap_before = 22 if self.y > MARGIN_TOP else 0
        lines = self.wrap(text, fnt, PAGE_W - 2 * MARGIN_X)
        line_h = int(self.text_height("Ag", fnt) * 1.28)
        self.ensure(gap_before + line_h * len(lines) + 16)
        self.y += gap_before
        for line in lines:
            self.draw.text((MARGIN_X, self.y), line, font=fnt, fill=ACCENT)
            self.y += line_h
        self.y += 16

    def code(self, text):
        lines = []
        max_width = PAGE_W - 2 * MARGIN_X - 28
        for raw in text.splitlines() or [""]:
            if not raw:
                lines.append("")
                continue
            current = ""
            for ch in raw:
                if self.text_width(current + ch, FONTS["code"]) <= max_width:
                    current += ch
                else:
                    lines.append(current)
                    current = ch
            lines.append(current)
        line_h = int(self.text_height("Ag", FONTS["code"]) * 1.35)
        h = line_h * len(lines) + 28
        self.ensure(h + 12)
        self.draw.rounded_rectangle(
            (MARGIN_X, self.y, PAGE_W - MARGIN_X, self.y + h),
            radius=8,
            fill=CODE_BG,
        )
        self.y += 14
        for line in lines:
            self.draw.text((MARGIN_X + 14, self.y), line, font=FONTS["code"], fill=INK)
            self.y += line_h
        self.y += 26

    def table(self, rows):
        text = "\n".join(rows)
        self.code(text)

    def image(self, path):
        if path.endswith(".svg"):
            img = thermal_diagram(PAGE_W - 2 * MARGIN_X)
        else:
            img = Image.open(ROOT / path).convert("RGB")
            max_w = PAGE_W - 2 * MARGIN_X
            scale = min(max_w / img.width, 1.0)
            img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
        self.ensure(img.height + 22)
        x = (PAGE_W - img.width) // 2
        self.page.paste(img, (x, self.y))
        self.y += img.height + 22


def thermal_diagram(width):
    h = int(width * 0.46)
    img = Image.new("RGB", (width, h), (248, 250, 252))
    d = ImageDraw.Draw(img)
    margin = 18
    mid = width // 2
    d.rectangle((margin, margin, width - margin, h - 48), outline=(110, 127, 145), width=3)
    d.rectangle((margin + 2, margin + 2, mid, h - 50), fill=(240, 247, 255))
    d.rectangle((mid, margin + 2, width - margin - 2, h - 50), fill=(255, 246, 232))
    d.line((mid, margin, mid, h // 2 - 24), fill=INK, width=4)
    d.line((mid, h // 2 + 24, mid, h - 48), fill=INK, width=4)
    d.rounded_rectangle((mid - 8, h // 2 - 24, mid + 8, h // 2 + 24), radius=7, fill=BG, outline=INK, width=2)
    title = FONTS["caption"]
    d.text((width * 0.25, margin + 12), "Room A", font=title, fill=INK, anchor="mm")
    d.text((width * 0.75, margin + 12), "Room B", font=title, fill=INK, anchor="mm")
    positions = [
        (0.18, 0.39, "1", (43, 108, 176)), (0.29, 0.55, "2", (43, 108, 176)),
        (0.40, 0.35, "3", (43, 108, 176)), (0.62, 0.34, "4", (217, 119, 6)),
        (0.74, 0.31, "5", (217, 119, 6)), (0.86, 0.40, "6", (217, 119, 6)),
        (0.67, 0.58, "7", (217, 119, 6)), (0.80, 0.55, "8", (217, 119, 6)),
        (0.90, 0.66, "9", (217, 119, 6)), (0.61, 0.76, "10", (217, 119, 6)),
    ]
    pf = FONTS["caption"]
    for px, py, label, color in positions:
        x, y = int(width * px), int(h * py)
        d.ellipse((x - 18, y - 18, x + 18, y + 18), fill=color, outline=(80, 70, 60), width=2)
        d.text((x, y), label, font=pf, fill=BG, anchor="mm")
    d.text((width // 2, h - 24), "small aperture permits random exchange", font=title, fill=MUTED, anchor="mm")
    return img


def strip_markdown_decoration(line):
    line = re.sub(r"<span[^>]*>", "", line)
    line = re.sub(r"</span>", "", line)
    line = re.sub(r"<strong>|</strong>", "", line)
    return line


def render():
    renderer = MobilePdf()
    lines = README.read_text(encoding="utf-8").splitlines()
    in_code = False
    code_lines = []
    table_rows = []
    paragraph = []

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            renderer.paragraph(" ".join(paragraph))
            paragraph = []

    def flush_table():
        nonlocal table_rows
        if table_rows:
            renderer.table(table_rows)
            table_rows = []

    def flush_code():
        nonlocal code_lines
        if code_lines:
            renderer.code("\n".join(code_lines))
            code_lines = []

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                flush_paragraph()
                flush_table()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            flush_paragraph()
            flush_table()
            continue
        if line.startswith("<!--"):
            continue
        if re.fullmatch(r"<a id=\"[^\"]+\"></a>", line.strip()):
            continue
        match = re.match(r"^(#{1,6})\s+(.*)", line)
        if match:
            flush_paragraph()
            flush_table()
            renderer.heading(renderer.clean_inline(match.group(2)), len(match.group(1)))
            continue
        image_match = re.match(r"!\[[^\]]*\]\(([^)]+)\)", line.strip())
        if image_match:
            flush_paragraph()
            flush_table()
            renderer.image(image_match.group(1))
            continue
        if line.strip().startswith("*Figure "):
            flush_paragraph()
            flush_table()
            caption = line.strip().strip("*")
            renderer.paragraph(caption, fnt=FONTS["caption"], fill=MUTED, spacing=18)
            continue
        if line.lstrip().startswith("- "):
            flush_paragraph()
            flush_table()
            renderer.paragraph("• " + line.lstrip()[2:], indent=10)
            continue
        if line.startswith("|"):
            flush_paragraph()
            table_rows.append(line)
            continue
        if line.startswith("$$") and line.endswith("$$") and len(line) > 4:
            flush_paragraph()
            flush_table()
            renderer.code(line.strip("$"))
            continue
        paragraph.append(strip_markdown_decoration(line))

    flush_paragraph()
    flush_table()
    flush_code()
    renderer.finish()


if __name__ == "__main__":
    render()
    print(OUTPUT)
