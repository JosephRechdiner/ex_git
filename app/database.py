from datetime import datetime
from typing import List, Optional
from app.models import Employee, EmployeeCreate, EmployeeUpdate

class Database:
    def __init__(self):
        self.employees = self.init_sample_data()

    def add_employee(self, employee: EmployeeCreate) -> Employee:
        self.employees.append(employee)
        return employee
    
    def get_all_employees(self) -> List[Employee]:
        return self.employees
    
    def get_employee_by_id(self, emp_id: str) -> Optional[Employee]:
        for employee in self.employees:
            if employee.id == emp_id:
                return employee
            
    def update_employee(self, emp_id: str, data: EmployeeUpdate) -> Optional[Employee]:
        for employee in self.employees:
            if employee.id == emp_id:
                employee.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                for key, value in data.items():
                    employee[key] = value
                return employee
            
    def delete_employee(self, emp_id: str) -> bool:
        new_employees = [employee for employee in self.employees if employee.id != emp_id]
        has_changed = len(self.employees) == len(new_employees)
        self.employees = new_employees
        return has_changed
    
    def init_sample_data(self):
        data = [
            {"id": "1", "first_name": "Yossi", "last_name": "Rechdiner", "office_name": "kodkod", "job_title": "engineer"},
            {"id": "2", "first_name": "Moshe", "last_name": "Elmaliach", "office_name": "kodkod", "job_title": "engineer"},
            {"id": "2", "first_name": "Yossi", "last_name": "Kipper", "office_name": "kodkod", "job_title": "engineer"},
            {"id": "2", "first_name": "Aharon", "last_name": "Segal", "office_name": "kodkod", "job_title": "engineer"}
        ]
        employees = []
        for employee in data:
            new_employee = Employee(**employee)
            employees.append(new_employee)
        return employees

    def to_dict(self) -> List[dict]:
        return [employee.to_dict() for employee in self.employees]

        
 