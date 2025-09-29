from dependencies.dependencies import init_dep
from fastapi import FastAPI
from routes.routes import api_router

from basic_with_multiple_models.seed import seed


def main():
    init_dep()
    seed()


app = FastAPI()
app.include_router(api_router)

main()
