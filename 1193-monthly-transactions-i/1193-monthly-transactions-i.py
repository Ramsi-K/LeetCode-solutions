import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["month"] = pd.to_datetime(transactions['trans_date']).apply(lambda x: '{year}-{month}'.format(year=x.year, month='{:02}'.format(x.month)))
    # transactions.dropna(subset="country", inplace=True)
    # print(transactions)
    # print("------------------------------------------------------------------")
    total = transactions.groupby(["country", "month"], as_index=False, dropna=False).agg({"id": "count", "amount": "sum"}).rename({"id": "trans_count", "amount":"trans_total_amount"}, axis=1)
    # print(total)
    # print("------------------------------------------------------------------")
    approved = transactions[transactions.state == "approved"].groupby(["country", "month"], as_index=False, dropna=False).agg({"id": "count", "amount": "sum"}).rename({"id": "approved_count", "amount": "approved_total_amount"}, axis=1)
    # print(approved)
    # print("------------------------------------------------------------------")
    out = pd.merge(left = total, right = approved, how = "left", on = ["country", "month"]).sort_values(["month"])
    # print(out)
    return out[["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"]].fillna({"approved_count":0, "approved_total_amount":0})