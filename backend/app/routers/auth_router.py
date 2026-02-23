from fastapi import APIRouter
from app.schemas.auth_schema import RegisterRequest, LoginRequest
from app.services.auth_service import register_user, login_user

router = APIRouter()

@router.post("/register")
async def register(data: RegisterRequest):
    return await register_user(data)

@router.post("/login")
async def login(data: LoginRequest):
    return await login_user(data)
