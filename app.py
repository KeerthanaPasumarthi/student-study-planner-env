from fastapi import FastAPI

app = FastAPI()

current_observation = {
    "subjects": ["Math", "Physics"],
    "deadlines": {"Math": 3, "Physics": 5},
    "study_hours_left": 4,
    "completed_subjects": [],
    "current_day": 1
}


@app.get("/")
def home():
    return {"message": "Study Planner API is running"}


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


@app.get("/state")
def get_state():
    return {
        "observation": current_observation
    }


@app.post("/step")
def step(action: dict):
    global current_observation

    subject = action.get("subject")
    hours = action.get("hours", 1)

    if subject not in current_observation["completed_subjects"]:
        current_observation["completed_subjects"].append(subject)

    current_observation["study_hours_left"] -= hours

    done = len(current_observation["completed_subjects"]) == len(current_observation["subjects"])

    reward = {
        "score": 1 if done else 0.5,
        "message": "Progress updated"
    }

    return {
        "observation": current_observation,
        "reward": reward,
        "done": done,
        "info": {}
    }
