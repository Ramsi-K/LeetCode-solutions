import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity["first"] = activity.groupby("player_id").event_date.transform("min")
    activity["second"] = activity["first"] + pd.DateOffset(1) == activity["event_date"]

    return pd.DataFrame({"fraction": [round(sum(activity.second) / activity.player_id.nunique(), 2)]})