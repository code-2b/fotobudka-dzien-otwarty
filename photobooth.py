st.set_page_config(
    page_title="FotoBudka — Dzień Otwarty",
    page_icon="📸",
    layout="centered"
)

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import qrcode
import base64

st.set_page_config(page_title="FotoBudka — Dzień Otwarty", layout="centered")

st.title("FotoBudka — Dzień Otwarty")
st.write("Zrób zdjęcie, wybierz ramkę i pobierz gotową pamiątkę.")

# 1) Kamera
img_file = st.camera_input("Zrób zdjęcie")

# 2) Ustawienia nakładki (działa nawet bez zdjęcia — uczeń może klikać)
frame_style = st.selectbox("Styl ramki", ["Zielona (Eco)", "Niebieska (Tech)", "Fioletowa (Art)"])
caption = st.text_input("Napis na zdjęciu", "Dołączam do ZS nr4 w Nowym Sączu")
show_qr = st.checkbox("Dodaj QR (np. do strony szkoły)", value=True)
qr_text = st.text_input("Tekst/URL do QR", "https://zsnr4.net")
LOGO_B64 = "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"

def make_frame_color(style: str):
    return {
        "Zielona (Eco)": (30, 160, 90),
        "Niebieska (Tech)": (40, 110, 210),
        "Fioletowa (Art)": (150, 60, 200),
    }[style]

def _get_text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    x0, y0, x1, y1 = draw.textbbox((0, 0), text, font=font)
    return max(0, x1 - x0), max(0, y1 - y0)


def _wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    words = text.strip().split()
    if not words:
        return ["Dzień Otwarty!"]
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        width, _ = _get_text_size(draw, candidate, font)
        if width <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def _ellipsize_to_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> str:
    base = text.strip()
    if not base:
        return "…"
    out = base
    while out:
        width, _ = _get_text_size(draw, out + "…", font)
        if width <= max_width:
            return out + "…"
        out = out[:-1]
    return "…"


