# TABLEAU FILTER IMPLEMENTATION & INTERACTION GUIDE
## ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS (PHASE 2)

**Document ID:** FIG-EV-2026-PH2  
**Platform:** Tableau Public / Tableau Desktop  
**Data Source:** `cleaned_ev_dataset.csv`

---

## 1. Overview of Interactive Controls

To allow executive stakeholders and analysts to interrogate the fleet across commercial, geographic, and technological dimensions, six global filters and three dashboard interaction actions are implemented.

```
+----------------------------------------------------------------------------------------------------------+
|  [Manufacturer: (All)]  [Category: (All)]  [Country: (All)]  [Battery: (All)]  [Year: (All)]  [Region: (All)]|
+----------------------------------------------------------------------------------------------------------+
```

---

## 2. Global Dropdown Filter Configuration

Each of the six filters must be configured to affect all relevant worksheets using Tableau's **Apply to Worksheets** feature:

### Filter 1: Manufacturer (OEM)
* **Field:** `manufacturer`
* **Display Title:** `Select Manufacturer`
* **Control Type:** Multiple Values (Dropdown)
* **Search Enabled:** Yes (critical for 200 OEMs)
* **Scope Setting:** Right-click filter card -> **Apply to Worksheets** -> **All Using This Data Source**.

### Filter 2: EV Category
* **Field:** `category`
* **Display Title:** `Select EV Category`
* **Control Type:** Multiple Values (Dropdown)
* **Scope Setting:** Right-click filter card -> **Apply to Worksheets** -> **All Using This Data Source**.

### Filter 3: Manufacturing Country
* **Field:** `manufacturing_country`
* **Display Title:** `Select Assembly Country`
* **Control Type:** Multiple Values (Dropdown)
* **Scope Setting:** Right-click filter card -> **Apply to Worksheets** -> **All Using This Data Source**.

### Filter 4: Battery Technology Type
* **Field:** `battery_type`
* **Display Title:** `Select Battery Chemistry`
* **Control Type:** Multiple Values (Dropdown)
* **Options:** `(All)`, `LFP`, `NCA`, `NMC`, `Sodium-Ion`, `Solid-State`
* **Scope Setting:** Right-click filter card -> **Apply to Worksheets** -> **All Using This Data Source**.

### Filter 5: Model Year
* **Field:** `model_year`
* **Display Title:** `Select Model Year`
* **Control Type:** Multiple Values (Dropdown) or Slider / Range
* **Options:** `2018` through `2026`
* **Scope Setting:** Right-click filter card -> **Apply to Worksheets** -> **All Using This Data Source**.

### Filter 6: Market Region
* **Field:** `market_region`
* **Display Title:** `Select Target Market Region`
* **Control Type:** Multiple Values (Dropdown)
* **Options:** `Africa`, `Asia Pacific`, `Europe`, `Latin America`, `Middle East`, `North America`, `South Asia`
* **Scope Setting:** Right-click filter card -> **Apply to Worksheets** -> **All Using This Data Source**.

---

## 3. Dashboard Actions & Cross-Filtering Architecture

In addition to top-bar dropdown filters, dashboard actions transform the static visualizations into an interactive exploration environment.

### Action 1: Category Cross-Filter (Click on Category Bar)
* **Menu:** Dashboard -> Actions -> **Add Action** -> **Filter...**
* **Name:** `Filter Dashboard by Selected Category`
* **Source Sheet:** `Viz2_Category_Performance`
* **Run Action on:** **Select** (Click)
* **Target Sheets:** All other worksheets (KPI cards, Viz 3 Donut, Viz 4 Ratings, Viz 5 Sales Trend, Viz 6 Battery Share, Viz 7 Map).
* **Clearing Selection Will:** **Show all values**.
* **Target Field:** `category`

### Action 2: Manufacturing Country Cross-Filter (Click on Map)
* **Menu:** Dashboard -> Actions -> **Add Action** -> **Filter...**
* **Name:** `Filter Dashboard by Selected Country`
* **Source Sheet:** `Viz7_Manufacturing_Country_Map`
* **Run Action on:** **Select** (Click)
* **Target Sheets:** All other worksheets.
* **Clearing Selection Will:** **Show all values**.
* **Target Field:** `manufacturing_country`

### Action 3: Battery Chemistry Cross-Filter (Click on Pie Slice)
* **Menu:** Dashboard -> Actions -> **Add Action** -> **Filter...**
* **Name:** `Filter Dashboard by Battery Chemistry`
* **Source Sheet:** `Viz6_Battery_Technology_Share`
* **Run Action on:** **Select** (Click)
* **Target Sheets:** All other worksheets.
* **Clearing Selection Will:** **Show all values**.
* **Target Field:** `battery_type`

### Action 4: Manufacturer Highlight Action (Hover on OEM)
* **Menu:** Dashboard -> Actions -> **Add Action** -> **Highlight...**
* **Name:** `Highlight OEM Across Views`
* **Source Sheet:** `Viz3_Manufacturer_Market_Share`
* **Run Action on:** **Hover**
* **Target Sheets:** `Viz2_Category_Performance`, `Viz5_Sales_Trend_by_Model_Year`
* **Target Field:** `manufacturer`

---

## 4. Worksheets Affected Matrix

| Interactive Control | KPI Cards | Viz 2 (Category) | Viz 3 (OEM Donut) | Viz 4 (Ratings) | Viz 5 (Sales Trend) | Viz 6 (Battery Pie) | Viz 7 (Country Map) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Manufacturer Filter** | Yes | Yes | Yes (Highlights) | Yes | Yes | Yes | Yes |
| **Category Filter / Click** | Yes | Source / Self | Yes | Yes | Yes | Yes | Yes |
| **Country Filter / Map Click**| Yes | Yes | Yes | Yes | Yes | Yes | Source / Self |
| **Battery Type / Pie Click** | Yes | Yes | Yes | Yes | Yes | Source / Self | Yes |
| **Model Year Filter** | Yes | Yes | Yes | Yes | Source / Zoom | Yes | Yes |
| **Market Region Filter** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

---

## 5. Adding a "Reset All Filters" Button in Tableau

To enhance user experience, a native Reset Filter button is configured:
1. **Create Reset Worksheet:**
   * Create a new worksheet named `Btn_Reset_Filters`.
   * Create an ad-hoc calculated field in the Marks card: `"↺ Reset Filters"`.
   * Change Mark type to **Shape** or **Text**. Format font as 10pt Bold `#1F4E78`, background light gray `#EBF3FB`.
2. **Add to Dashboard:** Drag `Btn_Reset_Filters` next to the filter bar.
3. **Configure Reset Action:**
   * Dashboard -> Actions -> **Add Action** -> **Filter...**
   * Source: `Btn_Reset_Filters`.
   * Target Sheets: All worksheets.
   * Target Fields: `Selected Fields` -> map each filter field (`category`, `manufacturer`, etc.) to reset.
