import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(person, address, how="left", on="personId").drop(["personId", "addressId"], axis=1)