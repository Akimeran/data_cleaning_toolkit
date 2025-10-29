import pandas as pd
import numpy as np

def clean_missing(df, strategy='mean', columns=None, fill_value=None):
    df_cleaned = df.copy()
    target_cols = columns if columns else df.columns

    for col in target_cols:
        if strategy == 'mean':
            if pd.api.types.is_numeric_dtype(df[col]):
                df_cleaned[col].fillna(df[col].mean(), inplace=True)
        elif strategy == 'median':
            if pd.api.types.is_numeric_dtype(df[col]):
                df_cleaned[col].fillna(df[col].median(), inplace=True)
        elif strategy == 'mode':
            df_cleaned[col].fillna(df[col].mode()[0], inplace=True)
        elif strategy == 'drop':
            df_cleaned.dropna(subset=[col], inplace=True)
        elif strategy == 'constant':
            df_cleaned[col].fillna(fill_value, inplace=True)
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
    return df_cleaned