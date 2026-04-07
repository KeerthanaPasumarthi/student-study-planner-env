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

@app.post("/step")
def step(action: Action):
    observation, reward, done, info = env.step(action)

    return {
        "observation": observation.dict(),
        "reward": reward.dict(),
        "done": done,
        "info": info
    }