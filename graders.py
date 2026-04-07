def grade_task(completed_subjects, total_subjects):
    score = len(completed_subjects) / total_subjects
    return round(score, 2)