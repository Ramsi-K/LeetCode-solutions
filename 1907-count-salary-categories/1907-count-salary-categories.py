import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    bins = [-np.inf, 19999, 50000, np.inf]
    labels=["Low Salary","Average Salary","High Salary"]

    return accounts.groupby(pd.cut(accounts.income, bins, labels=labels)).count().drop("income", axis=1).rename(columns={"account_id": "accounts_count"}).reset_index().rename(columns={"income": "category"}).sort_values("accounts_count", ascending=False)