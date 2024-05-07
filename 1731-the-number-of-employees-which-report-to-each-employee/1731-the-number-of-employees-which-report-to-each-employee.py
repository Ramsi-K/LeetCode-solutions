import pandas as pd
import decimal

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    reports = employees.dropna(subset="reports_to")\
                .groupby("reports_to", as_index=False)\
                .agg(reports_count=("reports_to", "count"),\
                    average_age=("age", lambda x: decimal.Decimal(np.mean(x)).to_integral_value(rounding=decimal.ROUND_HALF_UP)))
                    
    out = reports.merge(employees[["employee_id", "name"]], left_on="reports_to", right_on="employee_id", how="left")
    return out[["employee_id", "name", "reports_count", "average_age"]].sort_values("employee_id")
