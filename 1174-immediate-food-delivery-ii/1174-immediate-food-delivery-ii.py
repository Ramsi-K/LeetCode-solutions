import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    out = delivery.sort_values("order_date").drop_duplicates("customer_id", keep="first")
    out = out[out.order_date == out.customer_pref_delivery_date]
    unique_customers = delivery.customer_id.nunique()
    immediate_deliveries = len(out)
    res = round(immediate_deliveries/unique_customers * 100, 2)
    # print(unique_customers)
    # print(out)
    # print(immediate_deliveries)
    # print(res)
    return pd.DataFrame([res], columns=["immediate_percentage"])