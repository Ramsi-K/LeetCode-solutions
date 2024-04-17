import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    grouped = courses.groupby("class").count().reset_index()
    return grouped[grouped["student"] >= 5]["class"].to_frame()