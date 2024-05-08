import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    out = activity[activity.activity_date.between("2019-06-28","2019-07-27")].groupby(["activity_date"]).nunique("user_id")
    out = out.reset_index().rename(columns={"activity_date":"day", "user_id":"active_users"})
    return out[["day", "active_users"]]