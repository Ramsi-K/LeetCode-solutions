import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    count1 = request_accepted.groupby("requester_id").agg(count1=("requester_id", "count")).reset_index()
    count2 = request_accepted.groupby("accepter_id").agg(count2=("accepter_id", "count")).reset_index()
    merged = count1.merge(count2, how="outer", left_on = "requester_id", right_on="accepter_id").fillna({"count1":0, "count2":0})
    merged["num"] = merged.count1 + merged.count2
    merged["id"] = np.where(merged.requester_id.notnull(), merged.requester_id, merged.accepter_id)
    return merged[merged.num == merged.num.max()][["id", "num"]]