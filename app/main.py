from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Sample FastAPI Project")

app.include_router(router)