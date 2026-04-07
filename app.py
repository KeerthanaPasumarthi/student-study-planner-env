from fastapi import FastAPI
from environment import StudyPlannerEnv
from models import Action

app = FastAPI()

env = StudyPlannerEnv()

@app.get("/")
def home():
    return {"message": "Study Planner API is running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.get("/state")
def state():
    return env.state()

@app.post("/reset")
def reset():
    global current_observation

    current_observation = {
        "subjects": ["Math", "Physics"],
        "deadlines": {"Math": 3, "Physics": 5},
        "study_hours_left": 4,
        "completed_subjects": [],
        "current_day": 1
    }

    return {
        "message": "Environment reset",
        "observation": current_observation
    }