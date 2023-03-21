from pydantic import UUID4, BaseModel

class Game(BaseModel):
    uuid: UUID4
    name: str
    short_description: str
    long_description: str

class GameShortDescription(BaseModel):
    uuid: UUID4
    short_description: str

class GameLongDescription(BaseModel):
    uuid: UUID4
    long_description: str
