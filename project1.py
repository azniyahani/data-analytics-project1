import pandas as pd
import numpy as np

# 1. Read the Excel dataset
df = pd.read_excel('dataset.xlsx')

print("=" * 50)
print("TASK 1: Dataset loaded successfully!")
print("=" * 50)

# 2. Display first 5 rows
print("\nTASK 2: First 5 rows of the dataset:")
print(df.head())

# 3. Show column names
print("\nTASK 3: Column names in the dataset:")
print(df.columns.tolist())

# 4. Find missing values
print("\nTASK 4: Missing values in each column:")
print(df.isnull().sum())

# 5. Find duplicate rows
print("\nTASK 5: Number of duplicate rows:")
print(f"Total duplicate rows: {df.duplicated().sum()}")

# 6. Find duplicate IDs (assuming 'ID' column exists)
if 'OrderID' in df.columns:
    print("\nTASK 6: Duplicate IDs:")
    
    duplicate_ids = df[df.duplicated(subset=['OrderID'], keep=False)]
    
    print(f"Count of duplicate IDs: {duplicate_ids['OrderID'].nunique()}")
    
    print(duplicate_ids.sort_values('OrderID'))

else:
    print("\nTASK 6: No 'OrderID' column found in dataset")

# 7. Convert date columns to datetime format
print("\nTASK 7: Converting date columns to datetime format...")
print("\nTASK 7: Converting Date column to datetime format...")

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    print("Date column converted successfully")
else:
    print("No Date column found")

# 8. Show invalid dates count (NaT values after conversion)
print("\nTASK 8: Invalid dates count:")
datetime_cols = df.select_dtypes(include=['datetime64']).columns
for col in datetime_cols:
    invalid_count = df[col].isna().sum()
    print(f"Invalid dates in '{col}': {invalid_count}")

# 9. Remove duplicate rows
print("\nTASK 9: Removing duplicate rows...")
initial_rows = len(df)
df = df.drop_duplicates()
removed_rows = initial_rows - len(df)
print(f"Removed {removed_rows} duplicate rows")

# 10. Fill missing values
print("\nTASK 10: Filling missing values...")
# Fill numeric columns with mean
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())
    print(f"Filled missing values in '{col}' with mean")

# Fill categorical/datetime columns with forward fill
df = df.ffill()
print("Missing values after filling:")
print(df.isnull().sum())

# 11. Save cleaned dataset
output_file = 'Cleaned_Dataset.xlsx'
# Create a completely fresh copy before saving
clean_df = df.copy()

# Save cleaned dataset
clean_df.to_excel(output_file, index=False)
print(f"\nTASK 11: Cleaned dataset saved as '{output_file}'")

print("\n" + "=" * 50)
print("Data cleaning process completed successfully!")
print("=" * 50)