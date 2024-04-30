import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    q1_prod = sales[(sales.sale_date >= "2019-01-01") & (sales.sale_date <= "2019-03-31")][["product_id"]]
    q24_prod = sales[(sales.sale_date < "2019-01-01") | (sales.sale_date > "2019-03-31")][["product_id"]]
    out_prod = q1_prod[~q1_prod.product_id.isin(q24_prod.product_id)]
    out_df = out_prod.merge(product[["product_id", "product_name"]], on="product_id")
    return out_df