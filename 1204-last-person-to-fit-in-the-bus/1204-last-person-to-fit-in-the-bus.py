import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values("turn", inplace=True)
    # print(queue)
    # print("-------------------------------")
    starting_wt = 0
    max_wt = 1000
    for i, row in queue.iterrows():
        starting_wt += row.weight
        if starting_wt > max_wt:
            not_allowed = row.turn
            print(row.turn)
            break
        last_allowed = row.person_name
    
    # print(f"Last person allowed: {last_allowed}")
    return pd.DataFrame([last_allowed], columns=["person_name"])
        