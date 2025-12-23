def transform_data(df):
    # Example transformations
    df.columns = df.columns.str.lower()
    df = df.dropna()
    return df