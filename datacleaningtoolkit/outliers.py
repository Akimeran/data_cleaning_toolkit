import pandas as pd

def detect_outliers(df, column, method='iqr'):
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        return df[(df[column] < Q1 - 1.5 * IQR) | (df[column] > Q3 + 1.5 * IQR)]
    elif method == 'zscore':
        mean = df[column].mean()
        std = df[column].std()
        return df[(df[column] - mean).abs() > 3 * std]
    else:
        raise ValueError("Method must be 'iqr' or 'zscore'")