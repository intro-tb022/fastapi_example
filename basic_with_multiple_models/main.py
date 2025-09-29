from contextlib import asynccontextmanager

from fastapi import FastAPI

from dependencies.dependencies import init_dep
from routes.routes import api_router
from seed import seed


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_dep()
    seed()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
