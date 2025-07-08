from pydantic import BaseModel, HttpUrl

class Asset(BaseModel):
    asset_id: str
    width: int
    height: int
    url: HttpUrl
