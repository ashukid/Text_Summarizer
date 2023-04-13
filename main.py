from fastapi import FastAPI

from usecase import summarizer_router

def include_router(app):
    app.include_router(summarizer_router.router)

def start_application():
    app = FastAPI()
    include_router(app)

    return app

app = start_application()