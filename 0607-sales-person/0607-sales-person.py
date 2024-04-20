import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(orders, company, on='com_id')
    res = sales_person[~sales_person['sales_id'].isin(merged[merged['name'] == 'RED']['sales_id'])][['name']]
    # print(res)
    return res
