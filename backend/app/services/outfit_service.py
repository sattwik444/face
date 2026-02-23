import random
from datetime import datetime
from app.database.mongodb import db
from bson import ObjectId

async def analyze_and_store_outfit(user_id: str, image_url: str):
    score = round(random.uniform(6.0, 9.8), 2)

    suggestions = [
        "Nice color coordination.",
        "Consider adding subtle accessories.",
        "Footwear complements well.",
        "Confident campus-ready look!"
    ]

    outfit_doc = {
        "user_id": user_id,
        "image_url": image_url,
        "score": score,
        "suggestions": suggestions,
        "likes": 0,
        "created_at": datetime.utcnow()
    }

    result = await db.outfits.insert_one(outfit_doc)
    outfit_doc["id"] = str(result.inserted_id)

    return outfit_doc


async def get_user_outfits(user_id: str):
    outfits = await db.outfits.find({"user_id": user_id}).to_list(100)
    for o in outfits:
        o["id"] = str(o["_id"])
        del o["_id"]
    return outfits


async def like_outfit(outfit_id: str):
    await db.outfits.update_one(
        {"_id": ObjectId(outfit_id)},
        {"$inc": {"likes": 1}}
    )
    return {"message": "Liked"}
