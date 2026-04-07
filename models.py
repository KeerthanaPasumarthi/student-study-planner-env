from pydantic import BaseModel
from typing import List, Dict

class Observation(BaseModel):
    subjects: List[str]
    deadlines: Dict[str, int]
    study_hours_left: int
    completed_subjects: List[str]
    current_day: int

class Action(BaseModel):
    subject: str
    hours: int

class Reward(BaseModel):
    score: float
    message: str