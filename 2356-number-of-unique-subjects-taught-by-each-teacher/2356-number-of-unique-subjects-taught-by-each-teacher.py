import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher[["teacher_id", "subject_id"]].drop_duplicates(["teacher_id", "subject_id"]).groupby("teacher_id").count().reset_index().rename(columns={"subject_id":"cnt"})