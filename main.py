#main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import Settings
from api.base import api_router
from api.v1.route_homepage import router
from database.session import engine
from database.base import Base
import uvicorn

def include_router(app):
    app.include_router(api_router)

def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=Settings.PROJECT_NAME,version=Settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app

app = start_application()

if __name__ == "__main__":
    uvicorn.run("main:app")