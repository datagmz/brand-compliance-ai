import fitz, re

def extract_brand_info(pdf_bytes: bytes) -> dict:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    info = {"safe_zone_px": None, "primary_colors": [], "fonts": {}}

    for page in doc:
        text = page.get_text("text")
        if "X is" in text:
            m = re.search(r"X is (\d+)px", text)
            if m:
                info["safe_zone_px"] = int(m.group(1))
        hexes = re.findall(r"#([0-9A-Fa-f]{6})", text)
        if hexes:
            info["primary_colors"].extend(f"#{h}" for h in hexes)
        if "Lexend" in text:
            info["fonts"]["primary"] = "Lexend"
        if "Inter" in text:
            info["fonts"]["secondary"] = "Inter"

    info["primary_colors"] = list(dict.fromkeys(info["primary_colors"]))
    return info
