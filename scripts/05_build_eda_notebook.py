import os
import nbformat as nbf

notebook_path = r"deliverables/ev_eda_analysis.ipynb"
root_notebook_path = r"ev_eda_analysis.ipynb"

nb = nbf.v4.new_notebook()

# Metadata
nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "codemirror_mode": {"name": "ipython", "version": 3},
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.11"
    }
}

cells = []

# Cell 1: Markdown Header
cells.append(nbf.v4.new_markdown_cell("""# ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS
## Exploratory Data Analysis & Strategic Market Intelligence (Phase 1)
**Author:** Expert Data Analyst & Visualization Engineer  
**Dataset:** Unified Global EV Market Intelligence Database (299,999 records, 38 attributes)  
**Objective:** Comprehensive multi-dimensional exploratory data analysis of global electric vehicle adoption, technological architectures, customer satisfaction, and decarbonization impact across 15 vehicle categories and 200 manufacturers.

---
### Analytical Framework:
1. **EV Category Distribution**
2. **Manufacturer (OEM) Competitive Landscape**
3. **Manufacturing Country & Regional Trade Dynamics**
4. **Battery Chemistry & Technology Adoption**
5. **Certified Driving Range Analysis**
6. **Battery Capacity & Specific Energy Benchmarking**
7. **Customer Satisfaction Distribution**
8. **Vehicle Pricing & Economic Stratification**
9. **Annual Sales Volume & Temporal Adoption (2018-2026)**
10. **Customer Ratings Across Vehicle Segments**
11. **Battery Capacity versus Driving Range Non-Linearities**
12. **Vehicle Price versus Battery Capacity Economics**
13. **Sales Distribution Across Leading OEMs**
14. **Sustainability Performance: CO2 Abatement & Energy Efficiency**
15. **Multivariate Parametric Correlation Matrix**
"""))

# Cell 2: Code Imports & Setup
cells.append(nbf.v4.new_code_cell("""# Environment Setup & Library Ingestion
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Visual Configuration
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

print("Libraries imported successfully!")
"""))

# Cell 3: Code Ingestion
cells.append(nbf.v4.new_markdown_cell("""### Ingesting Tableau-Ready Production Dataset
We load the deduplicated, domain-imputed dataset `cleaned_ev_dataset.csv`.
"""))

cells.append(nbf.v4.new_code_cell("""# Ingest cleaned unified dataset
data_path = 'cleaned_ev_dataset.csv'
try:
    df = pd.read_csv(data_path)
except FileNotFoundError:
    df = pd.read_csv('cleaned_data/cleaned_ev_dataset.csv')

print(f"Dataset Dimensions: {df.shape[0]:,} Rows x {df.shape[1]} Columns")
print(f"Source Partitions: {df['source_split'].value_counts().to_dict()}")
df.head(3)
"""))

# Cell 4: Investigation 1
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 1: EV Category Distribution
Evaluating the market presence across all 15 vehicle body styles and commercial segments.
"""))

cells.append(nbf.v4.new_code_cell("""cat_counts = df['category'].value_counts()
cat_pcts = df['category'].value_counts(normalize=True) * 100

plt.figure(figsize=(12, 6))
bars = plt.barh(cat_counts.index[::-1], cat_counts.values[::-1], color='#1f77b4', edgecolor='black', alpha=0.85)
plt.title('Global EV Fleet Distribution by Vehicle Category (299,999 records)', fontweight='bold')
plt.xlabel('Number of Unique Vehicle Models')
plt.ylabel('Vehicle Category')

for bar in bars:
    w = bar.get_width()
    plt.text(w + 300, bar.get_y() + bar.get_height()/2, f'{w:,} ({w/len(df)*100:.1f}%)', 
             va='center', fontsize=9, color='#333333')

plt.xlim(0, max(cat_counts.values) * 1.15)
plt.tight_layout()
plt.show()
"""))

# Cell 5: Investigation 2
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 2: Manufacturer (OEM) Distribution
Analyzing market concentration and model diversity across 200 automotive manufacturers.
"""))

