from PIL import Image
import io

def check_compliance(img_bytes: bytes, brand_info: dict):
    image = Image.open(io.BytesIO(img_bytes))
    breakdown = {
        "font_style": True,
        "safe_zone": True,
        "logo_colors": True,
        "palette": True
    }
    return sum(breakdown.values()), breakdown
