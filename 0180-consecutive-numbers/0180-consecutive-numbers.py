import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs.sort_values("id", inplace=True)
    logs.set_index("id", inplace=True)
    logs = logs.reindex(range(logs.index[0], logs.index[-1] + 1), fill_value=777)
    var = logs.rolling(window=3,min_periods=3).agg(['mean', 'var']).dropna()
    final_res = var.num[var.num==var.num//1].dropna()
    final_res = final_res[final_res["var"] == 0]
    final_res.rename(columns={"mean":"ConsecutiveNums"}, inplace=True)

    return final_res[["ConsecutiveNums"]].drop_duplicates()