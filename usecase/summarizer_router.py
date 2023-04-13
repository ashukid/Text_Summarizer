from fastapi import APIRouter, UploadFile

from .summarizer_service import get_summary

router = APIRouter(tags=["Meeting Summary Endpoints"],prefix="/app/v1")

@router.post("/summary")
async def public_get_summary(file: UploadFile):
    return await get_summary(file)