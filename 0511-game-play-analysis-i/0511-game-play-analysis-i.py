import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.sort_values("event_date").drop_duplicates("player_id", keep="first")[["player_id", "event_date"]].rename(columns={"event_date": "first_login"})