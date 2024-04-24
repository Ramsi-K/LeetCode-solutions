import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips = trips[~(trips["request_at"].ge("2013-10-04") | trips["request_at"].le("2013-09-30"))]
    merged_clients = trips.merge(users[["users_id", "banned"]], left_on="client_id", right_on = "users_id")
    merged_all = merged_clients.merge(users[["users_id", "banned"]], left_on="driver_id", right_on = "users_id", suffixes= ("_client", "_driver"))
    merged_all.drop(["users_id_client", "users_id_driver", "city_id", "client_id", "driver_id"], axis=1, inplace=True)
    merged_all = merged_all[~((merged_all["banned_client"]=="Yes") | (merged_all["banned_driver"]=="Yes"))]

    total_rides = merged_all.groupby("request_at").agg(
        total_rides= pd.NamedAgg("id", "count")).reset_index()
    cancelled_rides = merged_all[merged_all["status"].isin(["cancelled_by_client", "cancelled_by_driver"])].groupby("request_at").agg(cancelled_rides=("id", "count"))

    merged_res = cancelled_rides.merge(total_rides, on="request_at", how="outer").fillna(0)
    merged_res["Cancellation Rate"] = (merged_res["cancelled_rides"] / merged_res["total_rides"]).round(2)
    merged_res.rename(columns={"request_at":"Day"}, inplace=True)

    return merged_res[["Day", "Cancellation Rate"]]