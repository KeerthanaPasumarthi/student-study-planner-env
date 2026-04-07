from models import Observation, Action, Reward
from tasks import TASKS

class StudyPlannerEnv:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.reset()

    def reset(self):
        task = TASKS[self.difficulty]

        self.subjects = task["subjects"]
        self.deadlines = task["deadlines"]
        self.study_hours_left = task["study_hours_left"]
        self.completed_subjects = []
        self.current_day = 1

        return Observation(
            subjects=self.subjects,
            deadlines=self.deadlines,
            study_hours_left=self.study_hours_left,
            completed_subjects=self.completed_subjects,
            current_day=self.current_day
        )

    def state(self):
        return {
            "subjects": self.subjects,
            "deadlines": self.deadlines,
            "study_hours_left": self.study_hours_left,
            "completed_subjects": self.completed_subjects,
            "current_day": self.current_day
        }

    def step(self, action: Action):
        reward_score = 0.0
        done = False
        info = {}

        if action.subject in self.subjects and action.subject not in self.completed_subjects:
            self.study_hours_left -= action.hours

            if action.hours >= 2:
                self.completed_subjects.append(action.subject)
                reward_score += 0.3

            if len(self.completed_subjects) == len(self.subjects):
                reward_score += 0.7
                done = True
        else:
            reward_score -= 0.2

        if self.study_hours_left <= 0:
            done = True

        observation = Observation(
            subjects=self.subjects,
            deadlines=self.deadlines,
            study_hours_left=self.study_hours_left,
            completed_subjects=self.completed_subjects,
            current_day=self.current_day
        )

        reward = Reward(
            score=max(0.0, min(1.0, reward_score)),
            message="Progress updated"
        )

        return observation, reward, done, info