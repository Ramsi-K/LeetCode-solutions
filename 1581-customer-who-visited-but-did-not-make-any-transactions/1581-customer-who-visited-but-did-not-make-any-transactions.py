import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    out = visits.merge(transactions, on="visit_id", how="left")
    out = out[out.transaction_id.isnull()]
    return out.groupby("customer_id", as_index=False).agg(count_no_trans=("visit_id", "count"))