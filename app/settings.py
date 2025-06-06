from typing import List, Union
from pydantic import BaseSettings, AnyHttpUrl, validator

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

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
