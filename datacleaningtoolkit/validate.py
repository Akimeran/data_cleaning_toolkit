def validate_schema(df, expected_schema):
    errors = {}
    for col, expected_type in expected_schema.items():
        if col not in df.columns:
            errors[col] = 'Missing column'
        else:
            actual_type = df[col].dtype
            if not isinstance(df[col].dropna().iloc[0], expected_type):
                errors[col] = f'Expected {expected_type}, got {type(df[col].dropna().iloc[0])}'
    return errors