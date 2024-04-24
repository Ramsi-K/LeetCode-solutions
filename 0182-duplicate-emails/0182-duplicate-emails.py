import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    res = person.groupby("email").agg(count = pd.NamedAgg("email", "count")).reset_index()
    res = res[res["count"]>1]
    return res[["email"]].rename(columns={"email":"Email"})