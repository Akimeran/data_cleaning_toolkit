import pandas as pd

def normalize_strings(df, columns):
    df_normalized = df.copy()
    for col in columns:
        df_normalized[col] = df_normalized[col].astype(str).str.strip().str.lower()
    return df_normalized