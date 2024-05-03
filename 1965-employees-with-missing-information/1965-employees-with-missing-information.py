import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    merged = employees.merge(salaries, on="employee_id", how="outer")
    return merged[merged.isnull().any(axis=1)].sort_values("employee_id")[["employee_id"]]