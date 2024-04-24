import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values("recordDate", inplace=True)
    weather.set_index("recordDate", inplace=True)
    if len(weather) >= 2:
        weather = weather.reindex(pd.date_range(weather.index[0], weather.index[-1]))
    weather["diff"] = weather["temperature"] - weather["temperature"].shift(1)
    res = weather[weather["diff"] > 0]
    return res[["id"]]
    