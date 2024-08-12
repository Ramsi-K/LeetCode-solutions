import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["odd"] = np.where(transactions["amount"]%2==0, "even_sum", "odd_sum")
    # print(transactions)
    out = pd.pivot_table(transactions, values="amount", index=["transaction_date"],
                       columns=["odd"], aggfunc="sum").fillna(0).reset_index()[["transaction_date", "odd_sum", "even_sum"]]
    # print(out)
    return out