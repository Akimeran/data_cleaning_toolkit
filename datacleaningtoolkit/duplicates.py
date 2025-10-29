def remove_duplicates(df, subset=None, keep='first'):
    return df.drop_duplicates(subset=subset, keep=keep)

def flag_duplicates(df, subset=None):
    df_flagged = df.copy()
    df_flagged['is_duplicate'] = df.duplicated(subset=subset)
    return df_flagged