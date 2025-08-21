import pandas as pd

def load_food_data(filepath):
    """
    Load FAO Food Price Index dataset and ensure the 'Food Price Index' column exists.
    Cleans column names to avoid KeyError issues.
    """
    df = pd.read_csv(filepath)

    # Clean column names: strip spaces, lowercase
    df.columns = df.columns.str.strip().str.lower()

    # Try to standardize the column name
    if 'value' in df.columns:
        df.rename(columns={'value': 'food price index'}, inplace=True)
    elif 'food price index' not in df.columns:
        raise KeyError(
            f"No 'Food Price Index' column found. Available columns: {list(df.columns)}"
        )

    return df


def load_inflation_data(filepath):
    """
    Load inflation dataset and ensure the 'Inflation Rate' column exists.
    Cleans column names to avoid KeyError issues.
    """
    df = pd.read_csv(filepath)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Try to standardize the column name
    if 'inflation rate' not in df.columns:
        # If it's named differently, try to guess
        possible_matches = [col for col in df.columns if 'inflation' in col]
        if possible_matches:
            df.rename(columns={possible_matches[0]: 'inflation rate'}, inplace=True)
        else:
            raise KeyError(
                f"No 'Inflation Rate' column found. Available columns: {list(df.columns)}"
            )

    return df

