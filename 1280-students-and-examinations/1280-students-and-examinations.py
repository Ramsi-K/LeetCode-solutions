import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    grouped = examinations.groupby(["student_id", "subject_name"]).agg(attended_exams=("subject_name", "count")).reset_index()
    crossed = pd.merge(students,subjects, how="cross")
    res = pd.merge(crossed, grouped, how="left", left_on=["student_id", "subject_name"], right_on=["student_id", "subject_name"]).sort_values(["student_id", "subject_name"])
    res[["attended_exams"]] = res[["attended_exams"]].fillna(0)

    return res[["student_id", "student_name", "subject_name", "attended_exams"]]