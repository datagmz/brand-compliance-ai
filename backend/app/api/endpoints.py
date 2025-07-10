from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.services.brand_extractor import extract_brand_info
from app.services.compliance_checker import check_compliance

router = APIRouter()

@router.post("/upload-brand-kit")
async def upload_brand_kit(pdf_file: UploadFile = File(...)):
    if not pdf_file.filename.lower().endswith(".pdf"):
        raise HTTPException(400, "Only PDF brand kits allowed")
    pdf_bytes = await pdf_file.read()
    brand_info = extract_brand_info(pdf_bytes)
    return {"brand_info": brand_info}

@router.post("/assess-compliance")
async def assess_compliance(image_file: UploadFile = File(...)):
    if not image_file.content_type.startswith("image/"):
        raise HTTPException(400, "Only image uploads allowed")
    img_bytes = await image_file.read()
    score, breakdown = check_compliance(img_bytes, {})
    return JSONResponse({"score": score, "details": breakdown})
