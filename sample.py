import seaborn as sns
import pandas as pd

# Load the tips dataset
tips = sns.load_dataset("tips")

# Total number of records
print("Total Number of Records:", len(tips))

# Average total bill by gender
avg_bill_gender = tips.groupby("sex")["total_bill"].mean()

# Average tip by day
avg_tip_day = tips.groupby("day")["tip"].mean()

# Maximum and minimum tip
max_tip = tips["tip"].max()
min_tip = tips["tip"].min()

# Count of customers by day
customer_count = tips["day"].value_counts()

# Display results
print("\nAverage Total Bill by Gender:")
print(avg_bill_gender)

print("\nAverage Tip by Day:")
print(avg_tip_day)

print("\nMaximum Tip:", max_tip)
print("Minimum Tip:", min_tip)

print("\nNumber of Customers by Day:")
print(customer_count)
