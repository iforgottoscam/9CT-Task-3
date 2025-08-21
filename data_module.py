import pandas as pd
import matplotlib.pyplot as plt

# ---------- Data Loading ----------
def load_cpi_data(filepath):
    """
    Load CPI dataset without converting quarters to dates.
    Returns a DataFrame with all columns as in the CSV.
    """
    df = pd.read_csv(filepath)
    return df

def load_food_data(filepath):
    """
    Load FAO Food Price Index dataset and keep only relevant columns if present.
    Returns a DataFrame.
    """
    df = pd.read_csv(filepath)
    
    # If the expected columns exist, keep only them
    if 'Date' in df.columns and 'Food Price Index' in df.columns:
        df = df[['Date', 'Food Price Index']].dropna()
    
    return df

# ---------- Plotting ----------
def plot_cpi(df):
    """
    Plot CPI quarterly and annual change using index as x-axis.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Change from previous quarter (%)'], marker='o', label='Quarterly Change (%)')
    plt.plot(df.index, df['Annual change (%)'], marker='s', label='Annual Change (%)')
    plt.title('CPI Trends in Australia')
    plt.xlabel('Data Point Index')
    plt.ylabel('Percentage Change')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_food_index(df):
    """
    Plot FAO Food Price Index using index as x-axis.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Food Price Index'], color='orange', marker='o')
    plt.title('FAO Food Price Index')
    plt.xlabel('Data Point Index')
    plt.ylabel('Index (2014-2016=100)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
# main.py
# This script serves as the main entry point for the data visualization module.