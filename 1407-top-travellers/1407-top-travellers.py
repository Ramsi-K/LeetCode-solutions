import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    grouped = rides[["user_id", "distance"]].groupby("user_id", as_index=False).sum()
    merged = grouped.merge(users, left_on="user_id", right_on="id", how="right").fillna(0)
    out = merged[["name", "distance"]].sort_values(["distance", "name"], ascending=[False, True]).rename(columns={"distance":"travelled_distance"})
    return out