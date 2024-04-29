import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = project.merge(employee[["employee_id", "experience_years"]], on="employee_id")
    return (merged.groupby("project_id").agg(average_years = ("experience_years", "mean"))).reset_index()[["project_id", "average_years"]]