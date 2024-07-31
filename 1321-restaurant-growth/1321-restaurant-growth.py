import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    out = customer.groupby("visited_on").sum()["amount"].rolling(7).agg({"amount":"sum", "average_amount":"mean"}).round(2).dropna().reset_index()
    print(out)
    return out