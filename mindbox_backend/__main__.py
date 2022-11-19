from fastapi import FastAPI
from fastapi_pagination import add_pagination

from mindbox_backend.config.utils import get_settings
from mindbox_backend.endpoints import list_of_routes


def bind_routes(application: FastAPI, settings) -> None:
    for route in list_of_routes:
        application.include_router(route, prefix=settings.PATH_PREFIX)


def get_app() -> FastAPI:
    application = FastAPI(
        title="Market",
        docs_url="/swagger",
        openapi_url="/openapi",
    )
    settings = get_settings()
    bind_routes(application, settings)
    add_pagination(application)
    application.state.settings = settings
    return application


app = get_app()
