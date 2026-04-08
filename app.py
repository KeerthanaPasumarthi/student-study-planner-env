from fastapi import FastAPI
from environment import StudyPlannerEnvironment

app = FastAPI()

env = StudyPlannerEnvironment()


@app.get("/")
def home():
    return {"message": "Study Planner API is running"}


@app.post("/reset")
def reset():
    observation = env.reset()

    return {
        "message": "Environment reset",
        "observation": observation
    }


@app.get("/state")
def get_state():
    return {
        "observation": env.get_observation()
    }


@app.post("/step")
def step(action: dict):
    subject = action.get("subject")
    hours = action.get("hours", 1)

    observation, reward, done, info = env.step(subject, hours)

    return {
        "observation": observation,
        "reward": reward,
        "done": done,
        "info": info
    }
