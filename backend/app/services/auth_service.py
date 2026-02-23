from passlib.context import CryptContext
from app.database.mongodb import db
from app.core.security import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def register_user(data):
    existing = await db.users.find_one({"email": data.email})
    if existing:
        return {"error": "User already exists"}

    hashed = pwd_context.hash(data.password)

    user = {
        "email": data.email,
        "username": data.username,
        "class_name": data.class_name,
        "password": hashed,
        "xp": 0,
        "level": 0,
        "streak": 0
    }

    await db.users.insert_one(user)
    return {"message": "User registered"}

async def login_user(data):
    user = await db.users.find_one({"email": data.email})
    if not user:
        return {"error": "Invalid credentials"}

    if not pwd_context.verify(data.password, user["password"]):
        return {"error": "Invalid credentials"}

    token = create_access_token({"sub": str(user["_id"])})
    return {"access_token": token}
