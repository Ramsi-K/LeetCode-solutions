import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    counts = customer.drop_duplicates(["customer_id" ,"product_key"]).value_counts(["customer_id"]).reset_index()
    return counts[counts["count"]==len(product)][["customer_id"]]