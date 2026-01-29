from fastapi import APIRouter
from ...main import db
from ..models import MissionResponse, MissionCreate , MissionBase, Mission
router = APIRouter()

@router.get('/missions',response_model=MissionResponse)
def get_all_mission():
    return {'result':db.get_all_missions()}

@router.get('/missions/{mission_id}')
def get_mission_by_id(mission_id:str):
    res = db.get_mission_by_id(mission_id)
    return {"message":res}

@router.post('/missions')
def create_mission(raw_mission:MissionBase ):
    data = raw_mission.model_dump()
    data['id'] = str(len(db.missions) + 1)
    try:
        MissionCreate.model_validate(**data)
        new_mission = Mission(**data)
        db.add_mission(new_mission)
        return {'massage':"add mission succuss"}
    except Exception as e:
        return {'error': f'adding mission failed {e}'}

@router.put('/missions/{mission_id}')
def update_mission(mission_id:str):
    res = db.update_mission(mission_id)
    return

@router.delete('/missions/{mission_id}')
def delete_mission(mission_id:str):
    res = db.delete_mission(mission_id)
    return

@router.get('/missions/employee/{emp_id}')
def get_mission_by_employee_id(emp_id:str):
    res = db.get_missions_by_employee(emp_id)
    return
