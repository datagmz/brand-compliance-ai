import uuid
import os
from PIL import Image
from fastapi import UploadFile

ASSET_DIR = "assets"

def save_and_normalize_image(file: UploadFile) -> dict:
    # Ensure directory exists
    os.makedirs(ASSET_DIR, exist_ok=True)
    # Generate a unique ID + preserve extension
    asset_id = str(uuid.uuid4())
    ext = file.filename.rsplit(".", 1)[-1].lower()
    dest = os.path.join(ASSET_DIR, f"{asset_id}.{ext}")

    # Open with Pillow
    img = Image.open(file.file)
    # Resize if larger than 1200px in either dimension
    img.thumbnail((1200, 1200))
    # Save to disk
    img.save(dest)

    width, height = img.size
    return {
        "asset_id": asset_id,
        "width": width,
        "height": height,
        "url": f"/assets/{asset_id}.{ext}"
    }
