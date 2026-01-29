from app.routes import missions
from fastapi import FastAPI
from app.database import Database

app = FastAPI()
app.include_router(missions.router, prefix="/api")
db = Database()