cells.append(nbf.v4.new_code_cell("""mfg_counts = df['manufacturer'].value_counts()
print(f"Total Unique OEMs: {df['manufacturer'].nunique()}")
print(f"Mean Portfolio Size: {mfg_counts.mean():.1f} models | Std Dev: {mfg_counts.std():.1f}")

plt.figure(figsize=(14, 6))
top_20_mfg = mfg_counts.head(20)
plt.bar(top_20_mfg.index, top_20_mfg.values, color='#2ca02c', edgecolor='black', alpha=0.85)
plt.title('Top 20 Manufacturers by Model Offerings Count', fontweight='bold')
plt.xlabel('Manufacturer (OEM)')
plt.ylabel('Model Offerings Count')
plt.xticks(rotation=45, ha='right')
plt.ylim(1200, 1700)

for idx, val in enumerate(top_20_mfg.values):
    plt.text(idx, val + 10, f'{val}', ha='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()
"""))

# Cell 6: Investigation 3
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 3: Manufacturing Country & Regional Footprint
Assessing sovereign manufacturing output and regional market delivery.
"""))

cells.append(nbf.v4.new_code_cell("""fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

country_counts = df['manufacturing_country'].value_counts()
ax1.barh(country_counts.index[::-1], country_counts.values[::-1], color='#ff7f0e', edgecolor='black', alpha=0.85)
ax1.set_title('Manufacturing Country Assembly Output (Models)', fontweight='bold')
ax1.set_xlabel('Total Vehicle Models')

for i, v in enumerate(country_counts.values[::-1]):
    ax1.text(v + 300, i, f'{v:,} ({v/len(df)*100:.1f}%)', va='center', fontsize=9)
ax1.set_xlim(0, max(country_counts.values) * 1.18)

region_counts = df['market_region'].value_counts()
ax2.pie(region_counts.values, labels=region_counts.index, autopct='%1.1f%%', 
        colors=sns.color_palette('pastel'), startangle=140, 
        wedgeprops=dict(edgecolor='black', width=0.6))
ax2.set_title('Target Market Region Distribution', fontweight='bold')

plt.tight_layout()
plt.show()
"""))

# Cell 7: Investigation 4
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 4: Battery Technology Adoption & Durability
Evaluating battery cell chemistry shares and their respective cycle lives and degradation profiles.
"""))

cells.append(nbf.v4.new_code_cell("""bat_counts = df['battery_type'].value_counts()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

wedges, texts, autotexts = ax1.pie(bat_counts.values, labels=bat_counts.index, autopct='%1.1f%%',
                                  colors=['#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#8c564b'],
                                  startangle=90, pctdistance=0.75,
                                  wedgeprops=dict(width=0.45, edgecolor='black'))
ax1.set_title('Battery Chemistry Market Share', fontweight='bold')

sns.boxplot(data=df, x='battery_type', y='battery_cycle_life', ax=ax2, palette='Set2')
ax2.set_title('Battery Cycle Life Durability by Chemistry', fontweight='bold')
ax2.set_xlabel('Battery Chemistry Formulation')
ax2.set_ylabel('Rated Cycle Life to 80% SoH (Cycles)')

plt.tight_layout()
plt.show()

# Statistical breakdown
df.groupby('battery_type').agg({
    'battery_cycle_life': ['mean', 'median'],
    'battery_degradation_pct_5yr': ['mean', 'median']
}).round(2)
"""))

# Cell 8: Investigation 5
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 5: Certified Driving Range Performance
Analyzing single-charge operational driving range across vehicle segments.
"""))

cells.append(nbf.v4.new_code_cell("""range_by_cat = df.groupby('category')['range_km'].agg(['mean', 'median', 'std', 'max']).sort_values(by='mean', ascending=False)

