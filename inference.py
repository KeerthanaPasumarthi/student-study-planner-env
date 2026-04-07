from environment import StudyPlannerEnv
from models import Action
from graders import grade_task

for difficulty in ["easy", "medium", "hard"]:
    print(f"[START] Task: {difficulty}")

    env = StudyPlannerEnv(difficulty=difficulty)
    observation = env.reset()

    done = False

    while not done:
        remaining_subjects = [
            s for s in observation.subjects
            if s not in observation.completed_subjects
        ]

        if not remaining_subjects:
            break

        action = Action(subject=remaining_subjects[0], hours=2)

        print(f"[STEP] Taking action: {action}")

        observation, reward, done, info = env.step(action)

        print(f"[STEP] Reward: {reward.score}")

    final_score = grade_task(
        env.completed_subjects,
        len(env.subjects)
    )

    print(f"[END] Final Score: {final_score}")
    print("-" * 40)