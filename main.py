
from fastapi import FastAPI
from app.routes.employees import employees_router
from app.database import Database
from app.routes import missions


app = FastAPI()

db = Database()

app.include_router(employees_router)
app.include_router(missions.router, prefix="/api")


