from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI(
    title="Brand Compliance AI",
    description="Validate creative assets against the Neurons brand-kit.",
    version="0.1.0"
)

app.include_router(api_router, prefix="/v1")

@app.get("/health")
def health_check():
    return {"status": "ok"}

