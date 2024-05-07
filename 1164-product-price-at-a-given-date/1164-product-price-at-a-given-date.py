import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    unique_pid = pd.DataFrame(products.product_id.unique(), columns=["product_id"])
    products = products[products.change_date.le("2019-08-16")]
    date_changed = products.groupby("product_id", as_index=False)["change_date"].max()
    out = unique_pid.merge(date_changed.merge(products, on=["change_date", "product_id"], how="left")[["product_id", "new_price"]], on="product_id", how="left").fillna(10).rename(columns={"new_price":"price"})
    return out