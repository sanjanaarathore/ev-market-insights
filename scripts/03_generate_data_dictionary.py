import os
import pandas as pd
import numpy as np
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

os.makedirs("deliverables", exist_ok=True)
excel_path = r"deliverables/tableau_data_dictionary.xlsx"

print("Creating Tableau Data Dictionary Excel Workbook...")

# Load cleaned dataset for exact statistics
df = pd.read_csv(r"cleaned_data/cleaned_ev_dataset.csv")

wb = openpyxl.Workbook()
# Remove default sheet
wb.remove(wb.active)

# Styles
font_title = Font(name="Calibri", size=16, bold=True, color="1F4E78")
font_subtitle = Font(name="Calibri", size=11, italic=True, color="595959")
font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
fill_header = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
fill_zebra = PatternFill(start_color="F2F5F8", end_color="F2F5F8", fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
align_right = Alignment(horizontal="right", vertical="center")

# ==============================================================================
# SHEET 1: Data Dictionary
# ==============================================================================
ws1 = wb.create_sheet(title="Data Dictionary")
ws1.views.sheetView[0].showGridLines = True

ws1.append(["ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS - TABLEAU DATA DICTIONARY"])
ws1["A1"].font = font_title
ws1.append(["Production Dataset Schema, Roles, Formats, and Tableau Visual Metadata | Phase 1 Unified Fleet (299,999 records)"])
ws1["A2"].font = font_subtitle
ws1.append([]) # Blank row

headers1 = [
    "Field Name", "Business / Display Name", "Logical Group", "Tableau Role",
    "Tableau Data Type", "Default Aggregation", "Description & Analytical Purpose",
    "Valid Range / Domain Values", "Imputation Method"
]
ws1.append(headers1)
header_row_idx = 4
for col_num in range(1, len(headers1) + 1):
    cell = ws1.cell(row=header_row_idx, column=col_num)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_center

data_dictionary_items = [
    ("vehicle_id", "Vehicle ID", "A. Vehicle Identification", "Dimension", "String", "Count (Distinct)", "Unique primary key identifier for every vehicle record.", "EV200000 to EV499999", "None (100% Unique)"),
    ("model_name", "Model Name", "A. Vehicle Identification", "Dimension", "String", "Count (Distinct)", "Commercial model branding and vehicle series code.", "17,980 unique model names", "None (Complete)"),
    ("manufacturer", "Manufacturer (OEM)", "B. Manufacturer Information", "Dimension", "String", "Count (Distinct)", "Automotive original equipment manufacturer company name.", "200 distinct OEMs (e.g. VoltWorks, AmpereGroup)", "None (Complete)"),
    ("model_year", "Model Year", "B. Manufacturer Information", "Dimension", "Date / Number (whole)", "None / Attribute", "Release year of vehicle manufacturing and model iteration.", "2018 to 2026", "None (Complete)"),
    ("manufacturing_country", "Manufacturing Country", "C. Geographic Information", "Dimension (Geographic)", "String (Country/Region)", "Count (Distinct)", "Sovereign nation where vehicle assembly took place.", "10 nations: China, France, Germany, India, Japan, South Korea, Sweden, UK, USA, Vietnam", "None (Complete)"),
    ("market_region", "Market Region", "C. Geographic Information", "Dimension", "String", "Count (Distinct)", "Target continental sales territory and retail distribution region.", "7 regions: Africa, Asia Pacific, Europe, Latin America, Middle East, North America, South Asia", "None (Complete)"),
    ("category", "Vehicle Category", "D. Vehicle Category", "Dimension", "String", "Count (Distinct)", "Structural automotive body style and functional classification.", "15 categories (Two-Wheeler Scooter, Sedan, Compact SUV, Electric Bus, etc.)", "None (Complete)"),
    ("recommended_use_case", "Recommended Use Case", "D. Vehicle Category", "Dimension", "String", "Count (Distinct)", "Primary intended operational deployment profile.", "7 profiles: Urban Commute, Family Daily Use, Highway / Long-Distance, etc.", "None (Complete)"),
    ("battery_capacity_kwh", "Battery Capacity (kWh)", "E. Battery Specifications", "Measure", "Number (decimal)", "Average / Sum", "Nominal energy capacity of high-voltage traction pack in kilowatt-hours.", "1.50 to 410.00 kWh", "None (Complete)"),
    ("battery_type", "Battery Chemistry", "E. Battery Specifications", "Dimension", "String", "Count (Distinct)", "Electrochemical composition of active cell material.", "5 types: NMC, LFP, NCA, Sodium-Ion, Solid-State", "None (Complete)"),
    ("battery_cycle_life", "Battery Cycle Life", "E. Battery Specifications", "Measure", "Number (whole)", "Average", "Rated full charge/discharge cycle count to 80% State of Health (SoH).", "500 to 4,640 cycles", "Imputed via Median by Battery Type"),
    ("battery_degradation_pct_5yr", "5-Yr Battery Degradation (%)", "E. Battery Specifications", "Measure", "Number (decimal)", "Average", "Projected cumulative capacity loss percentage over 5 operating years.", "2.00% to 36.89%", "None (Complete)"),
    ("range_km", "Certified Range (km)", "F. Vehicle Performance", "Measure", "Number (decimal)", "Average", "Full charge certified driving range in kilometers under standardized cycle.", "55.0 to 660.0 km", "None (Complete)"),
    ("efficiency_wh_per_km", "Energy Efficiency (Wh/km)", "F. Vehicle Performance", "Measure", "Number (decimal)", "Average", "Electrical consumption rate per kilometer traveled (lower is more efficient).", "9.89 to 2,261.41 Wh/km", "None (Complete)"),
    ("motor_power_kw", "Motor Power (kW)", "F. Vehicle Performance", "Measure", "Number (decimal)", "Average / Max", "Total combined peak powertrain motor mechanical output in kilowatts.", "1.5 to 750.0 kW", "None (Complete)"),
    ("torque_nm", "Torque (Nm)", "F. Vehicle Performance", "Measure", "Number (decimal)", "Average / Max", "Total combined peak rotational wheel torque in Newton-meters.", "20.0 to 4,000.0 Nm", "None (Complete)"),
    ("num_motors", "Number of Motors", "F. Vehicle Performance", "Dimension / Measure", "Number (whole)", "Average / Mode", "Quantity of electric traction drive units installed on the vehicle chassis.", "1, 2, or 3 motors", "None (Complete)"),
    ("drivetrain", "Drivetrain Configuration", "F. Vehicle Performance", "Dimension", "String", "Count (Distinct)", "Axle propulsion configuration: Front, Rear, or All-Wheel Drive.", "FWD, RWD, AWD", "None (Complete)"),
    ("top_speed_kmph", "Top Speed (km/h)", "F. Vehicle Performance", "Measure", "Number (decimal)", "Average / Max", "Maximum electronically governed or achievable road velocity.", "40.0 to 330.0 km/h", "None (Complete)"),
    ("acceleration_0_100_sec", "0-100 km/h Time (s)", "F. Vehicle Performance", "Measure", "Number (decimal)", "Average / Min", "Elapsed sprint duration in seconds from standstill to 100 km/h.", "1.90 to 30.00 seconds", "None (Complete)"),
    ("weight_kg", "Curb Weight (kg)", "F. Vehicle Performance", "Measure", "Number (decimal)", "Average", "Unladen structural curb weight of the fully equipped vehicle in kilograms.", "215.7 to 4,696.2 kg", "None (Complete)"),
    ("num_seats", "Seating Capacity", "F. Vehicle Performance", "Dimension / Measure", "Number (whole)", "Average / Mode", "Total certified seating accommodation capacity for passengers and driver.", "1 to 65 seats", "None (Complete)"),
    ("cargo_capacity_liters", "Cargo Volume (L)", "F. Vehicle Performance", "Measure", "Number (decimal)", "Average", "Total enclosed luggage and trunk storage cargo volume in liters.", "15.0 to 2,001.5 liters", "None (Complete)"),
    ("max_dc_charging_kw", "Max DC Charge Power (kW)", "G. Charging Specifications", "Measure", "Number (decimal)", "Average / Max", "Peak acceptable Direct Current fast-charge power intake rate.", "3.0 to 350.0 kW", "None (Complete)"),
    ("charging_dc_fast_time_min", "DC Fast Charge Time (min)", "G. Charging Specifications", "Measure", "Number (decimal)", "Average", "Elapsed duration in minutes required for a 20% to 80% DC fast charge.", "8.0 to 59.6 minutes", "None (Complete)"),
    ("charging_ac_time_hr", "AC Charging Time (hr)", "G. Charging Specifications", "Measure", "Number (decimal)", "Average", "Duration in hours for a full Level 2 AC recharge from zero to 100%.", "0.30 to 30.00 hours", "None (Complete)"),
    ("num_charging_ports", "Number of Charging Ports", "G. Charging Specifications", "Dimension / Measure", "Number (whole)", "Mode", "Physical external plug receptacles available on vehicle body.", "1 or 2 ports", "None (Complete)"),
    ("price_usd", "Retail Price (USD)", "H. Pricing and Ownership", "Measure", "Number (decimal)", "Average / Median", "Manufacturer Suggested Retail Price (MSRP) baseline price in US Dollars.", "$900.04 to $409,995.49", "None (Complete)"),
    ("insurance_cost_usd_yearly", "Annual Insurance Cost (USD)", "H. Pricing and Ownership", "Measure", "Number (decimal)", "Average", "Estimated comprehensive annual vehicle insurance policy premium.", "$40.00 to $12,000.00", "None (Complete)"),
    ("warranty_years", "Warranty Coverage (Years)", "H. Pricing and Ownership", "Dimension / Measure", "Number (whole)", "Average", "Manufacturer warranty protection duration for powertrain and battery.", "2 to 8 years", "None (Complete)"),
    ("resale_value_pct_3yr", "3-Year Resale Value (%)", "H. Pricing and Ownership", "Measure", "Number (decimal)", "Average", "Projected secondary market retained residual value percentage after 3 years.", "15.00% to 90.00%", "Imputed via Median by Category"),
    ("safety_rating_stars", "Crash Safety Stars", "I. Safety and Technology", "Dimension / Measure", "Number (whole)", "Average", "Standardized vehicle occupant collision and active safety star rating.", "1 to 5 stars", "None (Complete)"),
    ("autonomous_level", "Autonomous Driving Level", "I. Safety and Technology", "Dimension", "Number (whole)", "Average / Mode", "SAE J3016 standardized automated driving autonomy capability level.", "0 to 5 (Level 0: None, Level 5: Full)", "None (Complete)"),
    ("infotainment_screen_inch", "Screen Size (Inches)", "I. Safety and Technology", "Measure", "Number (decimal)", "Average", "Central cockpit digital infotainment visual display diagonal size.", "3.0 to 17.0 inches", "Imputed via Median by Category"),
    ("co2_saved_tons_per_year", "CO2 Avoided (Tons/Year)", "J. Environmental Metrics", "Measure", "Number (decimal)", "Sum / Average", "Estimated metric tons of greenhouse gas emissions eliminated annually vs ICE.", "0.950 to 13.300 tons/yr", "None (Complete)"),
    ("annual_sales_units", "Annual Sales (Units)", "K. Sales and Customer Satisfaction", "Measure", "Number (whole)", "Sum / Average", "Annual retail unit sales volume recorded for the given vehicle model.", "9 to 1,066,612 units", "Imputed via Median by Category"),
    ("customer_rating", "Customer Satisfaction Rating", "K. Sales and Customer Satisfaction", "Measure", "Number (decimal)", "Average", "Aggregated consumer survey satisfaction index score on a 1 to 5 scale.", "1.52 to 5.00 / 5.0", "Imputed via Median by Category"),
    ("source_split", "Data Source Split", "Provenance", "Dimension", "String", "Count", "Designates source dataset partition provenance for validation filtering.", "Train (199,999) or Test (100,000)", "Engineered Provenance Flag")
]

for row_idx, item in enumerate(data_dictionary_items, start=5):
    ws1.append(list(item))
    for col_idx in range(1, len(item) + 1):
        c = ws1.cell(row=row_idx, column=col_idx)
        c.font = Font(name="Calibri", size=10)
        c.border = thin_border
        if col_idx in [1, 2, 7, 8, 9]:
            c.alignment = align_left
        elif col_idx in [3, 4, 5, 6]:
            c.alignment = align_center
        if row_idx % 2 == 0:
            c.fill = fill_zebra

# Set auto column widths
for col in ws1.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws1.column_dimensions[col_letter].width = max(max_len + 3, 12)
ws1.column_dimensions["A"].width = 24
ws1.column_dimensions["B"].width = 26
ws1.column_dimensions["C"].width = 24
ws1.column_dimensions["G"].width = 45
ws1.column_dimensions["H"].width = 30
ws1.column_dimensions["I"].width = 32

# ==============================================================================
# SHEET 2: Category Taxonomy
# ==============================================================================
ws2 = wb.create_sheet(title="Category Taxonomy")
ws2.views.sheetView[0].showGridLines = True

ws2.append(["ELECTRIC VEHICLE CATEGORY TAXONOMY & OPERATIONAL PROFILES"])
ws2["A1"].font = font_title
ws2.append(["Multi-Segment Automotive Benchmarking Matrix | Cleaned Fleet (299,999 records)"])
ws2["A2"].font = font_subtitle
ws2.append([])

headers2 = [
    "Vehicle Category", "Fleet Count", "Market Share (%)", "Typical Seats",
    "Avg Battery (kWh)", "Avg Range (km)", "Avg Price ($)", "Avg Efficiency (Wh/km)",
    "Avg Annual CO2 Saved (Tons)", "Primary Use Case"
]
ws2.append(headers2)
for col_num in range(1, len(headers2) + 1):
    cell = ws2.cell(row=4, column=col_num)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_center

cat_summary = df.groupby('category').agg({
    'vehicle_id': 'count',
    'num_seats': lambda x: f"{x.min()}-{x.max()}",
    'battery_capacity_kwh': 'mean',
    'range_km': 'mean',
    'price_usd': 'mean',
    'efficiency_wh_per_km': 'mean',
    'co2_saved_tons_per_year': 'mean',
    'recommended_use_case': lambda x: x.mode().iloc[0]
}).reset_index()

cat_summary['share'] = (cat_summary['vehicle_id'] / len(df) * 100).round(2)
cat_summary = cat_summary.sort_values(by='vehicle_id', ascending=False)

for r_idx, (_, row) in enumerate(cat_summary.iterrows(), start=5):
    row_vals = [
        row['category'],
        int(row['vehicle_id']),
        row['share'],
        row['num_seats'],
        round(row['battery_capacity_kwh'], 1),
        round(row['range_km'], 1),
        round(row['price_usd'], 2),
        round(row['efficiency_wh_per_km'], 1),
        round(row['co2_saved_tons_per_year'], 2),
        row['recommended_use_case']
    ]
    ws2.append(row_vals)
    for c_idx in range(1, len(row_vals) + 1):
        c = ws2.cell(row=r_idx, column=c_idx)
        c.font = Font(name="Calibri", size=10)
        c.border = thin_border
        if c_idx in [2, 3, 5, 6, 7, 8, 9]:
            c.alignment = align_right
        elif c_idx == 4:
            c.alignment = align_center
        else:
            c.alignment = align_left
        if r_idx % 2 == 0:
            c.fill = fill_zebra

for col in ws2.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws2.column_dimensions[col_letter].width = max(max_len + 3, 14)

# ==============================================================================
# SHEET 3: Summary Statistics
# ==============================================================================
ws3 = wb.create_sheet(title="Summary Statistics")
ws3.views.sheetView[0].showGridLines = True

ws3.append(["PARAMETRIC STATISTICAL SUMMARY FOR ALL NUMERICAL ATTRIBUTES"])
ws3["A1"].font = font_title
ws3.append(["Calculated Directly Across Complete Cleaned Fleet (299,999 records)"])
ws3["A2"].font = font_subtitle
ws3.append([])

headers3 = [
    "Numerical Measure", "Data Type", "Count", "Minimum", "25th Pct",
    "Median (50th)", "Mean", "75th Pct", "Maximum", "Std Deviation", "IQR"
]
ws3.append(headers3)
for col_num in range(1, len(headers3) + 1):
    cell = ws3.cell(row=4, column=col_num)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_center

num_cols_list = df.select_dtypes(include=[np.number]).columns.tolist()
for r_idx, col in enumerate(num_cols_list, start=5):
    ser = df[col]
    q25 = ser.quantile(0.25)
    q75 = ser.quantile(0.75)
    row_stat = [
        col,
        str(ser.dtype),
        int(ser.count()),
        round(float(ser.min()), 2),
        round(float(q25), 2),
        round(float(ser.median()), 2),
        round(float(ser.mean()), 2),
        round(float(q75), 2),
        round(float(ser.max()), 2),
        round(float(ser.std()), 2),
        round(float(q75 - q25), 2)
    ]
    ws3.append(row_stat)
    for c_idx in range(1, len(row_stat) + 1):
        c = ws3.cell(row=r_idx, column=c_idx)
        c.font = Font(name="Calibri", size=10)
        c.border = thin_border
        if c_idx > 2:
            c.alignment = align_right
        elif c_idx == 2:
            c.alignment = align_center
        else:
            c.alignment = align_left
        if r_idx % 2 == 0:
            c.fill = fill_zebra

for col in ws3.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws3.column_dimensions[col_letter].width = max(max_len + 3, 14)

# ==============================================================================
# SHEET 4: Tableau Implementation Guide
# ==============================================================================
ws4 = wb.create_sheet(title="Tableau Guide & Calcs")
ws4.views.sheetView[0].showGridLines = True

ws4.append(["TABLEAU IMPLEMENTATION BEST PRACTICES & RECOMMENDED CALCULATED FIELDS"])
ws4["A1"].font = font_title
ws4.append(["Ready-to-use Tableau Formulas, Parameter Controls, and Dashboard Blueprints for Phase 2"])
ws4["A2"].font = font_subtitle
ws4.append([])

headers4 = [
    "Calculation Name", "Tableau Formula Syntax", "Business Purpose / KPI Definition", "Recommended Chart Type"
]
ws4.append(headers4)
for col_num in range(1, len(headers4) + 1):
    cell = ws4.cell(row=4, column=col_num)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_center

calc_fields = [
    ("Cost per km Range ($/km)", "[price_usd] / [range_km]", "Measures consumer economic value and capital cost per unit of certified driving range.", "Scatter Plot vs Category"),
    ("Total Model Revenue ($)", "[annual_sales_units] * [price_usd]", "Computes global annual gross revenue generated by each model and OEM.", "Treemap / Ranked Bar Chart"),
    ("Pack Specific Energy (Wh/kg)", "([battery_capacity_kwh] * 1000) / [weight_kg]", "Evaluates gravimetric battery powertrain integration efficiency.", "Box Plot by Battery Type"),
    ("Fleet CO2 Abatement (Tons)", "[annual_sales_units] * [co2_saved_tons_per_year]", "Gross annual decarbonization impact achieved by active vehicle sales volume.", "Choropleth Map / KPI Card"),
    ("Efficiency Tier", 'IF [efficiency_wh_per_km] < 100 THEN "Ultra-Efficient (<100 Wh/km)" ELSEIF [efficiency_wh_per_km] < 200 THEN "Standard Passenger (100-200 Wh/km)" ELSEIF [efficiency_wh_per_km] < 350 THEN "Heavy Passenger (200-350 Wh/km)" ELSE "Commercial Heavy-Duty (>350 Wh/km)" END', "Categorizes fleet into energy consumption tiers for policy analysis.", "Donut Chart / Filter Dimension"),
    ("Charging Speed Tier", 'IF [max_dc_charging_kw] >= 250 THEN "Ultra-Fast (>=250 kW)" ELSEIF [max_dc_charging_kw] >= 100 THEN "Fast (100-249 kW)" ELSEIF [max_dc_charging_kw] >= 50 THEN "Rapid (50-99 kW)" ELSE "Standard (<50 kW)" END', "Classifies charging performance compatibility with high-power highway corridors.", "Stacked Bar Chart"),
    ("Resale Value Tier", 'IF [resale_value_pct_3yr] >= 60 THEN "High Retained Value (>=60%)" ELSEIF [resale_value_pct_3yr] >= 45 THEN "Average Retained Value (45-59%)" ELSE "Accelerated Depreciation (<45%)" END', "Evaluates commercial residual value risk and fleet leasing attractiveness.", "Heat Map Matrix"),
    ("Satisfaction Index", 'IF [customer_rating] >= 4.5 THEN "Delighted (4.5-5.0)" ELSEIF [customer_rating] >= 4.0 THEN "Satisfied (4.0-4.49)" ELSE "Needs Improvement (<4.0)" END', "Segments customer feedback for OEM product engineering teams.", "Bullet Chart / Diverging Bar")
]

for r_idx, item in enumerate(calc_fields, start=5):
    ws4.append(list(item))
    for c_idx in range(1, len(item) + 1):
        c = ws4.cell(row=r_idx, column=c_idx)
        c.font = Font(name="Calibri", size=10)
        c.border = thin_border
        c.alignment = align_left
        if r_idx % 2 == 0:
            c.fill = fill_zebra

for col in ws4.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws4.column_dimensions[col_letter].width = max(max_len + 3, 16)
ws4.column_dimensions["A"].width = 28
ws4.column_dimensions["B"].width = 45
ws4.column_dimensions["C"].width = 48
ws4.column_dimensions["D"].width = 30

wb.save(excel_path)
print(f"Tableau Data Dictionary successfully saved to: {excel_path}")
