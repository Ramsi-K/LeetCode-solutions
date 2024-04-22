import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    return employee.groupby("departmentId")["salary"].apply(lambda x: x[x.isin(np.sort(x.unique())[-3:])]).reset_index(level=0).join(employee["name"]).set_index("departmentId").join(department.set_index("id"), lsuffix='_emp',rsuffix='_dep').rename(columns={"name_dep": "Department", "name_emp": "Employee", "salary": "Salary"})[["Department", "Employee", "Salary"]]