# LC 1757 / Pandas
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products.copy()
    # Just saving conditionals which we will use to filter
    low_fats = df.low_fats == 'Y'
    recyclables = df.recyclable == 'Y'
    filtered = df[low_fats & recyclables]
    # If you don't surround product_id with [] then it will return a series (1d array)
    # Passing it within a list gives a proper dataframe (and we can select multiple columns this way if we want)
    return filtered[['product_id']]
