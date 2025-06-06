# app/settings.py

import os
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str
    CORS_ORIGINS_RAW: str = ""
    CORS_ORIGINS: List[str] = []

    class Config:
        env_file = ".env"
        case_sensitive = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        raw = os.getenv("CORS_ORIGINS_RAW", "")
        self.CORS_ORIGINS = [origin.strip() for origin in raw.split(",") if origin.strip()]
