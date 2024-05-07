import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders_in_2019 = orders[orders.order_date.dt.year==2019].groupby("buyer_id").agg(orders_in_2019=("item_id","count")).reset_index()
    merged = orders_in_2019.merge(users[["user_id", "join_date"]], left_on="buyer_id", right_on="user_id", how="right")
    merged[["orders_in_2019"]] = merged[["orders_in_2019"]].fillna(0)
    return merged[["user_id", "join_date", "orders_in_2019"]].rename(columns={"user_id":"buyer_id"})