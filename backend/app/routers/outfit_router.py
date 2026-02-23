from fastapi import APIRouter, Depends
from app.schemas.outfit_schema import OutfitCreate
from app.services.outfit_service import (
    analyze_and_store_outfit,
    get_user_outfits,
    like_outfit
)

router = APIRouter()

# TEMP user_id placeholder until auth middleware added
FAKE_USER_ID = "demo_user"

@router.post("/analyze")
async def analyze_outfit(data: OutfitCreate):
    return await analyze_and_store_outfit(FAKE_USER_ID, data.image_url)

@router.get("/my")
async def my_outfits():
    return await get_user_outfits(FAKE_USER_ID)

@router.post("/like/{outfit_id}")
async def like(outfit_id: str):
    return await like_outfit(outfit_id)
