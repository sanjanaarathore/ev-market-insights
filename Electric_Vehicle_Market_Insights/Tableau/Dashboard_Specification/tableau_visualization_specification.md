# TABLEAU VISUALIZATION SPECIFICATION
## ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS (PHASE 2)

**Document ID:** TVS-EV-2026-PH2  
**Target Platform:** Tableau Public / Tableau Desktop (2020.4 or newer, verified on Tableau Public 2026.3)  
**Primary Dataset:** `cleaned_ev_dataset.csv` (299,999 records, 38 columns)  
**Calculated Field Policy:** Strict adherence to project requirements—utilize native dataset fields directly wherever possible; avoid unnecessary calculated fields.

---

## 1. Data Source Connection & Tableau Environment Setup

1. **Launch Tableau Desktop / Tableau Public.**
2. **Connect to Data:** Select **Text file** -> navigate to and select `cleaned_ev_dataset.csv`.
3. **Data Source Verification:**
   * Total Rows: `299,999`
   * Field Count: `38` fields
   * Geographic Role Assignment: Ensure `manufacturing_country` is assigned the Geographic Role: **Country/Region**.
   * Date/Time Role Assignment: Ensure `model_year` can be used as a discrete dimension or integer.
4. **Data Extract:** In Tableau Desktop/Public, ensure the connection is set to **Extract** (hyper format) for maximum interactivity speed across 300,000 rows.

---

## 2. KPI Cards Technical Specifications

The dashboard header features a dedicated 6-KPI Summary Banner.

```
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|  TOTAL EV MODELS  |TOTAL MANUFACTURERS|AVG CUSTOMER RATING|AVG DRIVING RANGE  |AVG BATTERY CAP.   |TOTAL ANNUAL SALES |
|  299,999 Records  |      200 OEMs     |     4.09 / 5.0    |     324.5 km      |     78.2 kWh      |   2.34B Units     |
| (17,980 Unique)   |   (All Regions)   |  (Satisfied Tier) |  (EPA/WLTP Avg)   |   (Gross Pack)    | (Fleet Aggregate) |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
```

### KPI Card 1: Total EV Models
* **Worksheet Name:** `KPI_Total_Models`
* **Analytical Purpose:** Quantify the total volume of vehicle records and distinct commercial model offerings in the database.
* **Fields Used:**
  * Primary Measure: `COUNT(cleaned_ev_dataset.csv)` (or `COUNTD(vehicle_id)`) -> **299,999 records**.
  * Secondary Detail: `COUNTD(model_name)` -> **17,980 unique commercial models**.
* **Marks Card:**
  * Mark Type: **Text**
  * Text Shelf:
    ```text
    <AGG(COUNT(cleaned_ev_dataset.csv))>
    Records (<CNTD(model_name)> Unique Models)
    TOTAL EV MODELS
    ```
* **Format:**
  * Big Number: 22pt Bold, Color: `#1F4E78` (Navy).
  * Subtitle / Label: 9pt Regular, Color: `#595959` (Slate Gray).

### KPI Card 2: Total Manufacturers (OEMs)
* **Worksheet Name:** `KPI_Total_Manufacturers`
* **Analytical Purpose:** Gauge the breadth of global automotive competition.
* **Fields Used:** `COUNTD(manufacturer)` -> **200 distinct OEMs**.
* **Marks Card:**
  * Mark Type: **Text**
  * Text Shelf:
    ```text
    <CNTD(manufacturer)>
    Active Global OEMs
    TOTAL MANUFACTURERS
    ```
* **Format:** 22pt Bold, Color: `#1F4E78`.

### KPI Card 3: Average Customer Rating
* **Worksheet Name:** `KPI_Avg_Customer_Rating`
* **Analytical Purpose:** Monitor overall consumer sentiment and satisfaction index.
* **Fields Used:** `AVG(customer_rating)` -> **4.09 / 5.0**.
* **Marks Card:**
  * Mark Type: **Text**
  * Text Shelf:
    ```text
    <AVG(customer_rating)> ★
    Scale: 1.0 - 5.0 Stars
    AVG CUSTOMER RATING
    ```
* **Format:** 22pt Bold, Color: `#2CA02C` (Green) or `#1F4E78`. Number Format: Number (Custom) 2 decimal places.

### KPI Card 4: Average Driving Range
* **Worksheet Name:** `KPI_Avg_Driving_Range`
* **Analytical Purpose:** Benchmark average single-charge endurance across the global fleet.
* **Fields Used:** `AVG(range_km)` -> **324.46 km** (formatted as `324.5 km`).
* **Marks Card:**
  * Mark Type: **Text**
  * Text Shelf:
    ```text
    <AVG(range_km)> km
    Single-Charge Certified
    AVG DRIVING RANGE
    ```
