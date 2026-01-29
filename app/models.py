from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    office_name: str
    job_title: str

class EmployeeCreate(EmployeeBase):
    id: str

class EmployeeUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    office_name: Optional[str]
    job_title: Optional[str]

class EmployeeResponse(EmployeeBase):
    id: str
    created_at: Optional[str] | None
    updated_at: Optional[str] | None
    
class Employee:
    def __init__(self, id: str, first_name: str, last_name: str, office_name: str, job_title: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.office_name = office_name
        self.job_title = job_title
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.updated_at = None

    def to_dict(self):
        return self.__dict__
