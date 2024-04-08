import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= 0: return pd.DataFrame([{f"getNthHighestSalary({N})":None}])
    unique_salaries = employee.salary.sort_values(ascending=False).drop_duplicates(ignore_index=True)
    n_highest_salary = unique_salaries.iloc[N-1] if len(unique_salaries)>N-1 else None
    return pd.DataFrame([{f"getNthHighestSalary({N})":n_highest_salary}])