* **Format:** 22pt Bold, Color: `#0078D4` (Electric Blue). Number Format: Number (Custom) 1 decimal place.

### KPI Card 5: Average Battery Capacity
* **Worksheet Name:** `KPI_Avg_Battery_Capacity`
* **Analytical Purpose:** Track mean energy storage capacity of high-voltage traction packs.
* **Fields Used:** `AVG(battery_capacity_kwh)` -> **78.24 kWh** (formatted as `78.2 kWh`).
* **Marks Card:**
  * Mark Type: **Text**
  * Text Shelf:
    ```text
    <AVG(battery_capacity_kwh)> kWh
    Gross Traction Pack
    AVG BATTERY CAPACITY
    ```
* **Format:** 22pt Bold, Color: `#9467BD` (Purple) or `#1F4E78`. Number Format: Number (Custom) 1 decimal place.

### KPI Card 6: Total Annual Sales Volume
* **Worksheet Name:** `KPI_Total_Annual_Sales`
* **Analytical Purpose:** Represent gross global commercial sales volume across the fleet.
* **Fields Used:** `SUM(annual_sales_units)` -> **2,336,228,365 units** (~2.34B units).
* **Marks Card:**
  * Mark Type: **Text**
  * Text Shelf:
    ```text
    <SUM(annual_sales_units)>
    Annual Units Delivered
    TOTAL ANNUAL SALES
    ```
* **Format:** 22pt Bold, Color: `#D62728` (Crimson) or `#1F4E78`. Number Format: Number (Custom) Display Units: Billions (B), 2 decimal places (`2.34B`).

---

## 3. Seven Core Visualizations Technical Specifications

---

### VISUALIZATION 1: EV Market Performance at a Glance
* **Worksheet Name:** `Viz1_Market_Performance_Glance`
* **Purpose:** Display important market KPIs in a consolidated, single-view executive summary table / scorecard.
* **Structure:**
  * Columns Shelf: `Measure Names`
  * Rows Shelf: [Empty]
  * Text Shelf: `Measure Values`
  * Filter on Measure Names: Include `CNTD(vehicle_id)`, `CNTD(manufacturer)`, `AVG(customer_rating)`, `AVG(range_km)`, `AVG(battery_capacity_kwh)`, `SUM(annual_sales_units)`.
* **Alternative Dashboard Implementation:** Assemble the 6 individual KPI card worksheets in a unified horizontal container across the top of the dashboard.

---

### VISUALIZATION 2: EV Category Performance & Distribution
* **Worksheet Name:** `Viz2_Category_Performance`
* **Chart Type:** Horizontal Bar Chart
* **Purpose:** Compare market presence, model diversity, and unit sales across all 15 vehicle segments.
* **Shelves Configuration:**
  * **Rows Shelf:** `category` (Sorted Descending by `COUNT(cleaned_ev_dataset.csv)`)
  * **Columns Shelf:** `COUNT(cleaned_ev_dataset.csv)` (or `SUM(annual_sales_units)`)
* **Marks Card:**
  * Mark Type: **Bar**
  * Color Shelf: `category` (or sequential blue gradient: `#1F4E78` to `#85C1E9`)
  * Label Shelf:
    * Primary: `COUNT(cleaned_ev_dataset.csv)`
    * Secondary: Quick Table Calculation -> **Percent of Total**
  * Tooltip Shelf:
    ```text
    Vehicle Category: <category>
    Total Vehicle Models: <COUNT(cleaned_ev_dataset.csv)> (<% of Total COUNT(cleaned_ev_dataset.csv)>)
    Total Annual Sales: <SUM(annual_sales_units)> units
    Average Retail Price: $<AVG(price_usd)>
    Average Certified Range: <AVG(range_km)> km
    Average Battery Capacity: <AVG(battery_capacity_kwh)> kWh
    ```
* **Formatting:**
  * X-Axis: Title = "Number of Vehicle Models". Show major tick marks every 5,000 units.
  * Y-Axis: Title = "Vehicle Category". Header font: Arial 10pt Semi-bold.
  * Gridlines: Vertical gridlines dashed, subtle gray (`#E0E0E0`).

---

