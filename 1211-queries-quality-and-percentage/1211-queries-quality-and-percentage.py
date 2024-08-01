import pandas as pd

round_2 = lambda x: round(x + 1e-9, 2)

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries["quality"] = queries["rating"] / queries["position"]
    queries["poor_query_percentage"] = (queries["rating"] < 3) * 100
    # print(queries)
    out = queries.groupby("query_name")[["quality", "poor_query_percentage"]].mean().apply(round_2).reset_index()
    # print(out)
    return out

    # # print(queries[queries["query_name"] == "szsgysmafhfhstnagzhryxykvkmzn"])
    # # print(queries.columns)
    # queries = queries[queries["query_name"] == "szsgysmafhfhstnagzhryxykvkmzn"].drop(["query_name", "result"], axis=1)
    # queries["quality"] = queries["rating"] / queries["position"]
    # queries["poor_query_percentage"] = (queries["rating"] < 3) * 100
    # print(queries)
    # out = queries[["quality", "poor_query_percentage"]].mean().apply(round_2)
    # print(out)
    # # print(out.round(2))