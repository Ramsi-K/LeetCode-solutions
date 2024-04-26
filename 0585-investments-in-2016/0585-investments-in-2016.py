import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    insurance['count_2015'] = insurance.groupby('tiv_2015')['pid'].transform('count')
    insurance['latlon'] = insurance.groupby(['lat','lon'])['pid'].transform('count')
    insurance = insurance[(insurance['count_2015']>1) & (insurance['latlon']==1)][['tiv_2016']].sum().to_frame('tiv_2016').round(2)
    return insurance