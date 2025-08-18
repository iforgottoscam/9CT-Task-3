import pandas as pd

# Create a dictionary of data
data = {
    "Category": ["General CPI", "Food & Beverages", "Dairy Products", "Bread & Cereals", "Olive Oil / Cheese"],
    "Annual Increase (%)": [2.1, 3.0, 15.0, 11.8, 100.0]
}

# Convert dictionary into a DataFrame
df = pd.DataFrame(data)

# Print DataFrame
print(df)

# If you want to save it to a CSV file
df.to_csv("inflation_vs_essentials.csv", index=False)
