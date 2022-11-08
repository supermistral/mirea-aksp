import os

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    PROJECT_TITLE: str = "Shopping list app"
    PROJECT_VERSION: str = "0.0.1"
    HOST_HTTP: str = os.environ.get('HOST_HTTP', 'http://')
    HOST_URL: str = os.environ.get('HOST_URL', 'localhost')
    HOST_PORT: int = int(os.environ.get('HOST_PORT', 8000))
    BASE_URL: str = f'{HOST_HTTP}{HOST_URL}:{HOST_PORT}'
    DATABASE_URL: PostgresDsn


def get_settings() -> Settings:
    settings = Settings()

    if (db := os.environ['POSTGRES_DB']) is not None:
        settings.DATABASE_URL = PostgresDsn.build(
            scheme='postgresql+asyncpg',
            user = settings.DATABASE_URL.user,
            password = settings.DATABASE_URL.password,
            host = settings.DATABASE_URL.host,
            port=settings.DATABASE_URL.port,
            path=f"/{db}",
        )

    return settings


settings = get_settings()
