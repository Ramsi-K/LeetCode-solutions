import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    res = employee.merge(employee[["id","salary"]],left_on ="managerId", right_on = "id", suffixes = ["_emp", "_man"])
    res = res[res["salary_emp"] > res["salary_man"]][["name"]]
    res.columns = ["Employee"]

    return res