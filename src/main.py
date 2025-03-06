from fastapi import FastAPI

from src.dependencies.sqlmodel import init_sqlmodel
from src.dependencies.database import init_dep
from src.routes.routes import api_router
from src.seed import seed

def main():
    init_dep()
    init_sqlmodel()

    # seed()

app = FastAPI()
app.include_router(api_router)

main()