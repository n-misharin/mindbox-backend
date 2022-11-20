import asyncio
import os
from types import SimpleNamespace
from uuid import uuid4
import pytest
import pytest_asyncio
from httpx import AsyncClient

from alembic.command import upgrade
from alembic.config import Config

from sqlalchemy_utils import create_database, database_exists, drop_database
from sqlalchemy.orm import Session

from mindbox_backend.__main__ import get_app
from mindbox_backend.config.utils import get_settings
from tests.utils import make_alembic_config

from mindbox_backend.db.connection.session import SessionManager


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
def postgres() -> str:
    settings = get_settings()

    tmp_name = ".".join([uuid4().hex, "pytest"])
    settings.POSTGRES_DB = tmp_name
    os.environ["POSTGRES_DB"] = tmp_name

    tmp_url = settings.database_uri_sync
    if not database_exists(settings.database_uri_sync):
        create_database(settings.database_uri_sync)

    try:
        yield tmp_url
    finally:
        drop_database(tmp_url)


@pytest_asyncio.fixture
def alembic_config(postgres) -> Config:
    cmd_options = SimpleNamespace(
        config="mindbox_backend/db/",
        name="alembic",
        pg_url=postgres,
        raiseerr=False, x=None
    )
    return make_alembic_config(cmd_options)


@pytest_asyncio.fixture
def migrated_postgres(alembic_config: Config):
    upgrade(alembic_config, "head")


@pytest_asyncio.fixture
async def database(postgres, migrated_postgres, manager: SessionManager = SessionManager()) -> Session:
    manager.refresh()
    session_maker = SessionManager().get_session_maker()
    async with session_maker() as session:
        yield session


@pytest_asyncio.fixture
async def client(migrated_postgres, manager: SessionManager = SessionManager()) -> AsyncClient:
    app = get_app()
    manager.refresh()
    async with AsyncClient(app=app, base_url="http://test") as app_client:
        yield app_client
