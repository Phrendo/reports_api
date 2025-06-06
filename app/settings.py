# reports_api/app/settings.py

import os
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str
    CORS_ORIGINS: List[str] = []

    class Config:
        env_file = ".env"
        case_sensitive = True
