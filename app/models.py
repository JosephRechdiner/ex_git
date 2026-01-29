
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import uuid

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    office_name: str
    job_title: str

class EmployeeCreate(EmployeeBase):
    id: str = uuid.UUID

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

class Mission():
    def __init__(self,id:str,title:str,assigned_to:str,status:str,priority:str,deadline:str,created_at:datetime):
        self.id = id 
        self.title = title
        self.assigned_to =assigned_to
        self.status = status
        self.priority = priority
        self.deadline = deadline
        self.created_at = created_at

    def to_dict(self):
        return self.__dict__()


class MissionBase(BaseModel):
    title : str
    assigned_to : str
    status : str 
    priority : str
    deadline: str


class MissionCreate(MissionBase):
    id : str


class MissionUpdate(BaseModel):
    title :Optional[str]
    assigned_to :Optional[str]
    status : Optional[str]
    priority : Optional[str]
    deadline: Optional[str]


class MissionResponse(MissionCreate):
    create_at : datetime