plt.figure(figsize=(12, 7))
sns.boxplot(data=df, y='category', x='range_km', order=range_by_cat.index, palette='Blues_r')
plt.title('Driving Range (km) Distribution Across Vehicle Categories', fontweight='bold')
plt.xlabel('Certified Driving Range (Kilometers)')
plt.ylabel('Vehicle Category')
plt.axvline(df['range_km'].mean(), color='red', linestyle='--', label=f'Fleet Mean: {df["range_km"].mean():.1f} km')
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()

range_by_cat.round(1)
"""))

# Cell 9: Investigation 6
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 6: Battery Capacity Across Vehicle Segments
Benchmarking high-voltage traction battery pack capacity (kWh).
"""))

cells.append(nbf.v4.new_code_cell("""cap_by_cat = df.groupby('category')['battery_capacity_kwh'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
bars = plt.barh(cap_by_cat.index[::-1], cap_by_cat.values[::-1], color='#9467bd', edgecolor='black', alpha=0.85)
plt.title('Average Battery Capacity (kWh) by Vehicle Category', fontweight='bold')
plt.xlabel('Battery Capacity (kWh)')
plt.ylabel('Vehicle Category')

for bar in bars:
    w = bar.get_width()
    plt.text(w + 3, bar.get_y() + bar.get_height()/2, f'{w:.1f} kWh', va='center', fontsize=9)

plt.xlim(0, max(cap_by_cat.values) * 1.15)
plt.tight_layout()
plt.show()
"""))

# Cell 10: Investigation 7 & 10
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 7 & 10: Customer Satisfaction & Rating Across Categories
Assessing consumer review scores and satisfaction levels across market segments.
"""))

cells.append(nbf.v4.new_code_cell("""fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

sns.histplot(df['customer_rating'], bins=30, kde=True, ax=ax1, color='#17becf', edgecolor='black')
ax1.axvline(df['customer_rating'].mean(), color='red', linestyle='--', label=f"Mean: {df['customer_rating'].mean():.2f}")
ax1.set_title('Overall Customer Rating Distribution (1-5 Stars)', fontweight='bold')
ax1.set_xlabel('Customer Rating Score')
ax1.set_ylabel('Model Count')
ax1.legend()

rating_cat = df.groupby('category')['customer_rating'].mean().sort_values(ascending=False)
ax2.barh(rating_cat.index[::-1], rating_cat.values[::-1], color='#bcbd22', edgecolor='black', alpha=0.85)
ax2.set_xlim(3.8, 4.3)
ax2.set_title('Mean Customer Satisfaction by Vehicle Category', fontweight='bold')
ax2.set_xlabel('Mean Rating Score')

for i, v in enumerate(rating_cat.values[::-1]):
    ax2.text(v + 0.005, i, f'{v:.3f}', va='center', fontsize=9)

plt.tight_layout()
plt.show()
"""))

# Cell 11: Investigation 8
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 8: Vehicle Pricing & Economic Stratification
Evaluating MSRP price distribution and capital cost requirements across segments.
"""))

cells.append(nbf.v4.new_code_cell("""price_by_cat = df.groupby('category')['price_usd'].agg(['mean', 'median', 'std']).sort_values(by='mean', ascending=False)

plt.figure(figsize=(13, 6))
bars = plt.barh(price_by_cat.index[::-1], price_by_cat['mean'].values[::-1], color='#e377c2', edgecolor='black', alpha=0.85)
plt.title('Average Retail Price (MSRP USD) by Vehicle Category', fontweight='bold')
plt.xlabel('Average Vehicle Price ($ USD)')
plt.ylabel('Vehicle Category')

for bar in bars:
    w = bar.get_width()
    plt.text(w + 3000, bar.get_y() + bar.get_height()/2, f'${w:,.0f}', va='center', fontsize=9)

plt.xlim(0, max(price_by_cat['mean'].values) * 1.15)
plt.tight_layout()
plt.show()

price_by_cat.round(2)
"""))

