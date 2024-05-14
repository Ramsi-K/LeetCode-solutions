import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    out = transactions.groupby("account", as_index=False).agg(balance=("amount", "sum"))
    out = out[out.balance>10000]
    out = out.merge(users, on="account", how="left")
    return out[["name", "balance"]]