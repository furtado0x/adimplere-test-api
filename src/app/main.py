from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from src import __version__
from src.app.route import router

def app_init() -> FastAPI:
    origins = [
        "httop://localhost",
        "httop://localhost:8080"
    ]

    _app = FastAPI(
        title="API Adimplere Test",
        version=__version__,
        description="API desenvolvida para integração com outras APIs"
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    _app.include_router(router, prefix="/api")
    add_pagination(_app)

    return _app

app = app_init()