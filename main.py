import pandas as pd
import matplotlib.pyplot as plt

# --- Load CPI data ---
cpi_df = pd.read_csv("cpi_australia.csv")
cpi_df['Quarter'] = pd.to_datetime(cpi_df['Quarter'], format='%b-%y', errors='coerce')
cpi_df.rename(columns={'Quarter': 'Date', 'Annual change (%)': 'Inflation Rate'}, inplace=True)
cpi_df = cpi_df[['Date', 'Inflation Rate']]

# --- Load Food Price data ---
food_df = pd.read_csv("food_data.csv")
food_df['Date'] = pd.to_datetime(food_df['Date'], format='%Y-%m', errors='coerce')
food_df = food_df[['Date', 'Food Price Index']]

# --- Merge datasets ---
merged_df = pd.merge(cpi_df, food_df, on='Date', how='inner')

# --- Plot ---
plt.figure(figsize=(12, 6))
plt.plot(merged_df['Date'], merged_df['Inflation Rate'], label='Inflation Rate (%)', color='blue', marker='o')
plt.plot(merged_df['Date'], merged_df['Food Price Index'], label='Food Price Index', color='green', marker='o')

plt.title("Inflation Rate vs Food Price Index Over Time")
plt.xlabel("Date")
plt.ylabel("Rate / Index")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

from data_module import load_cpi_data, load_food_price_data, merge_datasets, plot_combined_trends

cpi_df = load_cpi_data("cpi_australia.csv")
food_df = load_food_price_data("food_data.csv")

merged_df = merge_datasets(cpi_df, food_df)
plot_combined_trends(merged_df)

