import fitz, re, uuid, os
import spacy
from typing import Tuple
from fastapi import UploadFile

nlp = spacy.load("en_core_web_sm")

def extract_text_and_images(pdf_bytes: bytes) -> Tuple[str, list[bytes]]:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text, images = "", []
    for page in doc:
        text += page.get_text("text") + "\n"
        for img in page.get_images(full=True):
            pix = fitz.Pixmap(doc, img[0])
            images.append(pix.tobytes("png"))
    return text, images

def parse_safe_zone(text: str) -> int:
    m = re.search(r"X\s*=\s*(\d+)\s*px", text)
    return int(m.group(1)) if m else 0

def parse_fonts(text: str):
    prim = re.search(r"Primary\s+Font[:\-]\s*([\w ]+)", text)
    sec  = re.search(r"Secondary\s+Font[:\-]\s*([\w ]+)", text)
    p = prim.group(1).strip() if prim else ""
    s = sec.group(1).strip()  if sec  else ""
    if not p or not s:
        ents = [ent.text for ent in nlp(text).ents if ent.label_ in ("PRODUCT","ORG")]
        if ents:
            p = p or ents[0]
            s = s or (ents[1] if len(ents)>1 else ents[0])
    return {"primary": p, "secondary": s}

def parse_colors(text: str):
    hexes = re.findall(r"#(?:[A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})", text)
    return list(dict.fromkeys(hexes))

def save_logo(image_bytes: bytes) -> str:
    os.makedirs("kits", exist_ok=True)
    path = f"kits/{uuid.uuid4()}.png"
    with open(path, "wb") as f:
        f.write(image_bytes)
    return path

async def ingest_brand_kit(file: UploadFile) -> dict:
    data = await file.read()
    text, images = extract_text_and_images(data)
    safe_zone = parse_safe_zone(text)
    fonts     = parse_fonts(text)
    colors    = parse_colors(text)
    logo_path = save_logo(images[0])
    return {
        "safe_zone_px": safe_zone,
        "fonts": fonts,
        "colors": colors,
        "logo_image_url": f"/static/{os.path.basename(logo_path)}"
    }
