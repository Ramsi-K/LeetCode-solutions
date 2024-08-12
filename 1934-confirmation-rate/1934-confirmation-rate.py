import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    confirmations.action = np.where(confirmations.action=="confirmed", 1, 0)
    out = confirmations.groupby("user_id", as_index=False)[["user_id", "action"]].mean().round(2).rename(columns={"action": "confirmation_rate"})
    out = out.merge(signups[["user_id"]], how="right").fillna(0.0)
    return out