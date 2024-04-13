import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    return department.merge(employee, left_on="id", right_on="departmentId", suffixes=["_department", "_employee"]).drop(["id_department", "id_employee", "departmentId"], axis=1).rename(columns={"name_department": "Department", "name_employee": "Employee", "salary": "Salary" }).groupby(["Department"]).apply(lambda x: x[x["Salary"] == x["Salary"].max()])