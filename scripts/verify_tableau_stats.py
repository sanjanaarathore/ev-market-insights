import pandas as pd
import numpy as np

df = pd.read_csv("cleaned_ev_dataset.csv")

print("=== PART 1: EXACT KPI VALUES ===")
total_records = len(df)
unique_models = df['model_name'].nunique()
total_mfg = df['manufacturer'].nunique()
avg_rating = df['customer_rating'].mean()
avg_range = df['range_km'].mean()
avg_bat = df['battery_capacity_kwh'].mean()
total_sales = df['annual_sales_units'].sum()

print(f"1. Total EV Model Records: {total_records:,}")
print(f"   Unique Commercial Models (model_name): {unique_models:,}")
print(f"2. Total Manufacturers (COUNTD): {total_mfg}")
print(f"3. Average Customer Rating: {avg_rating:.2f} / 5.0")
print(f"4. Average Driving Range: {avg_range:.2f} km")
print(f"5. Average Battery Capacity: {avg_bat:.2f} kWh")
print(f"6. Total Annual Sales: {total_sales:,.0f} units")

print("\n=== VISUALIZATION 2: CATEGORY PERFORMANCE ===")
cat_perf = df.groupby('category').agg(
    models_count=('vehicle_id', 'count'),
    total_sales=('annual_sales_units', 'sum'),
    avg_sales=('annual_sales_units', 'mean'),
    avg_price=('price_usd', 'mean')
).sort_values(by='models_count', ascending=False)
cat_perf['share_pct'] = (cat_perf['models_count'] / total_records * 100).round(2)
print(cat_perf)

print("\n=== VISUALIZATION 3: TOP MANUFACTURERS & DONUT SHARE ===")
mfg_perf = df.groupby('manufacturer').agg(
    models_count=('vehicle_id', 'count'),
    total_sales=('annual_sales_units', 'sum')
).sort_values(by='models_count', ascending=False)
print("Top 10 OEMs by model count:")
print(mfg_perf.head(10))

print("\n=== VISUALIZATION 4: CUSTOMER RATING BY CATEGORY ===")
rating_cat = df.groupby('category')['customer_rating'].agg(
    avg_rating='mean',
    median_rating='median',
    min_rating='min',
    max_rating='max',
    count='count'
).sort_values(by='avg_rating', ascending=False)
print(rating_cat.round(3))

print("\n=== VISUALIZATION 5: ANNUAL EV SALES BY MODEL YEAR ===")
sales_trend = df.groupby('model_year')['annual_sales_units'].agg(
    total_sales='sum',
    avg_sales='mean',
    models_count='count'
)
print(sales_trend)

print("\n=== VISUALIZATION 6: BATTERY TECHNOLOGY SHARE ===")
bat_share = df.groupby('battery_type').agg(
    models_count=('vehicle_id', 'count'),
    avg_cycle_life=('battery_cycle_life', 'mean'),
    avg_degradation_5yr=('battery_degradation_pct_5yr', 'mean')
).sort_values(by='models_count', ascending=False)
bat_share['share_pct'] = (bat_share['models_count'] / total_records * 100).round(2)
print(bat_share.round(2))

print("\n=== VISUALIZATION 7: MANUFACTURING COUNTRY DISTRIBUTION ===")
country_perf = df.groupby('manufacturing_country').agg(
    models_count=('vehicle_id', 'count'),
    total_sales=('annual_sales_units', 'sum')
).sort_values(by='models_count', ascending=False)
country_perf['share_pct'] = (country_perf['models_count'] / total_records * 100).round(2)
print(country_perf)

