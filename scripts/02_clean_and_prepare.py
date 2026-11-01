import os
import pandas as pd
import numpy as np

os.makedirs("cleaned_data", exist_ok=True)
os.makedirs("deliverables", exist_ok=True)

train_path = r"archive/ev_market_train.csv"
test_path = r"archive/ev_market_test.csv"

print("Reading raw datasets...")
df_train = pd.read_csv(train_path)
df_test = pd.read_csv(test_path)

print(f"Raw Train shape: {df_train.shape}")
print(f"Raw Test shape: {df_test.shape}")

# 1. Deduplication
print("\n--- Deduplication ---")
train_dups = df_train.duplicated().sum()
print(f"Full duplicate rows in Train: {train_dups}")
df_train_clean = df_train.drop_duplicates().copy()
print(f"Train shape after dropping exact duplicates: {df_train_clean.shape}")

test_dups = df_test.duplicated().sum()
print(f"Full duplicate rows in Test: {test_dups}")
df_test_clean = df_test.copy()

# Add source split column
df_train_clean['source_split'] = 'Train'
df_test_clean['source_split'] = 'Test'

# Combine for systematic imputation using population-level domain group medians
df_combined = pd.concat([df_train_clean, df_test_clean], ignore_index=True)
print(f"Combined fleet shape: {df_combined.shape}")

# 2. Imputation
print("\n--- Domain-Grounded Imputation ---")
# Compute group medians from the training split to prevent data leakage, then apply to both
# a. battery_cycle_life by battery_type
cycle_medians = df_train_clean.groupby('battery_type')['battery_cycle_life'].median()
print("Cycle life medians by battery_type (from Train):")
print(cycle_medians)
df_combined['battery_cycle_life'] = df_combined['battery_cycle_life'].fillna(
    df_combined['battery_type'].map(cycle_medians)
)

# b. infotainment_screen_inch by category
screen_medians = df_train_clean.groupby('category')['infotainment_screen_inch'].median()
print("\nInfotainment screen medians by category (from Train):")
print(screen_medians)
df_combined['infotainment_screen_inch'] = df_combined['infotainment_screen_inch'].fillna(
    df_combined['category'].map(screen_medians)
)

# c. annual_sales_units by category
sales_medians = df_train_clean.groupby('category')['annual_sales_units'].median()
print("\nAnnual sales medians by category (from Train):")
print(sales_medians)
df_combined['annual_sales_units'] = df_combined['annual_sales_units'].fillna(
    df_combined['category'].map(sales_medians)
)

# d. resale_value_pct_3yr by category
resale_medians = df_train_clean.groupby('category')['resale_value_pct_3yr'].median()
df_combined['resale_value_pct_3yr'] = df_combined['resale_value_pct_3yr'].fillna(
    df_combined['category'].map(resale_medians)
)

# e. customer_rating by category
rating_medians = df_train_clean.groupby('category')['customer_rating'].median()
df_combined['customer_rating'] = df_combined['customer_rating'].fillna(
    df_combined['category'].map(rating_medians)
)

# Verify zero nulls
print("\nNull counts after imputation in combined fleet:")
null_summary = df_combined.isnull().sum()
print(null_summary[null_summary > 0])
if null_summary.sum() == 0:
    print("SUCCESS: Zero missing values remaining across all columns!")

# 3. Data Type Standardization & Precision Formatting
print("\n--- Type Formatting & Normalization ---")
int_cols = [
    'model_year', 'num_motors', 'num_charging_ports', 'num_seats',
    'warranty_years', 'safety_rating_stars', 'autonomous_level', 'annual_sales_units'
]
for col in int_cols:
    df_combined[col] = df_combined[col].round().astype(int)

float_cols_2dec = [
    'battery_capacity_kwh', 'battery_cycle_life', 'battery_degradation_pct_5yr',
    'range_km', 'efficiency_wh_per_km', 'motor_power_kw', 'torque_nm',
    'top_speed_kmph', 'acceleration_0_100_sec', 'max_dc_charging_kw',
    'charging_dc_fast_time_min', 'charging_ac_time_hr', 'weight_kg',
    'cargo_capacity_liters', 'price_usd', 'insurance_cost_usd_yearly',
    'resale_value_pct_3yr', 'infotainment_screen_inch', 'customer_rating'
]
for col in float_cols_2dec:
    df_combined[col] = df_combined[col].round(2)

df_combined['co2_saved_tons_per_year'] = df_combined['co2_saved_tons_per_year'].round(3)

# String columns strip
str_cols = df_combined.select_dtypes(include=['object', 'string']).columns
for col in str_cols:
    df_combined[col] = df_combined[col].astype(str).str.strip()

# 4. Save Outputs
print("\n--- Exporting Clean Datasets ---")
# Separate back into train and test
clean_train = df_combined[df_combined['source_split'] == 'Train'].copy()
clean_test = df_combined[df_combined['source_split'] == 'Test'].copy()

clean_train_path = r"cleaned_data/cleaned_ev_train.csv"
clean_test_path = r"cleaned_data/cleaned_ev_test.csv"
unified_path = r"cleaned_data/cleaned_ev_dataset.csv"
deliverables_unified_path = r"deliverables/cleaned_ev_dataset.csv"

clean_train.to_csv(clean_train_path, index=False)
print(f"Exported: {clean_train_path} ({clean_train.shape})")

clean_test.to_csv(clean_test_path, index=False)
print(f"Exported: {clean_test_path} ({clean_test.shape})")

df_combined.to_csv(unified_path, index=False)
print(f"Exported: {unified_path} ({df_combined.shape})")

df_combined.to_csv(deliverables_unified_path, index=False)
print(f"Exported: {deliverables_unified_path} ({df_combined.shape})")

print("\nAll datasets successfully prepared and verified Tableau-ready!")

