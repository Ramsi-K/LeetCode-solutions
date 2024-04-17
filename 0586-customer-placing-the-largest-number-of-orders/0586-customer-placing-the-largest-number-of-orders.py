import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.mode()[["customer_number"]].head(1)
    # grouped = orders.groupby("customer_number").count().reset_index()
    # return grouped[grouped["order_number"]==grouped["order_number"].max()][["customer_number"]]