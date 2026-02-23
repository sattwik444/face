from pydantic import BaseModel
from typing import List
from datetime import datetime

class OutfitCreate(BaseModel):
    image_url: str

class OutfitResponse(BaseModel):
    score: float
    suggestions: List[str]
    created_at: datetime
