from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    auth_router,
    outfit_router,
    presentation_router,
    avatar_router,
    social_router,
    chat_router,
    gamification_router,
    challenge_router
)

app = FastAPI(title="Campus AI Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router, prefix="/api/auth", tags=["auth"])
app.include_router(outfit_router.router, prefix="/api/outfit", tags=["outfit"])
app.include_router(presentation_router.router, prefix="/api/presentation", tags=["presentation"])
app.include_router(avatar_router.router, prefix="/api/avatar", tags=["avatar"])
app.include_router(social_router.router, prefix="/api/social", tags=["social"])
app.include_router(gamification_router.router, prefix="/api/gamification", tags=["gamification"])
app.include_router(challenge_router.router, prefix="/api/challenge", tags=["challenge"])
app.include_router(chat_router.router)
