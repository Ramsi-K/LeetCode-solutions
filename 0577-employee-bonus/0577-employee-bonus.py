import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    res = bonus.merge(employee[["empId", "name"]], on="empId", how="outer")
    res = res[(res["bonus"] < 1000) | (res["bonus"].isna())]
    return res[["name", "bonus"]].sort_values("name")