from typing import List, Union
from pydantic import BaseSettings, AnyHttpUrl, validator
# app/settings.py

import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("CORS_ORIGINS", pre=True)
    def parse_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str) and v:
            return [origin.strip() for origin in v.split(",")]
        if isinstance(v, list):
            return v
        return []
    CORS_ORIGINS: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]