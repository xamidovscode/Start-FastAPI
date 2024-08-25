from fastapi import FastAPI
from app.core.server import Server
from app.sections.common.routers import router

def app():
    project = FastAPI(
        title="Start FastAPI",
    )
    project.include_router(router)
    return Server(project).get_app()