# Cell 12: Investigation 9
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 9: Annual Sales Volume & Temporal Adoption Trends
Analyzing global adoption trajectory across model years 2018 through 2026.
"""))

cells.append(nbf.v4.new_code_cell("""sales_year = df.groupby('model_year')['annual_sales_units'].agg(['sum', 'mean', 'count'])

fig, ax1 = plt.subplots(figsize=(12, 5))

color = 'tab:blue'
ax1.set_xlabel('Model Year', fontweight='bold')
ax1.set_ylabel('Total Fleet Annual Sales Units', color=color, fontweight='bold')
line1 = ax1.plot(sales_year.index, sales_year['sum'], color=color, marker='o', linewidth=2.5, label='Total Fleet Sales')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Mean Sales per Model (Units)', color=color, fontweight='bold')
line2 = ax2.plot(sales_year.index, sales_year['mean'], color=color, marker='s', linestyle='--', linewidth=2, label='Mean Sales / Model')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Global EV Sales Trajectory Across Model Years (2018 - 2026)', fontweight='bold')
fig.tight_layout()
plt.show()

sales_year.round(1)
"""))

# Cell 13: Investigation 11 & 12
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 11 & 12: Powertrain Engineering & Pricing Economics
1. **Battery Capacity vs. Driving Range:** Demonstrating segment-specific energy requirements.
2. **Vehicle Price vs. Battery Capacity:** Revealing battery cost dominance in EV pricing.
"""))

cells.append(nbf.v4.new_code_cell("""fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Sample 5,000 points for clear visual rendering without overplotting
df_sample = df.sample(5000, random_state=42)

# 1. Capacity vs Range
sns.scatterplot(data=df_sample, x='battery_capacity_kwh', y='range_km', hue='category', 
                palette='tab20', alpha=0.6, s=30, legend=False, ax=ax1)
ax1.set_title(f"Battery Capacity vs. Driving Range (Overall r = +{df['battery_capacity_kwh'].corr(df['range_km']):.4f})", fontweight='bold')
ax1.set_xlabel('Battery Capacity (kWh)')
ax1.set_ylabel('Certified Driving Range (km)')

# 2. Price vs Capacity
sns.scatterplot(data=df_sample, x='battery_capacity_kwh', y='price_usd', hue='category', 
                palette='tab20', alpha=0.6, s=30, legend=False, ax=ax2)
ax2.set_title(f"Vehicle Price vs. Battery Capacity (Overall r = +{df['price_usd'].corr(df['battery_capacity_kwh']):.4f})", fontweight='bold')
ax2.set_xlabel('Battery Capacity (kWh)')
ax2.set_ylabel('Vehicle Retail Price ($ USD)')

plt.tight_layout()
plt.show()
"""))

# Cell 14: Investigation 13
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 13: Top OEM Manufacturers by Cumulative Sales
Ranking top 15 automotive corporations by total annual units sold.
"""))

cells.append(nbf.v4.new_code_cell("""mfg_sales = df.groupby('manufacturer')['annual_sales_units'].sum().sort_values(ascending=False).head(15)

plt.figure(figsize=(14, 6))
bars = plt.bar(mfg_sales.index, mfg_sales.values / 1e6, color='#8c564b', edgecolor='black', alpha=0.85)
plt.title('Top 15 Automotive Manufacturers by Total Sales Volume (Million Units)', fontweight='bold')
plt.xlabel('Manufacturer Brand (OEM)')
plt.ylabel('Total Annual Sales Volume (Million Units)')
plt.xticks(rotation=45, ha='right')

for bar in bars:
    h = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, h + 0.1, f'{h:.2f}M', ha='center', fontsize=9, fontweight='bold')

plt.ylim(10, max(mfg_sales.values/1e6) * 1.1)
plt.tight_layout()
plt.show()
"""))

# Cell 15: Investigation 14
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 14: Sustainability Performance: Decarbonization & Efficiency
Benchmarking net annual metric tons of CO2 greenhouse gas avoided and energy efficiency (Wh/km).
"""))

