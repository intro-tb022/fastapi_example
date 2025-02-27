from fastapi import FastAPI

from src.dependencies import init_dep
from src.routes.routes import api_router
from src.seed import seed

def main():
    init_dep()
    seed()

app = FastAPI()
app.include_router(api_router)

main()