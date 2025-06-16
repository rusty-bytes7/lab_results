#this module will flag the results as low or high based on the reference range
import pandas as pd
def flag_results(df):
    """
    Flags the results in the DataFrame based on the reference range.
    
    Parameters:
    df (DataFrame): DataFrame containing lab results with 'Result', 'Low', and 'High' columns.
    
    Returns:
    DataFrame: DataFrame with an additional 'Flag' column indicating 'Low', 'High', or 'Normal'.
    """
    if not {'Result', 'ReferenceLow', 'ReferenceHigh'}.issubset(df.columns):
        raise ValueError("DataFrame must contain 'Result', 'ReferenceLow', and 'ReferenceHigh' columns.")
    
    def flag(row):
        if row['Result'] < row['ReferenceLow']:
            return 'Low'
        elif row['Result'] > row['ReferenceHigh']:
            return 'High'
        else:
            return 'Normal'
    
    df['Flag'] = df.apply(flag, axis=1)
    return df