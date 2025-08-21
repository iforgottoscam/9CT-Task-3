import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def get_available_datasets():
    """Return available dataset files"""
    return {
        "food_data.csv": os.path.exists("food_data.csv"),
        "cpi_australia.csv": os.path.exists("cpi_australia.csv")
    }

def load_dataset(filename):
    """Load the specified dataset file"""
    try:
        df = pd.read_csv(filename)
        print(f"{filename} loaded successfully!")
        return df
    except FileNotFoundError:
        print(f"{filename} not found. Creating sample data...")
        return create_sample_data(filename)

def create_sample_data(filename):
    """Create sample data for the specified file"""
    if filename == "food_data.csv":
        data = {
            'food_id': range(1, 51),
            'food_name': [f'Food_Item_{i}' for i in range(1, 51)],
            'category': np.random.choice(['Fruit', 'Vegetable', 'Dairy', 'Meat', 'Grain'], 50),
            'calories': np.random.randint(50, 500, 50),
            'price': np.random.uniform(1, 20, 50).round(2)
        }
    elif filename == "cpi_australia.csv":
        dates = pd.date_range('2020-01-01', periods=24, freq='M')
        data = {
            'Date': dates.strftime('%Y-%m-%d'),
            'CPI': np.random.uniform(110, 130, 24).round(2),
            'Inflation_Rate': np.random.uniform(1.5, 5.0, 24).round(2)
        }
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return df

def display_dataset_preview(dataset, filename):
    """Display a preview of the dataset"""
    print(f"\n=== {filename} Preview ===")
    print(f"Shape: {dataset.shape}")
    print(f"Columns: {list(dataset.columns)}")
    print("\nFirst 10 entries:")
    print(dataset.head(10))
    print("\nData types:")
    print(dataset.dtypes)

def display_visualisation(dataset, filename):
    """Create visualizations based on the dataset"""
    if dataset.empty:
        print("No data to visualize.")
        return
    
    print(f"\n=== {filename} Visualizations ===")
    
    if filename == "food_data.csv":
        # Food data visualizations
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        if 'category' in dataset.columns:
            category_counts = dataset['category'].value_counts()
            axes[0].bar(category_counts.index, category_counts.values)
            axes[0].set_title('Food Category Distribution')
            axes[0].tick_params(axis='x', rotation=45)
        
        if 'price' in dataset.columns:
            axes[1].hist(dataset['price'], bins=10, alpha=0.7, color='green')
            axes[1].set_title('Price Distribution')
            axes[1].set_xlabel('Price ($)')
        
        plt.suptitle('Food Data Analysis')
        
    elif filename == "cpi_australia.csv":
        # CPI data visualizations
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        if 'Date' in dataset.columns and 'CPI' in dataset.columns:
            dataset['Date'] = pd.to_datetime(dataset['Date'])
            axes[0].plot(dataset['Date'], dataset['CPI'], marker='o')
            axes[0].set_title('CPI Over Time')
            axes[0].tick_params(axis='x', rotation=45)
        
        if 'Inflation_Rate' in dataset.columns:
            axes[1].hist(dataset['Inflation_Rate'], bins=8, alpha=0.7, color='blue')
            axes[1].set_title('Inflation Rate Distribution')
            axes[1].set_xlabel('Inflation Rate (%)')
        
        plt.suptitle('CPI Australia Analysis')
    
    plt.tight_layout()
    plt.show()

def search_data(dataset, filename):
    """Search for specific data entries"""
    print(f"\n=== Search in {filename} ===")
    print("Available columns:", list(dataset.columns))
    column = input("Enter column to search: ").strip()
    
    if column not in dataset.columns:
        print("Column not found.")
        return
    
    value = input(f"Enter value to search in {column}: ").strip()
    
    try:
        if pd.api.types.is_numeric_dtype(dataset[column]):
            value = float(value)
            results = dataset[dataset[column] == value]
        else:
            results = dataset[dataset[column].astype(str).str.contains(value, case=False, na=False)]
        
        print(f"\nFound {len(results)} results:")
        print(results)
        
    except ValueError:
        print("Please enter a valid value for this column.")

def update_data_entry(dataset, filename):
    """Update a specific data entry"""
    print(f"\n=== Update in {filename} ===")
    try:
        print("First few rows:")
        print(dataset.head())
        
        row_index = int(input("Enter row index to update (0-based): "))
        
        if row_index not in dataset.index:
            print("Row index not found.")
            return dataset
        
        print("Available columns:", list(dataset.columns))
        column = input("Enter column to update: ").strip()
        
        if column not in dataset.columns:
            print("Column not found.")
            return dataset
        
        new_value = input(f"Enter new value for {column}: ").strip()
        
        if pd.api.types.is_numeric_dtype(dataset[column]):
            new_value = float(new_value)
        
        dataset.at[row_index, column] = new_value
        print("Entry updated successfully.")
        return dataset
        
    except ValueError as e:
        print(f"Error: {e}")
        return dataset

def save_changes(dataset, filename):
    """Save changes to the specified CSV file"""
    try:
        dataset.to_csv(filename, index=False)
        print(f"Changes saved to {filename}")
    except Exception as e:
        print(f"Error saving changes: {e}")
