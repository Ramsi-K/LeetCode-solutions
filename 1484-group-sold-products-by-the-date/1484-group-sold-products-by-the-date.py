import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities\
                .groupby(["sell_date"])\
                .agg(
                    num_sold=("product", "nunique"),
                    products= ("product", lambda x: ",".join(sorted(x.unique())))
                    )\
                .reset_index()

    return activities