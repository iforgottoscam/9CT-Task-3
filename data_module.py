
# data_module.py
import pandas as pd
import matplotlib.pyplot as plt

def load_food_price_data(filepath):
    """
    Loads the food price indices CSV and converts the 'Date' column to datetime.
    """
    df = pd.read_csv(filepath)
    
    # Ensure the 'Date' column exists and is in datetime format
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        raise ValueError("Expected a 'Date' column in the dataset.")
    
    return df

def plot_food_price_trends(df):
    """
    Plots line charts for each food price index over time.
    """
    plt.figure(figsize=(12, 6))
    
    # Plot each index column (excluding 'Date')
    for column in df.columns:
        if column != 'Date':
            plt.plot(df['Date'], df[column], label=column)
    
    plt.title("Food Price Indices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Index Value")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

