from pydantic import BaseModel
from typing import Optional
from datetime import datetime


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
