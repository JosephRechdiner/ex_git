from typing import List
from fastapi import APIRouter
from app.models import EmployeeBase, EmployeeCreate, EmployeeResponse, EmployeeUpdate
from ...main import db

employees_router = APIRouter()

@employees_router.get("/employees", response_model=List[EmployeeResponse])
def employees():
    return db.get_all_employees()

@employees_router.get("/employees/{emp_id}", response_model=EmployeeResponse)
def employee_by_id(emp_id: str):
    return db.get_employee_by_id(emp_id)

@employees_router.post("/employees", response_model=EmployeeCreate)
def create_employee(employees: EmployeeBase):
    return db.add_employee(employees)

@employees_router.put("/employees/{emp_id}")
def put_employee(emp_id: str, employees: EmployeeUpdate):
    return db.update_employee(emp_id, employees)

@employees_router.delete("/employees/{emp_id}")
def put_employees(emp_id: str):
    has_deleted = db.delete_employee(emp_id)
    if has_deleted:
        return {"msg": "Deleted"}
    return {"msg": "Not deleted"}