import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return sales.assign(first_year = sales.groupby("product_id").year.transform(min)).query("first_year == year").iloc[:,[1,5,3,4]]