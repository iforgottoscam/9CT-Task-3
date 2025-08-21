import os
from data_module import load_cpi_data, load_food_price_data, merge_datasets, plot_combined_trends

print("Current working directory:", os.getcwd())

# Use your renamed files
cpi_path = "cpi_australia.csv.csv"
food_path = "food_data.csv.csv"

try:
    cpi_df = load_cpi_data(cpi_path)
    food_df = load_food_price_data(food_path)
    merged_df = merge_datasets(cpi_df, food_df)

    print(f"Merged dataset has {len(merged_df)} rows")
    plot_combined_trends(merged_df)

except FileNotFoundError as e:
    print(f"Error: {e}")
# main.py
