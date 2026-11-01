import os
import pandas as pd
import numpy as np

# Ensure directories
os.makedirs("deliverables", exist_ok=True)
os.makedirs("scripts", exist_ok=True)

# Load data for exact statistics
df = pd.read_csv("cleaned_ev_dataset.csv")

total_records = len(df)
unique_models = df['model_name'].nunique()
total_mfg = df['manufacturer'].nunique()
avg_rating = df['customer_rating'].mean()
avg_range = df['range_km'].mean()
avg_bat = df['battery_capacity_kwh'].mean()
total_sales = df['annual_sales_units'].sum()

print("Loaded cleaned dataset successfully:")
print(f"Records: {total_records:,}, Unique Models: {unique_models:,}, OEMs: {total_mfg}")

