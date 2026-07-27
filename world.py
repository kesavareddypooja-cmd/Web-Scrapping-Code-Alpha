import pandas as pd
import seaborn as sns

# Load the tips dataset
df = sns.load_dataset("tips")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# Display the shape of the dataset
print("\nShape of the Dataset:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Display correlation between numerical columns
print("\nCorrelation Matrix:")
print(df.select_dtypes(include='number').corr())
