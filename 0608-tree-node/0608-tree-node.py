import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree["parent"] = np.where(pd.isnull(tree["p_id"].values), "False", "True")
    tree["child"] = np.where(tree["id"].isin(tree["p_id"]), "True", "False")
    tree["type"] = "Root"
    tree.loc[(tree["parent"]=="True") & (tree["child"]=="False"), "type"] = "Leaf"
    tree.loc[(tree["parent"]=="True") & (tree["child"]=="True"), "type"] = "Inner"
    return tree[["id", "type"]]