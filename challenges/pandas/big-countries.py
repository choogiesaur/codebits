# LC 595 / Pandas Study Plan
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    # Select rows where given conditions are met
    big_countries = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    
    # Return only given columns from the filtered set
    columns_to_return = ['name','population','area']
    res = big_countries[columns_to_return]
    return res
