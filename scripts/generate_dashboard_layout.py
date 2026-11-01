import os

output_path = r"deliverables/dashboard_layout_plan.md"
root_path = r"dashboard_layout_plan.md"

content = """# TABLEAU DASHBOARD LAYOUT PLAN
## ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS (PHASE 2)

**Document ID:** DLP-EV-2026-PH2  
**Dashboard Title:** ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS  
**Dashboard Subtitle:** A Data-Driven Exploration of Global EV Manufacturing, Technology and Market Trends.  
**Platform:** Tableau Public / Tableau Desktop  
**Target Resolution:** Standard Desktop / Large Display (`1440 x 900` px or `1366 x 768` px)  
**Layout Container Architecture:** Clean 100% Tiled Hierarchy with Horizontal and Vertical Layout Containers

---

## 1. Design Philosophy & Visual Design System

The dashboard is engineered to emulate executive business intelligence cockpits (McKinsey, Bloomberg NEF, IEA EV Outlook):
* **Information Density:** High utility with zero clutter.
* **Palette Restraint:** Executive Navy (`#1F4E78`), Clean White Container Backgrounds (`#FFFFFF`), Slate Gray Structure (`#F4F6F9`), and purposeful semantic accents.
* **Typography Hierarchy:**
  * Dashboard Header: Arial / Tableau Bold, 20pt, Color `#1F4E78`
  * Dashboard Subtitle: Arial / Tableau Book, 11pt, Color `#5A6B7C`
  * Worksheet Titles: Arial / Tableau Semi-bold, 12pt, Color `#2C3E50`
  * KPI Large Numerics: Arial / Tableau Bold, 22pt, Color `#1F4E78`
  * Axis & Labels: Arial / Tableau Regular, 9pt, Color `#4A5568`
* **Spacing & Padding:** Strict 8px outer padding on all container cards; 4px inner padding between chart elements.

```
+---------------------------------------------------------------------------------------------------------+
|                                  HEADER & METADATA BAR (Height: 80px)                                   |
|  ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS                                                         |
|  A Data-Driven Exploration of Global EV Manufacturing, Technology and Market Trends                     |
+---------------------------------------------------------------------------------------------------------+
|                                    GLOBAL FILTER BAR (Height: 55px)                                     |
|  [Manufacturer: All] [Category: All] [Country: All] [Battery: All] [Model Year: All] [Region: All]      |
+---------------------------------------------------------------------------------------------------------+
|                                  KPI CARDS CONTAINER (Height: 95px)                                     |
|  +--------------+ +--------------+ +--------------+ +--------------+ +--------------+ +--------------+  |
|  |TOTAL MODELS  | |TOTAL MFGS    | |AVG RATING    | |AVG RANGE     | |AVG BATTERY   | |TOTAL SALES   |  |
|  |299,999 Recs  | |200 OEMs      | |4.09 / 5.0 ★  | |324.5 km      | |78.2 kWh      | |2.34B Units   |  |
|  |(17.9k Models)| |(Global Fleet)| |(Satisfied)   | |(Single-Chrg) | |(Pack Gross)  | |(Fleet Agg.)  |  |
|  +--------------+ +--------------+ +--------------+ +--------------+ +--------------+ +--------------+  |
+---------------------------------------------------------------------------------------------------------+
|                                           MAIN VISUAL BODY                                              |
|  +-------------------------------------------------+ +-----------------------------------------------+  |
|  | VISUALIZATION 2:                                | | VISUALIZATION 3:                              |  |
|  | EV Category Performance & Distribution          | | Market Share by Manufacturer                  |  |
|  | (Horizontal Bar Chart: 15 Categories)           | | (Donut Chart: Top OEMs vs Market)             |  |
|  +-------------------------------------------------+ +-----------------------------------------------+  |
|                                                                                                         |
|  +---------------------------+ +----------------------------+ +--------------------------------------+  |
|  | VISUALIZATION 5:          | | VISUALIZATION 6:           | | VISUALIZATION 4:                     |  |
|  | Annual Sales Trend        | | Battery Technology Share   | | Customer Rating Records              |  |
|  | (Line Chart: 2018-2026)   | | (Pie Chart: 5 Chemistries) | | (Bar Chart with Fleet Avg Line)      |  |
|  +---------------------------+ +----------------------------+ +--------------------------------------+  |
|                                                                                                         |
|  +---------------------------------------------------------------------------------------------------+  |
|  | VISUALIZATION 7:                                                                                  |  |
|  | Electric Vehicle Distribution by Manufacturing Country                                            |  |
|  | (Global Geographic Choropleth Map: 10 Sovereign Assembly Hubs)                                    |  |
|  +---------------------------------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------------------------------+
```

---

## 2. Container Hierarchy & Layout Structure

### Root Container: Vertical Container (Width: 1440px, Height: Automatic or Fixed 1150px)
* Background: `#F4F6F9` (Light Slate Canvas)
* Border: None

#### A. Header Zone (Height: 80px)
* Container Type: **Horizontal Container**
* Components:
  1. **Title & Subtitle Text Box (Left Aligned, 75% width):**
     * Line 1: `ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS` (20pt Bold, `#1F4E78`)
     * Line 2: `A Data-Driven Exploration of Global EV Manufacturing, Technology and Market Trends.` (11pt Book, `#5A6B7C`)
  2. **Metadata & Status Pill (Right Aligned, 25% width):**
     * Text: `Production Dataset: 299,999 Records | 200 OEMs | Status: Phase 2 Certified`
     * Background: `#EBF3FB`, Border: 1px solid `#B9D5F1`, Radius: 4px.

#### B. Global Interactive Filter Bar (Height: 55px)
* Container Type: **Horizontal Container**
* Background: `#FFFFFF`, Border: 1px solid `#E1E4E8`
* Padding: Top/Bottom 8px, Left/Right 12px
* Components (6 equal-spaced dropdown filter controls):
  1. `Manufacturer` (Multiple Values Dropdown)
  2. `Category` (Multiple Values Dropdown)
  3. `Manufacturing Country` (Multiple Values Dropdown)
  4. `Battery Type` (Multiple Values Dropdown)
  5. `Model Year` (Multiple Values Dropdown)
  6. `Market Region` (Multiple Values Dropdown)

#### C. Executive KPI Scorecard Container (Height: 95px)
* Container Type: **Horizontal Container**
* Components (6 equal-width tiled cards, width ~230px each):
  * **Card 1: Total Models:** `KPI_Total_Models` (White card, `#1F4E78` border top)
  * **Card 2: Total Manufacturers:** `KPI_Total_Manufacturers`
  * **Card 3: Avg Rating:** `KPI_Avg_Customer_Rating`
  * **Card 4: Avg Range:** `KPI_Avg_Driving_Range`
  * **Card 5: Avg Battery:** `KPI_Avg_Battery_Capacity`
  * **Card 6: Total Sales:** `KPI_Total_Annual_Sales`

#### D. Visual Row 1: Structural Market Dynamics (Height: 340px)
* Container Type: **Horizontal Container**
* Split: 58% Left / 42% Right
* **Left Tile (58%):** `Viz2_Category_Performance`
  * Card title: `EV Category Performance & Distribution`
  * Subtitle: `Total unique model offerings and volume by vehicle body category`
  * Background: `#FFFFFF`, Border: 1px solid `#E1E4E8`, Inner Padding: 8px
* **Right Tile (42%):** `Viz3_Manufacturer_Market_Share`
  * Card title: `Market Share by Manufacturer`
  * Subtitle: `Model portfolio contribution across 200 active OEMs`
  * Background: `#FFFFFF`, Border: 1px solid `#E1E4E8`, Inner Padding: 8px

#### E. Visual Row 2: Technology, Sales & Consumer Sentiment (Height: 320px)
* Container Type: **Horizontal Container**
* Split: 34% / 33% / 33%
* **Left Tile (34%):** `Viz5_Sales_Trend_by_Model_Year`
  * Card title: `Annual EV Sales Trend by Model Year`
  * Subtitle: `Total annual sales volume (units) by model release vintage`
  * Background: `#FFFFFF`, Border: 1px solid `#E1E4E8`, Inner Padding: 8px
* **Center Tile (33%):** `Viz6_Battery_Technology_Share`
  * Card title: `Battery Technology Market Share`
  * Subtitle: `Electrochemical cell chemistry distribution`
  * Background: `#FFFFFF`, Border: 1px solid `#E1E4E8`, Inner Padding: 8px
* **Right Tile (33%):** `Viz4_Customer_Rating_by_Category`
  * Card title: `Customer Rating Records by EV Category`
  * Subtitle: `Average satisfaction score (1-5★) vs fleet baseline (4.09★)`
  * Background: `#FFFFFF`, Border: 1px solid `#E1E4E8`, Inner Padding: 8px

#### F. Visual Row 3: Global Production Footprint (Height: 340px)
* Container Type: **Horizontal Container**
* **Full-Width Tile (100%):** `Viz7_Manufacturing_Country_Map`
  * Card title: `Electric Vehicle Distribution by Manufacturing Country`
  * Subtitle: `Geographic concentration of vehicle model assembly across 10 sovereign automotive hubs`
  * Background: `#FFFFFF`, Border: 1px solid `#E1E4E8`, Inner Padding: 8px

---

## 3. Formatting, Padding, and Border Standard

To achieve a clean, modern, native card appearance:
1. Every worksheet container receives:
   * **Outer Padding:** 6px (creates distinct gutters between cards).
   * **Inner Padding:** 8px (keeps text away from card edges).
   * **Shading / Background:** Pure White (`#FFFFFF`).
   * **Border:** Thin solid stroke (`#D9E1E8`).
2. Dashboard Canvas Background is set to Soft Neutral (`#F4F6F9`).
3. Title Formatting:
   * Bold 12pt `#1F4E78` Title.
   * Light 9pt `#7F8C8D` Subtitle.
4. Tooltips:
   * Uniform styling: Dark Charcoal background (`#263238`), White font (`#FFFFFF`), Arial 9pt.

---

## 4. Responsive Device Designer Blueprints

Tableau Device Designer presets:
* **Default (Desktop):** 1440 x 900 px (or 1366 x 768 px). Full 3-row layout.
* **Tablet (iPad / Surface):** 1024 x 768 px. KPI cards collapse into 2 rows of 3. Visual rows stack into 2-column or 1-column layouts.
* **Phone / Mobile:** 375 x 667 px. Single-column vertical scroll. Filters placed inside collapsible container; KPI cards stacked vertically.
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)
with open(root_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated: {output_path} and {root_path}")

