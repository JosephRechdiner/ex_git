from pydantic import BaseModel,Field
from models import Mission
from typing import List,Optional


class Database():
    def __init__(self):
        # TODO: its modify conflict
        self.missions: List[Mission] = []
    
    def add_mission(self,mission:Mission)-> Mission:
        self.missions.append(mission)
        
    def get_all_missions(self) -> List[Mission]:
        return self.missions
    
    def get_mission_by_id(self,mission_id:str)-> Optional[Mission]:
        for mission in self.missions:
            if mission_id == mission.id:
                return mission
        return None
    
    def get_missions_by_employee(self,emp_id:str) -> List[Mission]:
        for mission in self.missions:
            if mission.assigned_to == emp_id:
                return mission
        return None
    def update_mission(mission_id, data) -> Optional[Mission]:
        pass
    def delete_mission(mission_id) -> bool:
        pass

def init_sample_data():
    # TODO: modify
        pass