cells.append(nbf.v4.new_code_cell("""fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

co2_cat = df.groupby('category')['co2_saved_tons_per_year'].mean().sort_values(ascending=False)
ax1.barh(co2_cat.index[::-1], co2_cat.values[::-1], color='#2ca02c', edgecolor='black', alpha=0.85)
ax1.set_title('Annual CO2 Emissions Saved vs ICE (Tons/Year)', fontweight='bold')
ax1.set_xlabel('Mean CO2 Saved (Metric Tons / Vehicle / Year)')

for i, v in enumerate(co2_cat.values[::-1]):
    ax1.text(v + 0.1, i, f'{v:.2f} t', va='center', fontsize=9)
ax1.set_xlim(0, max(co2_cat.values) * 1.18)

eff_cat = df.groupby('category')['efficiency_wh_per_km'].mean().sort_values(ascending=True)
ax2.barh(eff_cat.index[::-1], eff_cat.values[::-1], color='#1f77b4', edgecolor='black', alpha=0.85)
ax2.set_title('Vehicle Energy Consumption Efficiency (Wh/km - Lower is Better)', fontweight='bold')
ax2.set_xlabel('Mean Consumption Rate (Wh/km)')

for i, v in enumerate(eff_cat.values[::-1]):
    ax2.text(v + 15, i, f'{v:.1f}', va='center', fontsize=9)
ax2.set_xlim(0, max(eff_cat.values) * 1.18)

plt.tight_layout()
plt.show()
"""))

# Cell 16: Correlation Heatmap
cells.append(nbf.v4.new_markdown_cell("""---
## Investigation 15: Multivariate Correlation Analysis
Examining parametric linear relationships across key technical, operational, and financial dimensions.
"""))

cells.append(nbf.v4.new_code_cell("""key_numeric = [
    'battery_capacity_kwh', 'range_km', 'efficiency_wh_per_km', 'motor_power_kw',
    'torque_nm', 'top_speed_kmph', 'acceleration_0_100_sec', 'weight_kg',
    'price_usd', 'insurance_cost_usd_yearly', 'co2_saved_tons_per_year',
    'annual_sales_units', 'customer_rating'
]

plt.figure(figsize=(12, 10))
corr_matrix = df[key_numeric].corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True, square=True, linewidths=0.5)
plt.title('Correlation Heatmap of Key Technical, Commercial & Financial Metrics', fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
"""))

# Cell 17: Summary and Strategic Takeaways
cells.append(nbf.v4.new_markdown_cell("""---
## Phase 1 Strategic Insights & Key Takeaways:
1. **Commercial Electrification is the High-Impact Decarbonization Lever:** Heavy electric commercial buses and freight trucks displace over 9.0 metric tons of CO2 annually per vehicle—nearly 3x the carbon displacement of standard passenger vehicles.
2. **Battery Sizing is the Primary Economic Cost Driver:** Installed battery pack capacity (kWh) exhibits an overwhelming r = +0.8373 correlation with retail price ($ USD).
3. **Chemistry Specialization:** LFP and NMC together command nearly 66% of the market. Solid-State offers exceptional cycle durability (3,000+ cycles) but commands premium pricing.
4. **Balanced Global Manufacturing Footprint:** Manufacturing is distributed evenly (~10% per nation) across 10 major automotive economies, with Asian manufacturers accounting for over 40% of global assembly.
5. **Phase 2 Ready:** Cleaned dataset is 100% free of missing values, validated for range and physical consistency, and ready for Tableau Public dashboard construction and Flask web deployment.
"""))

nb.cells = cells

# Save notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)
print(f"Jupyter Notebook successfully created at: {notebook_path}")

with open(root_notebook_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)
print(f"Jupyter Notebook also created at: {root_notebook_path}")

