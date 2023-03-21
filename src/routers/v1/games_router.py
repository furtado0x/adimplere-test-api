from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from src.schemas.games_schemas import (
    Game,
    GameShortDescription,
    GameLongDescription
)
from src.services.games_services import GamesService

router = APIRouter(
    prefix="/v1/games", tags=["games"]
)

@router.get(
    "",
    description="Lista todos os Games",
    status_code=status.HTTP_200_OK,
    response_model=List[GameShortDescription],
)
async def get_all(
    games: List[Game] = Depends(
        GamesService._list_games
    ),
):
    return await GamesService._list_games_short_description(
        games
    )

@router.get(
    "/{name}",
    description="Lista todos os Games",
    status_code=status.HTTP_200_OK,
    response_model=GameLongDescription,
)
async def get_one(
    name: str,
    games: List[Game] = Depends(
        GamesService._list_games
    ),
):
    return await GamesService._get_game_long_description(
        name, games
    )