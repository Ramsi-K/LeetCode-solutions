import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    columns = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    return department.pivot_table(index="id", columns="month", values="revenue").reindex(columns=columns).rename(columns=lambda x: x+"_Revenue").reset_index()