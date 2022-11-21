import os

from pydantic import BaseSettings


class DefaultSettings(BaseSettings):
    PATH_PREFIX: str = os.environ.get("PATH_PREFIX", "/api/v1")
    APP_HOST: str = os.environ.get("APP_HOST", "http://127.0.0.1")
    APP_PORT: int = os.environ.get("APP_PORT", 80)

    POSTGRES_DB: str = os.environ.get("POSTGRES_DB", "market_db")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", "user")
    POSTGRES_PORT: int = os.environ.get("POSTGRES_PORT", 5432)
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD", "hackme")

    PAGINATION_PAGE_SIZE: int = 50

    def get_base_app_url(self):
        return f"{self.APP_HOST}{self.PATH_PREFIX}:{self.APP_PORT}"

    @property
    def database_uri(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@" \
               f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def database_uri_sync(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@" \
               f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
