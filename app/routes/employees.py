from typing import List
from fastapi import APIRouter
from app.models import EmployeeBase, EmployeeCreate, EmployeeResponse


employees_routes = APIRouter()

@employees_routes.get("/employees")
def employees():
    return db.get_all_employees()

@employees_routes.get("/employees/{emp_id}", response_model=EmployeeCreate)
def employee_by_id(emp_id: str):
    return db.get_employee_by_id(emp_id)

@employees_routes.post("/employees", response_model=EmployeeCreate)
def create_employees(employees: EmployeeBase):
    return db.add_employee(employees)

@employees_routes.get("/employees")
def get_employees():
    return db.get_all_employees()