### VISUALIZATION 3: Market Share by Manufacturer
* **Worksheet Name:** `Viz3_Manufacturer_Market_Share`
* **Chart Type:** Donut Chart (Dual-Axis Pie Chart)
* **Purpose:** Analyze manufacturer contribution, leading OEM market shares, and portfolio dispersion.
* **Shelves Configuration:**
  * **Columns Shelf:** `MIN(0)` (or dummy calculated field `0`), duplicated as dual axis: `MIN(0)` and `MIN(0)`.
  * **Rows Shelf:** [Empty]
* **Marks Card 1 (Outer Ring - Pie):**
  * Mark Type: **Pie**
  * Color Shelf: `manufacturer` (Top 10 OEMs highlighted; remaining grouped or distinct palette)
  * Angle Shelf: `COUNT(cleaned_ev_dataset.csv)`
  * Size: Large
  * Tooltip:
    ```text
    Manufacturer: <manufacturer>
    Model Offerings: <COUNT(cleaned_ev_dataset.csv)>
    Market Share: <% of Total COUNT(cleaned_ev_dataset.csv)>
    Total Annual Sales: <SUM(annual_sales_units)> units
    ```
* **Marks Card 2 (Inner Circle - Hole):**
  * Mark Type: **Circle**
  * Color Shelf: White (`#FFFFFF`)
  * Size: Medium (creating the donut ring opening)
  * Label Shelf:
    ```text
    200
    Active OEMs
    ```
  * Label Alignment: Center-Center, 14pt Bold Navy.
* **Formatting:** Synchronize dual axes, hide zero lines, hide axis headers.

---

### VISUALIZATION 4: Customer Rating Records by EV Category
* **Worksheet Name:** `Viz4_Customer_Rating_by_Category`
* **Chart Type:** Horizontal or Vertical Bar Chart
* **Purpose:** Benchmark customer satisfaction and review score variations across the 15 vehicle categories.
* **Shelves Configuration:**
  * **Rows Shelf:** `category` (Sorted Descending by `AVG(customer_rating)`)
  * **Columns Shelf:** `AVG(customer_rating)`
* **Marks Card:**
  * Mark Type: **Bar**
  * Color Shelf: `AVG(customer_rating)` (Diverging Color Palette: Orange-Blue or Green sequential)
  * Label Shelf: `AVG(customer_rating)` (Format: Number Custom, 3 decimal places, e.g., `4.094 ★`)
  * Tooltip:
    ```text
    Vehicle Category: <category>
    Average Customer Rating: <AVG(customer_rating)> / 5.0 Stars
    Total Evaluated Models: <COUNT(cleaned_ev_dataset.csv)>
    Min Rating: <MIN(customer_rating)> | Max Rating: <MAX(customer_rating)>
    ```
* **Analytics Pane:**
  * Add **Reference Line** -> Value: `AVG(customer_rating)` across entire fleet (4.09 Stars). Line style: Red Dashed, Label: "Fleet Average: 4.09★".
* **Formatting:**
  * X-Axis: Edit Axis -> Set Range from **3.8 to 4.2 Stars** to allow visual differentiation between category satisfaction tiers while maintaining professional baseline notation.

---

### VISUALIZATION 5: Annual EV Sales Trend by Model Year
* **Worksheet Name:** `Viz5_Sales_Trend_by_Model_Year`
* **Chart Type:** Line Chart with Data Point Markers
* **Purpose:** Track annual sales volume across vehicle model release years (2018–2026) to assess market evolution.
* **Shelves Configuration:**
  * **Columns Shelf:** `model_year` (Discrete Dimension or Continuous)
  * **Rows Shelf:** `SUM(annual_sales_units)`
* **Marks Card:**
  * Mark Type: **Line**
  * Shape/Marker: Show Data Point Markers (Circle)
  * Color Shelf: Solid Brand Blue (`#0078D4`)
  * Line Width: 3pt
  * Label Shelf: `SUM(annual_sales_units)` (Format: Display Units = Millions `M`, 1 decimal place, e.g., `258.2M`)
  * Tooltip:
    ```text
    Model Release Year: <model_year>
    Total Annual Sales: <SUM(annual_sales_units)> units
    Average Sales per Model: <AVG(annual_sales_units)> units
    Total Models Introduced: <COUNT(cleaned_ev_dataset.csv)>
    ```
* **Formatting:**
  * X-Axis: Title = "Model Year". Tick marks at every integer year: 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026.
  * Y-Axis: Title = "Annual Sales Volume (Units)". Number format: Millions (`M`). Range: 240M to 280M.

---

