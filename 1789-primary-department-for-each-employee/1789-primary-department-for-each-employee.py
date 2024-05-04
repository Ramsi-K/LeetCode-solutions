import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    grouped = employee.groupby("employee_id", as_index=False).agg(total=("employee_id", "count"))
    merged = employee.merge(grouped, on="employee_id", how="left")
    concat = pd.concat([merged.query('total==1'), merged[(merged.total!=1) & (merged.primary_flag=="Y")]])
    return concat[["employee_id", "department_id"]]

    