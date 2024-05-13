import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders.order_date.dt.year==2020) & (orders.order_date.dt.month==2)].groupby("product_id", as_index=False).sum("unit")
    orders = orders[orders.unit.ge(100)]
    return orders.merge(products, on="product_id", how="left")[["product_name", "unit"]]