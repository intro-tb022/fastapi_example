from fastapi import FastAPI

from dependencies import init_dep
from routes.routes import api_router
from seed import seed


def main():
    init_dep()
    seed()


app = FastAPI()
app.include_router(api_router)

main()
