def rename_columns(df, rename_map):
    return df.rename(columns=rename_map)

def standardize_column_names(df):
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df