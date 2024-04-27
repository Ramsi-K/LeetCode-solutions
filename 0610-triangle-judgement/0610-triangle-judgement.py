import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = ["Yes" if ((x + y > z) and (x + z > y) and (y + z > x)) else "No" for x, y, z in zip(triangle.x, triangle.y, triangle.z)]
    return triangle