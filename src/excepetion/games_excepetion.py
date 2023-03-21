from fastapi import HTTPException
from starlette import status

GameNotFoundExcepetion = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Game não encontrado."
)