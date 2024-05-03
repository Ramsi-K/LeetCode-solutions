import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.dropna(subset=["manager_id"])[(~employees.dropna(subset=["manager_id"]).manager_id.isin(employees["employee_id"])) & (employees.salary<30000)].sort_values("employee_id")[["employee_id"]]