### VISUALIZATION 6: Battery Technology Market Share
* **Worksheet Name:** `Viz6_Battery_Technology_Share`
* **Chart Type:** Pie Chart / Donut Chart
* **Purpose:** Highlight the competitive distribution across all 5 battery cell chemistries (NMC, LFP, NCA, Sodium-Ion, Solid-State).
* **Shelves Configuration:**
  * **Columns Shelf:** [Empty]
  * **Rows Shelf:** [Empty]
* **Marks Card:**
  * Mark Type: **Pie**
  * Color Shelf: `battery_type`
    * NMC: Royal Navy (`#1F4E78`)
    * LFP: Emerald Green (`#2CA02C`)
    * NCA: Coral Red (`#FF7F0E`)
    * Sodium-Ion: Amber Gold (`#BCBD22`)
    * Solid-State: Deep Purple (`#9467BD`)
  * Angle Shelf: `COUNT(cleaned_ev_dataset.csv)`
  * Label Shelf:
    * Primary: `battery_type`
    * Secondary: Quick Table Calculation -> **Percent of Total** (e.g., `NMC: 33.8%`, `LFP: 32.1%`)
  * Tooltip:
    ```text
    Battery Chemistry: <battery_type>
    Total Vehicle Models: <COUNT(cleaned_ev_dataset.csv)>
    Market Share: <% of Total COUNT(cleaned_ev_dataset.csv)>
    Average Cycle Life: <AVG(battery_cycle_life)> cycles
    Average 5-Yr Degradation: <AVG(battery_degradation_pct_5yr)>%
    ```
* **Formatting:** Clean white borders around pie slices (`Border: #FFFFFF`).

---

### VISUALIZATION 7: Electric Vehicle Distribution by Manufacturing Country
* **Worksheet Name:** `Viz7_Manufacturing_Country_Map`
* **Chart Type:** Geographic Filled Map (Choropleth) or Symbol Map
* **Purpose:** Map sovereign automotive manufacturing presence across the 10 production nations.
* **Geographic Setup:** Ensure `manufacturing_country` is recognized as Country/Region.
* **Shelves Configuration:**
  * **Columns Shelf:** `Longitude (generated)`
  * **Rows Shelf:** `Latitude (generated)`
* **Marks Card (Filled Map):**
  * Mark Type: **Map**
  * Detail Shelf: `manufacturing_country`
  * Color Shelf: `COUNT(cleaned_ev_dataset.csv)` (Sequential color palette: Blues or Teal, 5 steps)
  * Label Shelf:
    * `manufacturing_country`
    * `COUNT(cleaned_ev_dataset.csv)`
  * Tooltip:
    ```text
    Manufacturing Country: <manufacturing_country>
    Total Vehicle Models Produced: <COUNT(cleaned_ev_dataset.csv)>
    Share of Global Assembly: <% of Total COUNT(cleaned_ev_dataset.csv)>
    Total Annual Sales from Country: <SUM(annual_sales_units)> units
    ```
* **Map Layers:** Background style: Light / Gray. Washout: 10%. Coastline and country borders visible.

---

## 4. Summary Table of Visualizations and Fields

| Viz # | Title | Chart Type | Dimensions Used | Measures & Aggregations |
| :--- | :--- | :--- | :--- | :--- |
| **KPI** | EV Market Performance at a Glance | KPI Metric Cards | None | `CNTD(vehicle_id)`, `CNTD(model_name)`, `CNTD(manufacturer)`, `AVG(customer_rating)`, `AVG(range_km)`, `AVG(battery_capacity_kwh)`, `SUM(annual_sales_units)` |
| **Viz 2** | EV Category Performance & Distribution | Horizontal Bar Chart | `category` | `COUNT(vehicle_id)`, `SUM(annual_sales_units)`, `% of Total` |
| **Viz 3** | Market Share by Manufacturer | Donut Chart (Dual Axis) | `manufacturer` | `COUNT(vehicle_id)`, `% of Total`, Center Label: `CNTD(manufacturer)` |
| **Viz 4** | Customer Rating Records by EV Category | Bar Chart with Ref Line | `category` | `AVG(customer_rating)`, Reference Line: `Fleet AVG` |
| **Viz 5** | Annual EV Sales Trend by Model Year | Line Chart with Markers | `model_year` | `SUM(annual_sales_units)` |
| **Viz 6** | Battery Technology Market Share | Pie Chart | `battery_type` | `COUNT(vehicle_id)`, `% of Total` |
| **Viz 7** | EV Distribution by Manufacturing Country | Geographic Choropleth Map | `manufacturing_country` | `COUNT(vehicle_id)`, `SUM(annual_sales_units)` |
