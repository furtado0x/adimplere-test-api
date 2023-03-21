from typing import List

from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    partners_api: List[str] = Field(env="PARTNERS_API")

    class Config:
        env_file = ".env"
        case_sensitive = False
        env_file_encoding = "utf-8"