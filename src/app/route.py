from fastapi import APIRouter

from src.routers.v1.games_router import router as games_router

router = APIRouter()

router.include_router(games_router)

@router.get("/health-check")
async def health_check():
    return {"status": "ok"}