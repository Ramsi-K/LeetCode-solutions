import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    out = register.groupby("contest_id", as_index=False).agg(percentage=("user_id", "count"))
    out["percentage"] = round((out["percentage"] / len(users)) * 100, 2)
    return out.sort_values(["percentage", "contest_id"], ascending=[False, True])