import pandas as pd

def validate_df(df: pd.DataFrame):
    # not used currently
    required = {"year", "count", "name"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing columns: {required - set(df.columns)}")