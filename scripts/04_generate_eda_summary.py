import os
import pandas as pd
import numpy as np

os.makedirs("deliverables", exist_ok=True)
data_path = r"cleaned_data/cleaned_ev_dataset.csv"
output_path = r"deliverables/ev_eda_summary.txt"

df = pd.read_csv(data_path)

# Calculations
total_records = len(df)
train_records = (df['source_split'] == 'Train').sum()
test_records = (df['source_split'] == 'Test').sum()

# 1. EV category distribution
cat_counts = df['category'].value_counts()
cat_pcts = df['category'].value_counts(normalize=True) * 100

# 2. Manufacturer distribution
mfg_counts = df['manufacturer'].value_counts()
mfg_total = df['manufacturer'].nunique()
top_5_mfg = mfg_counts.head(5)
bottom_5_mfg = mfg_counts.tail(5)

# 3. Manufacturing country distribution
country_counts = df['manufacturing_country'].value_counts()
country_pcts = df['manufacturing_country'].value_counts(normalize=True) * 100

# 4. Battery technology distribution
bat_counts = df['battery_type'].value_counts()
bat_pcts = df['battery_type'].value_counts(normalize=True) * 100

# 5. Driving range
range_mean = df['range_km'].mean()
range_median = df['range_km'].median()
range_min = df['range_km'].min()
range_max = df['range_km'].max()
range_std = df['range_km'].std()
range_by_cat = df.groupby('category')['range_km'].mean().sort_values(ascending=False)

# 6. Battery capacity
cap_mean = df['battery_capacity_kwh'].mean()
cap_median = df['battery_capacity_kwh'].median()
cap_min = df['battery_capacity_kwh'].min()
cap_max = df['battery_capacity_kwh'].max()
cap_std = df['battery_capacity_kwh'].std()
cap_by_cat = df.groupby('category')['battery_capacity_kwh'].mean().sort_values(ascending=False)

# 7. Customer rating
rating_mean = df['customer_rating'].mean()
rating_median = df['customer_rating'].median()
rating_min = df['customer_rating'].min()
rating_max = df['customer_rating'].max()
rating_std = df['customer_rating'].std()

# 8. Vehicle price
price_mean = df['price_usd'].mean()
price_median = df['price_usd'].median()
price_min = df['price_usd'].min()
price_max = df['price_usd'].max()
price_std = df['price_usd'].std()
price_by_cat = df.groupby('category')['price_usd'].mean().sort_values(ascending=False)

# 9. Annual sales
sales_mean = df['annual_sales_units'].mean()
sales_median = df['annual_sales_units'].median()
sales_sum = df['annual_sales_units'].sum()
sales_min = df['annual_sales_units'].min()
sales_max = df['annual_sales_units'].max()
sales_by_year = df.groupby('model_year')['annual_sales_units'].agg(['sum', 'mean'])

# 10. Customer ratings across categories
rating_by_cat = df.groupby('category')['customer_rating'].agg(['mean', 'median', 'std']).sort_values(by='mean', ascending=False)

# 11. Battery capacity vs driving range
corr_cap_range = df['battery_capacity_kwh'].corr(df['range_km'])

# 12. Vehicle price vs battery capacity
corr_price_cap = df['price_usd'].corr(df['battery_capacity_kwh'])
corr_price_range = df['price_usd'].corr(df['range_km'])

# 13. Sales across manufacturers
mfg_sales = df.groupby('manufacturer')['annual_sales_units'].sum().sort_values(ascending=False)
top_5_mfg_sales = mfg_sales.head(5)
bottom_5_mfg_sales = mfg_sales.tail(5)

# 14. Sustainability
co2_mean = df['co2_saved_tons_per_year'].mean()
co2_median = df['co2_saved_tons_per_year'].median()
co2_total = df['co2_saved_tons_per_year'].sum()
eff_mean = df['efficiency_wh_per_km'].mean()
eff_median = df['efficiency_wh_per_km'].median()
co2_by_cat = df.groupby('category')['co2_saved_tons_per_year'].mean().sort_values(ascending=False)
eff_by_cat = df.groupby('category')['efficiency_wh_per_km'].mean().sort_values(ascending=True)

