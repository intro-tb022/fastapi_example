from fastapi import FastAPI

from src.dependencies.sqlmodel import init_engine
from src.dependencies.database import init_db
from src.routes.routes import api_router


def main():
    init_engine()
    init_db()


main()

app = FastAPI()
app.include_router(api_router)
