import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    out = activity.sort_values(["machine_id", "process_id", "timestamp"]).set_index(["machine_id", "process_id"]) 
    # print(out)
    out = out.groupby(level=[0,1]).agg({"timestamp":"diff"}).round(3).dropna()
    # print(out)
    out = out.groupby(level=0).mean().round(3).rename(columns={"timestamp": "processing_time"}).reset_index()
    # print(out)
    return out