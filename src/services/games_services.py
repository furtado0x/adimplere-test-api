import asyncio
from typing import List
from uuid import uuid4
from itertools import chain

import httpx

from src.schemas.games_schemas import (
    Game,
    GameShortDescription,
    GameLongDescription
)
from src.app.settings import Settings
from src.excepetion.games_excepetion import GameNotFoundExcepetion


class GamesService:
    @classmethod
    async def _list_games_by_api(cls, api: str) -> List[Game]:
        async with httpx.AsyncClient() as client:
            res = await client.get(
                api,
                headers={
                    "Content-Type": "application/json", 
                    "Authorization": "Bearer <token>"
                },
            )
            return [
                Game(
                    uuid=uuid4(),
                    name=game.get("title", ""),
                    short_description=game.get("shortDescription", ""),
                    long_description=game.get("longDescription", ""),
                )
                for game in res.json()
            ]

    @classmethod
    async def _list_games(cls) -> List[Game]:
        s = Settings()
        partners_api = s.partners_api
        games = await asyncio.gather(
            *(
                cls._list_games_by_api(api)
                for api in partners_api
            )
        )
        return list(chain.from_iterable(games))
        
    @classmethod
    async def _list_games_short_description(
        cls,
        games: List[Game]
    ):
        return [
            GameShortDescription(
                uuid=game.uuid,
                short_description=game.short_description
            )
            for game in games
        ]

    @classmethod
    async def _get_game_long_description(
        cls,
        name: str,
        games: List[Game]
    ) -> GameLongDescription:
        try:
            game = [
                GameLongDescription(
                    uuid=game.uuid,
                    long_description=game.long_description
                )
                for game in games if game.name == name
            ].pop()
        except IndexError:
            raise GameNotFoundExcepetion
        return game