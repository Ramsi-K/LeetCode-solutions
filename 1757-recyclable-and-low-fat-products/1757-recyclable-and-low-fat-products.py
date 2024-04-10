import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return (products[(products.low_fats=="Y") & (products.recyclable=="Y")][["product_id"]])
    # return products.query('low_fats=="Y" and recyclable=="Y"')[['product_id']]