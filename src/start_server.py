from settings import SQL_BASE, SERVER_HOST, SERVER_PORT

import sys

sys.path.append('C:/exzemkafe/')

from src.server.sql_base.kafe_db import base_worker
from fastapi import FastAPI
from src.server.router import routers
from uvicorn import run
from fastapi.responses import RedirectResponse

base_worker.create_base(SQL_BASE)

app = FastAPI(title='kafe', version='Alpha 0.1')


@app.get("/")
def start_page() -> RedirectResponse:
    return RedirectResponse('/docs')


[app.include_router(router) for router in routers]


if __name__ == "__main__":
    run("start_server:app", reload=True, host=SERVER_HOST, port=SERVER_PORT)
