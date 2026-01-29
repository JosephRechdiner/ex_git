from fastapi import FastAPI
from app.routes.employees import employees_router
from app.database import Database

app = FastAPI()

db = Database()

app.include_router(employees_router)