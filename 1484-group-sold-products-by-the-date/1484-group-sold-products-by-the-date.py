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
    # activities = activities\
    # .sort_values("product")\
    # .groupby(["sell_date"])\
    # .agg(
    #     # num_sold=("product", "count"),
    #     products= ("product", ",".join)
    #     )\
    #     .reset_index()
  
    # activities["products"]= activities["products"].str.split(",").apply(set).apply(sorted).apply(",".join)
    # activities["num_sold"]= activities["products"].str.split(",").apply(lambda x: len(x))

    # return activities[["sell_date", "num_sold", "products"]]