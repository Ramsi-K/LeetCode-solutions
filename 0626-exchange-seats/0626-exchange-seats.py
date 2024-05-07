import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    for i in range(1, len(seat["id"]), 2):
        seat["id"][i], seat["id"][i-1] = seat["id"][i-1], seat["id"][i]
    return seat.sort_values("id")