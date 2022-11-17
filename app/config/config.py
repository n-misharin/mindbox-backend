import os

from pydantic import BaseSettings


class DefaultSettings(BaseSettings):
    PATH_PREFIX: str = os.environ.get("PATH_PREFIX", "/api/v1")
    APP_HOST: str = os.environ.get("APP_HOST", "http://127.0.0.1")
    APP_PORT: int = os.environ.get("APP_PORT", 8000)

    POSTGRES_DB: str = os.environ.get("POSTGRES", "market_db")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", "user")
    POSTGRES_PORT: int = os.environ.get("POSTGRES_PORT", 5432)
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD", "hackme")

    @property
    def database_uri(self) -> str:
        return f"postgres+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@" \
               f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
