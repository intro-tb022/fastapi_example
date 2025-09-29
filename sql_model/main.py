from contextlib import asynccontextmanager

from dependencies.database import init_db
from dependencies.sqlmodel import init_engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routes import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_engine()
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
