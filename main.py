from fastapi import FastAPI

from dependencies.database import init_db
from dependencies.sqlmodel import init_engine
from routes.routes import api_router


def main():
    init_engine()
    init_db()


main()

app = FastAPI()
app.include_router(api_router)