def _load_font(size: int) -> ImageFont.ImageFont:
    font_candidates = [
        "data/DejaVuSans_ZS4.ttf",
        "DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for path in font_candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except Exception:
            continue
    return ImageFont.load_default()


@st.cache_resource(show_spinner=False)
def _load_school_logo() -> Image.Image | None:
    if not LOGO_B64 or LOGO_B64.startswith("___WSTAW"):
        return None

    try:
        logo_bytes = base64.b64decode(LOGO_B64.encode("ascii"))
        logo = Image.open(io.BytesIO(logo_bytes)).convert("RGBA")
        return logo
    except Exception:
        return None


def _paste_logo_top_left(photo_rgba: Image.Image, thickness: int):
    logo = _load_school_logo()
    if logo is None:
        return

    w, h = photo_rgba.size
    margin = max(10, thickness + 8)
    target_w = max(120, min(int(w * 0.22), 280))

    lw, lh = logo.size
    if lw <= 0 or lh <= 0:
        return
    target_h = int(target_w * (lh / lw))
    logo = logo.resize((target_w, target_h), Image.Resampling.LANCZOS)

    # Delikatne białe tło pod logo dla czytelności.
    bg_pad = 8
    bg = Image.new("RGBA", (target_w + 2 * bg_pad, target_h + 2 * bg_pad), (255, 255, 255, 120))
    photo_rgba.alpha_composite(bg, (margin - bg_pad, margin - bg_pad))
    photo_rgba.alpha_composite(logo, (margin, margin))


def _draw_caption_and_qr(photo: Image.Image, caption: str, qr_text: str | None):
    w, h = photo.size
    draw = ImageDraw.Draw(photo)

    # Pasek na podpis (większy, aby nie ściskać liter i uniknąć nachodzenia).
    bar_h = max(96, h // 6)
    bar_y0 = h - bar_h
    draw.rectangle([0, bar_y0, w, h], fill=(0, 0, 0))

    # QR
    qr_target = 0
    qr_margin = 12
    if qr_text:
        qr = qrcode.QRCode(border=1, box_size=6)
        qr.add_data(qr_text)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        qr_target = bar_h - 18
        qr_img = qr_img.resize((qr_target, qr_target), Image.Resampling.NEAREST)
        photo.paste(qr_img, (w - qr_target - qr_margin, bar_y0 + 9))

    left_pad = 22
    right_pad = 22 + (qr_target + qr_margin + 8 if qr_target else 0)
    text_area_w = max(120, w - left_pad - right_pad)
    text = caption.strip() if caption.strip() else "Dołączam do ZS nr4 w Nowym Sączu"

    # Dopasowanie czcionki i łamanie do maksymalnie 2 linii.
    font_size = max(22, h // 20)
    min_font_size = 16
    chosen_lines: list[str] = []
    chosen_font: ImageFont.ImageFont = _load_font(font_size)

    while font_size >= min_font_size:
        font = _load_font(font_size)
        lines = _wrap_text(draw, text, font, text_area_w)
        if len(lines) > 2:
            lines = [lines[0], " ".join(lines[1:])]
            lines[1] = _ellipsize_to_width(draw, lines[1], font, text_area_w)

        line_heights = [_get_text_size(draw, ln, font)[1] for ln in lines]
        total_h = sum(line_heights) + (6 if len(lines) > 1 else 0)
        if total_h <= bar_h - 20:
            chosen_lines = lines
            chosen_font = font
            break
        font_size -= 1

    if not chosen_lines:
        chosen_font = _load_font(min_font_size)
        chosen_lines = _wrap_text(draw, text, chosen_font, text_area_w)
        if len(chosen_lines) > 2:
            chosen_lines = [chosen_lines[0], _ellipsize_to_width(draw, " ".join(chosen_lines[1:]), chosen_font, text_area_w)]

    # Pionowe wyśrodkowanie linii w pasku.
    line_heights = [_get_text_size(draw, ln, chosen_font)[1] for ln in chosen_lines]
    total_h = sum(line_heights) + (6 if len(chosen_lines) > 1 else 0)
    y = bar_y0 + (bar_h - total_h) // 2
    for i, line in enumerate(chosen_lines):
        draw.text((left_pad, y), line, fill=(255, 255, 255), font=chosen_font)
        y += line_heights[i] + 6


def add_overlay(photo: Image.Image, style: str, caption: str, qr_text: str | None):
    photo = photo.convert("RGB")
    w, h = photo.size
    draw = ImageDraw.Draw(photo)

    # Ramka
    color = make_frame_color(style)
    thickness = max(10, min(w, h) // 40)
    for i in range(thickness):
        draw.rectangle([i, i, w - 1 - i, h - 1 - i], outline=color)

    # Logo szkoły: lewy górny róg
    photo_rgba = photo.convert("RGBA")
    _paste_logo_top_left(photo_rgba, thickness=thickness)
    photo = photo_rgba.convert("RGB")

    # Pasek podpisu + QR + czytelny napis
    _draw_caption_and_qr(photo, caption=caption, qr_text=qr_text)
    return photo

if img_file is None:
    st.info("Najpierw zrób zdjęcie kamerą powyżej.")
else:
    # 3) Przetwarzanie zdjęcia
    original = Image.open(img_file)
    final = add_overlay(original, frame_style, caption, qr_text if show_qr else None)

    st.subheader("Podgląd")
    st.image(final, use_container_width=True)

    # 4) Pobieranie
    buf = io.BytesIO()
    final.save(buf, format="JPEG", quality=92)
    st.download_button(
        "Pobierz zdjęcie (JPG)",
        data=buf.getvalue(),
        file_name="fotobudka_dzien_otwarty.jpg",
        mime="image/jpeg",
    )

st.caption("Tip: Kamera działa w przeglądarce — na telefonach wychodzi świetnie.")
