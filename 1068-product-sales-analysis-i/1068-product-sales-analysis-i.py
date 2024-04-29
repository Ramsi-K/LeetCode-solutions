import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    out_df = sales[["product_id", "year", "price"]].merge(product, on="product_id")
    return out_df[["product_name", "year", "price"]]