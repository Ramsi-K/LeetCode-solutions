import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium = stadium[stadium.people >= 100].sort_values(by='id')
    out = (stadium.id.diff() == 1) & (stadium.id.diff().shift(1) == 1)
    return stadium[out | out.shift(-1) | out.shift(-2)]