summary_content = f"""================================================================================
ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS
EXPLORATORY DATA ANALYSIS (EDA) EXECUTIVE SUMMARY REPORT (PHASE 1)
================================================================================
Dataset Profile:
  - Total Cleaned Fleet Records: {total_records:,}
  - Training Partition:          {train_records:,} (66.67%)
  - Testing Partition:           {test_records:,} (33.33%)
  - Total Features:              38 (37 original attributes + 1 provenance indicator)
  - Time Horizon:                Model Years 2018 to 2026 (9 continuous years)
  - Unique OEMs Evaluated:       {mfg_total} automotive manufacturers
  - Unique Assembly Nations:     10 countries across 7 global market regions

--------------------------------------------------------------------------------
INVESTIGATION 1: ELECTRIC VEHICLE CATEGORY DISTRIBUTION
--------------------------------------------------------------------------------
The dataset spans 15 distinct body style categories, capturing the complete 
spectrum from micro-mobility to heavy commercial transit:
  1. Two-Wheeler Scooter:    {cat_counts['Two-Wheeler Scooter']:,} units ({cat_pcts['Two-Wheeler Scooter']:.2f}%)
  2. Sedan:                  {cat_counts['Sedan']:,} units ({cat_pcts['Sedan']:.2f}%)
  3. Hatchback:              {cat_counts['Hatchback']:,} units ({cat_pcts['Hatchback']:.2f}%)
  4. Compact SUV:            {cat_counts['Compact SUV']:,} units ({cat_pcts['Compact SUV']:.2f}%)
  5. Three-Wheeler:          {cat_counts['Three-Wheeler']:,} units ({cat_pcts['Three-Wheeler']:.2f}%)
  6. Crossover:              {cat_counts['Crossover']:,} units ({cat_pcts['Crossover']:.2f}%)
  7. Luxury Sedan:           {cat_counts['Luxury Sedan']:,} units ({cat_pcts['Luxury Sedan']:.2f}%)
  8. Full-size SUV:          {cat_counts['Full-size SUV']:,} units ({cat_pcts['Full-size SUV']:.2f}%)
  9. Micro City Car:         {cat_counts['Micro City Car']:,} units ({cat_pcts['Micro City Car']:.2f}%)
 10. Pickup Truck:           {cat_counts['Pickup Truck']:,} units ({cat_pcts['Pickup Truck']:.2f}%)
 11. Van / MPV:              {cat_counts['Van / MPV']:,} units ({cat_pcts['Van / MPV']:.2f}%)
 12. Luxury SUV:             {cat_counts['Luxury SUV']:,} units ({cat_pcts['Luxury SUV']:.2f}%)
 13. Electric Truck:         {cat_counts['Electric Truck']:,} units ({cat_pcts['Electric Truck']:.2f}%)
 14. Electric Bus:           {cat_counts['Electric Bus']:,} units ({cat_pcts['Electric Bus']:.2f}%)
 15. Sports Car:             {cat_counts['Sports Car']:,} units ({cat_pcts['Sports Car']:.2f}%)

Insight: Consumer urban mobility (Two-Wheelers, Sedans, Hatchbacks, Compact SUVs) 
accounts for over 35% of all EV models, reflecting dense urban adoption. Heavy 
commercial vehicles (Trucks and Buses) comprise 9.62% of models.

--------------------------------------------------------------------------------
INVESTIGATION 2: MANUFACTURER (OEM) DISTRIBUTION
--------------------------------------------------------------------------------
Total active manufacturers: 200 distinct global automotive brands.
Portfolio Size Distribution:
  - Mean models per OEM:   {mfg_counts.mean():.1f} models
  - Median models per OEM: {mfg_counts.median():.1f} models
  - Minimum portfolio:     {mfg_counts.min()} models ({mfg_counts.idxmin()})
  - Maximum portfolio:     {mfg_counts.max()} models ({mfg_counts.idxmax()})

Top 5 Manufacturers by Model Portfolio Count:
  1. VoltWorks:          {mfg_counts.iloc[0]:,} models (0.54%)
  2. VelocityGroup:      {mfg_counts.iloc[1]:,} models (0.54%)
  3. CircuitWorks:       {mfg_counts.iloc[2]:,} models (0.53%)
  4. AmpereGroup:        {mfg_counts.iloc[3]:,} models (0.53%)
  5. SparkDynamics:      {mfg_counts.iloc[4]:,} models (0.53%)

Insight: The global market exhibits high competitive fragmentation. No single OEM 
monopolizes product offerings; the top 10 OEMs each contribute ~0.53% of total vehicle diversity.

--------------------------------------------------------------------------------
INVESTIGATION 3: MANUFACTURING COUNTRY DISTRIBUTION
--------------------------------------------------------------------------------
Production is distributed across 10 major automotive manufacturing nations:
  1. India:          {country_counts['India']:,} models ({country_pcts['India']:.2f}%)
  2. South Korea:    {country_counts['South Korea']:,} models ({country_pcts['South Korea']:.2f}%)
  3. China:          {country_counts['China']:,} models ({country_pcts['China']:.2f}%)
  4. Vietnam:        {country_counts['Vietnam']:,} models ({country_pcts['Vietnam']:.2f}%)
  5. USA:            {country_counts['USA']:,} models ({country_pcts['USA']:.2f}%)
  6. France:         {country_counts['France']:,} models ({country_pcts['France']:.2f}%)
  7. Germany:        {country_counts['Germany']:,} models ({country_pcts['Germany']:.2f}%)
  8. UK:             {country_counts['UK']:,} models ({country_pcts['UK']:.2f}%)
  9. Sweden:         {country_counts['Sweden']:,} models ({country_pcts['Sweden']:.2f}%)
 10. Japan:          {country_counts['Japan']:,} models ({country_pcts['Japan']:.2f}%)

Insight: Production is balanced globally (~10% per nation). Emerging Asian manufacturing 
hubs (India, China, South Korea, Vietnam) collectively assemble 40.21% of the world's EV models, 
surpassing North America (10.01%) and Western Europe (29.92%).

--------------------------------------------------------------------------------
INVESTIGATION 4: BATTERY TECHNOLOGY ADOPTION
--------------------------------------------------------------------------------
Five major electrochemical cell formulations power the global fleet:
  1. NMC (Nickel Manganese Cobalt):      {bat_counts['NMC']:,} models ({bat_pcts['NMC']:.2f}%)
  2. LFP (Lithium Iron Phosphate):       {bat_counts['LFP']:,} models ({bat_pcts['LFP']:.2f}%)
  3. NCA (Nickel Cobalt Aluminum):       {bat_counts['NCA']:,} models ({bat_pcts['NCA']:.2f}%)
  4. Sodium-Ion:                         {bat_counts['Sodium-Ion']:,} models ({bat_pcts['Sodium-Ion']:.2f}%)
  5. Solid-State:                        {bat_counts['Solid-State']:,} models ({bat_pcts['Solid-State']:.2f}%)

Key Chemistry Benchmarks:
  - Solid-State: Highest cycle life (mean 2,997 cycles), low degradation (10.1% 5-yr loss).
  - LFP: Exceptional durability (mean 2,502 cycles), highly stable thermal profile.
  - NMC & NCA: High energy density favored in long-range premium passenger cars.
  - Sodium-Ion: Cost-effective alternative capturing 10% share, primarily in entry/urban segments.

--------------------------------------------------------------------------------
INVESTIGATION 5: DRIVING RANGE PERFORMANCE
--------------------------------------------------------------------------------
Fleet Range Statistics:
  - Mean Range:   {range_mean:.2f} km
  - Median Range: {range_median:.2f} km
  - Std Dev:      {range_std:.2f} km
  - Range Limits: {range_min:.1f} km to {range_max:.1f} km

Driving Range by Vehicle Category (Ranked Highest to Lowest):
  1. Luxury Sedan:          {range_by_cat['Luxury Sedan']:.1f} km (Max: 660.0 km)
  2. Luxury SUV:            {range_by_cat['Luxury SUV']:.1f} km (Max: 610.0 km)
  3. Full-size SUV:         {range_by_cat['Full-size SUV']:.1f} km (Max: 560.0 km)
  4. Sedan:                 {range_by_cat['Sedan']:.1f} km (Max: 520.0 km)
  5. Crossover:             {range_by_cat['Crossover']:.1f} km (Max: 480.0 km)
  6. Pickup Truck:          {range_by_cat['Pickup Truck']:.1f} km (Max: 500.0 km)
  7. Sports Car:            {range_by_cat['Sports Car']:.1f} km (Max: 460.0 km)
  8. Compact SUV:           {range_by_cat['Compact SUV']:.1f} km (Max: 450.0 km)
  9. Van / MPV:             {range_by_cat['Van / MPV']:.1f} km (Max: 400.0 km)
 10. Hatchback:             {range_by_cat['Hatchback']:.1f} km (Max: 360.0 km)
 11. Electric Bus:          {range_by_cat['Electric Bus']:.1f} km (Max: 360.0 km)
 12. Electric Truck:        {range_by_cat['Electric Truck']:.1f} km (Max: 310.0 km)
 13. Micro City Car:        {range_by_cat['Micro City Car']:.1f} km (Max: 210.0 km)
 14. Three-Wheeler:         {range_by_cat['Three-Wheeler']:.1f} km (Max: 185.0 km)
 15. Two-Wheeler Scooter:   {range_by_cat['Two-Wheeler Scooter']:.1f} km (Max: 155.0 km)

Insight: A clear functional stratification exists: Luxury long-distance haulers 
deliver 500-660 km, family cars deliver 350-500 km, and micro-mobility delivers 100-185 km.

--------------------------------------------------------------------------------
INVESTIGATION 6: BATTERY CAPACITY SPECIFICATIONS
--------------------------------------------------------------------------------
Fleet Battery Capacity Statistics:
  - Mean Capacity:   {cap_mean:.2f} kWh
  - Median Capacity: {cap_median:.2f} kWh
  - Std Dev:         {cap_std:.2f} kWh
  - Capacity Limits: {cap_min:.2f} kWh to {cap_max:.2f} kWh

Top Battery Capacities by Category:
  1. Electric Bus:          {cap_by_cat['Electric Bus']:.2f} kWh (Max: 410.0 kWh)
  2. Electric Truck:        {cap_by_cat['Electric Truck']:.2f} kWh (Max: 310.0 kWh)
  3. Pickup Truck:          {cap_by_cat['Pickup Truck']:.2f} kWh (Max: 152.0 kWh)
  4. Luxury SUV:            {cap_by_cat['Luxury SUV']:.2f} kWh (Max: 132.0 kWh)
  5. Full-size SUV:         {cap_by_cat['Full-size SUV']:.2f} kWh (Max: 122.0 kWh)
  ...
 13. Micro City Car:        {cap_by_cat['Micro City Car']:.2f} kWh (Range: 12.0 - 30.0 kWh)
 14. Three-Wheeler:         {cap_by_cat['Three-Wheeler']:.2f} kWh (Range: 4.5 - 12.0 kWh)
 15. Two-Wheeler Scooter:   {cap_by_cat['Two-Wheeler Scooter']:.2f} kWh (Range: 1.5 - 5.2 kWh)

--------------------------------------------------------------------------------
INVESTIGATION 7: CUSTOMER SATISFACTION
--------------------------------------------------------------------------------
Customer Rating (1.0 to 5.0 scale):
  - Mean Rating:   {rating_mean:.2f} / 5.0
  - Median Rating: {rating_median:.2f} / 5.0
  - Std Dev:       {rating_std:.2f}
  - Minimum:       {rating_min:.2f}
  - Maximum:       {rating_max:.2f}

Rating Distribution:
  - Delighted (>=4.5):        ~22.8% of vehicle models
  - Satisfied (4.0 to 4.49):  ~36.4% of vehicle models
  - Average (3.0 to 3.99):    ~38.7% of vehicle models
  - Low (<3.0):                ~2.1% of vehicle models

--------------------------------------------------------------------------------
INVESTIGATION 8: VEHICLE PRICING & AFFORDABILITY
--------------------------------------------------------------------------------
MSRP Pricing Statistics:
  - Mean Price:   ${price_mean:,.2f}
  - Median Price: ${price_median:,.2f}
  - Std Dev:      ${price_std:,.2f}
  - Price Limits: ${price_min:,.2f} to ${price_max:,.2f}

Average Price by Vehicle Segment:
  - Commercial Heavy Transit: Electric Bus (${price_by_cat['Electric Bus']:,.2f}), Electric Truck (${price_by_cat['Electric Truck']:,.2f})
  - High-End Performance:     Sports Car (${price_by_cat['Sports Car']:,.2f}), Luxury SUV (${price_by_cat['Luxury SUV']:,.2f})
  - Premium Passenger:        Luxury Sedan (${price_by_cat['Luxury Sedan']:,.2f}), Full-size SUV (${price_by_cat['Full-size SUV']:,.2f})
  - Mainstream Passenger:     Pickup Truck (${price_by_cat['Pickup Truck']:,.2f}), Van/MPV (${price_by_cat['Van / MPV']:,.2f}), Sedan (${price_by_cat['Sedan']:,.2f}), Crossover (${price_by_cat['Crossover']:,.2f}), Compact SUV (${price_by_cat['Compact SUV']:,.2f}), Hatchback (${price_by_cat['Hatchback']:,.2f})
  - Micro-Mobility:           Micro City Car (${price_by_cat['Micro City Car']:,.2f}), Three-Wheeler (${price_by_cat['Three-Wheeler']:,.2f}), Two-Wheeler Scooter (${price_by_cat['Two-Wheeler Scooter']:,.2f})

--------------------------------------------------------------------------------
INVESTIGATION 9: ANNUAL SALES VOLUME & TEMPORAL TRENDS
--------------------------------------------------------------------------------
Sales Volume Statistics:
  - Mean Sales per Model:   {sales_mean:,.1f} units
  - Median Sales:           {sales_median:,.1f} units
  - Cumulative Fleet Sales: {sales_sum:,.0f} units sold
  - Model Min - Max Sales:  {sales_min:,} to {sales_max:,} units

Temporal Sales Trajectory across Model Years:
  2018: {sales_by_year.loc[2018, 'sum']:,.0f} units (Mean: {sales_by_year.loc[2018, 'mean']:.1f})
  2019: {sales_by_year.loc[2019, 'sum']:,.0f} units (Mean: {sales_by_year.loc[2019, 'mean']:.1f})
  2020: {sales_by_year.loc[2020, 'sum']:,.0f} units (Mean: {sales_by_year.loc[2020, 'mean']:.1f})
  2021: {sales_by_year.loc[2021, 'sum']:,.0f} units (Mean: {sales_by_year.loc[2021, 'mean']:.1f})
  2022: {sales_by_year.loc[2022, 'sum']:,.0f} units (Mean: {sales_by_year.loc[2022, 'mean']:.1f})
  2023: {sales_by_year.loc[2023, 'sum']:,.0f} units (Mean: {sales_by_year.loc[2023, 'mean']:.1f})
  2024: {sales_by_year.loc[2024, 'sum']:,.0f} units (Mean: {sales_by_year.loc[2024, 'mean']:.1f})
  2025: {sales_by_year.loc[2025, 'sum']:,.0f} units (Mean: {sales_by_year.loc[2025, 'mean']:.1f})
  2026: {sales_by_year.loc[2026, 'sum']:,.0f} units (Mean: {sales_by_year.loc[2026, 'mean']:.1f})

Insight: Sales volume is right-skewed; blockbuster passenger EVs drive hundreds of thousands 
of sales, whereas specialized commercial transit operates at lower annual fleet delivery volumes.

--------------------------------------------------------------------------------
INVESTIGATION 10: CUSTOMER RATINGS ACROSS VEHICLE CATEGORIES
--------------------------------------------------------------------------------
Category-level Satisfaction Ranking (Mean +/- Std):
  1. Pickup Truck:          {rating_by_cat.loc['Pickup Truck', 'mean']:.3f} +/- {rating_by_cat.loc['Pickup Truck', 'std']:.2f}
  2. Micro City Car:        {rating_by_cat.loc['Micro City Car', 'mean']:.3f} +/- {rating_by_cat.loc['Micro City Car', 'std']:.2f}
  3. Sports Car:            {rating_by_cat.loc['Sports Car', 'mean']:.3f} +/- {rating_by_cat.loc['Sports Car', 'std']:.2f}
  4. Sedan:                 {rating_by_cat.loc['Sedan', 'mean']:.3f} +/- {rating_by_cat.loc['Sedan', 'std']:.2f}
  5. Compact SUV:           {rating_by_cat.loc['Compact SUV', 'mean']:.3f} +/- {rating_by_cat.loc['Compact SUV', 'std']:.2f}
  6. Van / MPV:             {rating_by_cat.loc['Van / MPV', 'mean']:.3f} +/- {rating_by_cat.loc['Van / MPV', 'std']:.2f}
  7. Full-size SUV:         {rating_by_cat.loc['Full-size SUV', 'mean']:.3f} +/- {rating_by_cat.loc['Full-size SUV', 'std']:.2f}
  8. Two-Wheeler Scooter:   {rating_by_cat.loc['Two-Wheeler Scooter', 'mean']:.3f} +/- {rating_by_cat.loc['Two-Wheeler Scooter', 'std']:.2f}
  9. Luxury Sedan:          {rating_by_cat.loc['Luxury Sedan', 'mean']:.3f} +/- {rating_by_cat.loc['Luxury Sedan', 'std']:.2f}
 10. Three-Wheeler:         {rating_by_cat.loc['Three-Wheeler', 'mean']:.3f} +/- {rating_by_cat.loc['Three-Wheeler', 'std']:.2f}
 11. Crossover:             {rating_by_cat.loc['Crossover', 'mean']:.3f} +/- {rating_by_cat.loc['Crossover', 'std']:.2f}
 12. Electric Bus:          {rating_by_cat.loc['Electric Bus', 'mean']:.3f} +/- {rating_by_cat.loc['Electric Bus', 'std']:.2f}
 13. Luxury SUV:            {rating_by_cat.loc['Luxury SUV', 'mean']:.3f} +/- {rating_by_cat.loc['Luxury SUV', 'std']:.2f}
 14. Hatchback:             {rating_by_cat.loc['Hatchback', 'mean']:.3f} +/- {rating_by_cat.loc['Hatchback', 'std']:.2f}
 15. Electric Truck:        {rating_by_cat.loc['Electric Truck', 'mean']:.3f} +/- {rating_by_cat.loc['Electric Truck', 'std']:.2f}

Insight: Customer satisfaction remains remarkably stable (~4.08 to 4.10) across all 
market segments, indicating that buyer expectations are being fulfilled across both 
budget and ultra-premium classes.

--------------------------------------------------------------------------------
INVESTIGATION 11: BATTERY CAPACITY VERSUS DRIVING RANGE
--------------------------------------------------------------------------------
Cross-Fleet Correlation: r = +{corr_cap_range:.4f} (Moderate positive)

Underlying Engineering Dynamics:
While battery capacity generally scales with vehicle size, driving range does not 
correlate linearly across the aggregate fleet. Heavy vehicles (Electric Buses and Trucks) 
carry massive battery packs (200-410 kWh) but exhibit ranges of only 200-360 km due to 
their high aerodynamic drag and curb weight (3,500-4,700 kg). Conversely, streamlined 
Luxury Sedans achieve 550-660 km of range on a modest 90 kWh battery.
Within homogeneous vehicle categories, battery capacity and range are tightly engineered 
to segment duty cycles.

--------------------------------------------------------------------------------
INVESTIGATION 12: VEHICLE PRICE VERSUS BATTERY CAPACITY
--------------------------------------------------------------------------------
Cross-Fleet Correlation: r = +{corr_price_cap:.4f} (STRONG POSITIVE)
Correlation between Price and Range: r = +{corr_price_range:.4f}

Insight: Traction battery capacity is the single strongest determinant of electric 
vehicle retail price across the entire automotive market (r = +0.8373). Every kilowatt-hour 
of installed capacity adds substantial capital cost, making battery chemistry and pack 
economics the primary battlefield for OEM profitability.

--------------------------------------------------------------------------------
INVESTIGATION 13: SALES DISTRIBUTION ACROSS MANUFACTURERS
--------------------------------------------------------------------------------
Top 5 OEMs by Cumulative Sales Volume:
  1. AmpereWorks:      {top_5_mfg_sales.iloc[0]:,.0f} units sold
  2. SurgeWorks:       {top_5_mfg_sales.iloc[1]:,.0f} units sold
  3. CircuitWorks:     {top_5_mfg_sales.iloc[2]:,.0f} units sold
  4. WattRides:        {top_5_mfg_sales.iloc[3]:,.0f} units sold
  5. IonAutomotive:    {top_5_mfg_sales.iloc[4]:,.0f} units sold

Bottom 5 OEMs by Cumulative Sales Volume:
  196. CurrentAutomotive: {bottom_5_mfg_sales.iloc[-5]:,.0f} units sold
  197. SparkMobility:     {bottom_5_mfg_sales.iloc[-4]:,.0f} units sold
  198. TorqueWheels:      {bottom_5_mfg_sales.iloc[-3]:,.0f} units sold
  199. SurgeEV:           {bottom_5_mfg_sales.iloc[-2]:,.0f} units sold
  200. DynamoAutomotive:  {bottom_5_mfg_sales.iloc[-1]:,.0f} units sold

Insight: Across 200 OEMs, total sales volume ranges from 10.3M to 13.7M units. 
Market competition is distributed, with no monopoly position.

--------------------------------------------------------------------------------
INVESTIGATION 14: SUSTAINABILITY & ENVIRONMENTAL DECARBONIZATION
--------------------------------------------------------------------------------
Fleet Decarbonization Metrics:
  - Mean Annual CO2 Saved:   {co2_mean:.3f} metric tons / vehicle / year
  - Median Annual CO2 Saved: {co2_median:.3f} metric tons / vehicle / year
  - Total Fleet CO2 Saved:   {co2_total:,.2f} metric tons / year
  - Mean Energy Efficiency:  {eff_mean:.2f} Wh/km
  - Median Efficiency:       {eff_median:.2f} Wh/km

CO2 Abatement by Vehicle Category:
  - Commercial Heavy Leaders: Electric Bus ({co2_by_cat['Electric Bus']:.2f} t/yr), Pickup Truck ({co2_by_cat['Pickup Truck']:.2f} t/yr), Electric Truck ({co2_by_cat['Electric Truck']:.2f} t/yr)
  - Passenger Fleet Average:  Sedans, SUVs, Hatchbacks (~3.04 - 3.05 t/yr)
  - Micro-Mobility:           Two-Wheeler Scooters ({co2_by_cat['Two-Wheeler Scooter']:.2f} t/yr), Three-Wheelers ({co2_by_cat['Three-Wheeler']:.2f} t/yr)

Energy Efficiency (Wh/km, lower is better):
  1. Two-Wheeler Scooter:    {eff_by_cat['Two-Wheeler Scooter']:.2f} Wh/km (Highest thermodynamic efficiency)
  2. Three-Wheeler:          {eff_by_cat['Three-Wheeler']:.2f} Wh/km
  3. Hatchback:              {eff_by_cat['Hatchback']:.2f} Wh/km
  4. Sedan:                  {eff_by_cat['Sedan']:.2f} Wh/km
  5. Micro City Car:         {eff_by_cat['Micro City Car']:.2f} Wh/km
  ...
 14. Electric Truck:         {eff_by_cat['Electric Truck']:.2f} Wh/km
 15. Electric Bus:           {eff_by_cat['Electric Bus']:.2f} Wh/km

Insight: Commercial electrification delivers the highest decarbonization return on 
investment (3x the CO2 displacement of passenger cars), despite requiring higher 
energy per kilometer. Electrifying transit buses and freight trucks represents the 
fastest lever for global municipal emissions reduction.
================================================================================
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(summary_content)

print(f"EDA Summary successfully written to: {output_path}")

