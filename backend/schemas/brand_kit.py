from pydantic import BaseModel, HttpUrl
from typing import List, Dict

class BrandKit(BaseModel):
    safe_zone_px: int
    fonts: Dict[str, str]
    colors: List[str]
    logo_image_url: HttpUrl
