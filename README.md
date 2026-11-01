# ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS
## Comprehensive Data Analytics, Business Intelligence & Full-Stack Web Integration

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask 3.1](https://img.shields.io/badge/Flask-3.1-black.svg)](https://flask.palletsprojects.com/)
[![Tableau Public](https://img.shields.io/badge/Tableau_Public-2026.3-orange.svg)](https://public.tableau.com/)
[![Data Quality](https://img.shields.io/badge/Data_Quality-100%25_Verified-success.svg)]()
[![Dataset](https://img.shields.io/badge/Fleet_Records-299%2C999-brightgreen.svg)]()

---

## 1. Project Overview

**"ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS"** is an end-to-end data analytics, business intelligence, and web application platform designed to analyze the global electric vehicle (EV) ecosystem. Across **299,999 validated vehicle records**, the project evaluates:
* **Market Distribution Across Manufacturers:** Competitive dynamics across 200 automotive OEMs.
* **Vehicle Category Stratification:** Performance and pricing across 15 vehicle categories from micro-mobility to heavy commercial transit.
* **Battery Technology Adoption:** Lifespan and degradation across 5 cell chemistries (NMC, LFP, NCA, Sodium-Ion, Solid-State).
* **Engineering & Powertrain Performance:** Range, battery capacity, motor power, torque, and thermodynamic efficiency.
* **Economic Determinants:** Retail price (MSRP) regression, resale value retention, and insurance costs.
* **Sustainability ROI:** Net annual carbon displacement (tons CO2 saved per vehicle per year vs ICE).

---

## 2. Directory Structure

```
Electric_Vehicle_Market_Insights/
│
├── Dataset/
│   ├── Original/
│   │   ├── ev_market_train.csv          (Raw training split: 200,000 records)
│   │   └── ev_market_test.csv           (Raw testing split: 100,000 records)
│   └── Cleaned/
│       ├── cleaned_ev_dataset.csv       (Production Tableau-ready fleet: 299,999 records)
│       ├── cleaned_ev_train.csv         (Deduplicated clean train split: 199,999 records)
│       └── cleaned_ev_test.csv          (Clean test split: 100,000 records)
│
├── Analysis/
│   ├── Notebooks/
│   │   └── ev_eda_analysis.ipynb        (Reproducible 31-cell Jupyter EDA Notebook)
│   └── Reports/
│       ├── dataset_profile.csv          (37-feature metadata profile & IQR audit)
│       ├── data_quality_report.txt       (Comprehensive data quality & deduplication audit)
│       ├── ev_eda_summary.txt           (Executive statistical findings across 14 topics)
│       ├── tableau_data_dictionary.xlsx (Multi-tab professional Excel data dictionary)
│       └── performance_testing_report.txt (Actual empirical benchmark test results)
│
├── Tableau/
│   ├── Dashboard_Specification/
│   │   ├── tableau_visualization_specification.md (Shelf-by-shelf configuration guide)
│   │   ├── dashboard_layout_plan.md               (1440x900 container grid architecture)
│   │   ├── filter_implementation_guide.md         (Global filters & cross-filtering actions)
│   │   ├── chart_wise_analytical_findings.md      (Exact metrics & empirical findings)
│   │   └── tableau_testing_checklist.md           (25-point quality assurance protocol)
│   ├── Story_Specification/
│   │   └── tableau_story_structure.md             (7-scene narrative storytelling script)
│   └── Screenshots/                               (Directory for dashboard exports)
│
├── Flask_Web_App/
│   ├── app.py                           (Flask backend server & REST API endpoints)
│   ├── templates/
│   │   ├── base.html                    (Master HTML5 template with Tableau API v3)
│   │   ├── index.html                   (Landing page, KPIs, embedded Tableau, overview)
│   │   ├── tableau.html                 (Dedicated Tableau Public & Story explorer)
│   │   ├── findings.html                (Detailed 14-topic research findings page)
│   │   └── compare.html                 (Interactive vehicle spec comparator tool)
│   ├── static/
│   │   ├── css/style.css                (Modern responsive design system & CSS Grid)
│   │   ├── js/main.js                   (Story switcher, spec comparator, embed modal)
│   │   └── img/                         (Web branding assets and icons)
│   └── requirements.txt                 (Python package dependencies)
│
├── Documentation/
│   ├── Final_Project_Report.docx        (Formal 25-section academic project report in Word)
│   ├── Final_Project_Report.md          (Markdown counterpart of 25-section report)
│   ├── Presentation_Script.docx         (5–7 minute oral screen-sharing presentation script)
│   ├── Presentation_Script.md           (Markdown counterpart of presentation script)
│   └── Viva_Questions_and_Answers.md    (28 comprehensive technical Viva Q&A items)
│
└── README.md                            (Master project documentation and execution guide)
```

---

## 3. How to Run the Flask Web Application

### Prerequisites
* Python 3.9 or higher (tested on Python 3.11/3.13)
* Dependencies installed via `pip`

### Step 1: Navigate to the Flask App Directory
```powershell
cd "Electric_Vehicle_Market_Insights\Flask_Web_App"
```

### Step 2: Install Required Packages
```powershell
pip install -r requirements.txt
```

### Step 3: Launch the Application
```powershell
python app.py
```

### Step 4: Access in Web Browser
Open your preferred browser (Chrome, Edge, Firefox, Safari) and navigate to:
```
http://127.0.0.1:5000
```

### Web Application Features:
* **Interactive KPI Scorecard:** Displays live fleet metrics (299,999 records, 200 OEMs, 4.09★ rating, 324.5 km range, 78.2 kWh battery, 2.34B sales).
* **Official Tableau Embedding:** Embedded `<tableau-viz>` web component with an on-page configuration modal allowing you to link your own published Tableau Public workbook URL.
* **7-Scene Story Navigator:** Guided tabbed narrative through the 7 strategic story points.
* **Vehicle Spec Comparator:** Side-by-side benchmark comparing technical and pricing specs between any two vehicle categories.
* **REST APIs:** `/api/kpi`, `/api/category-stats`, and `/api/spec-compare`.

---

## 4. How to Publish the Dashboard to Tableau Public

### Step 1: Open Tableau Desktop or Tableau Public
Launch Tableau Public (pre-installed at `C:\Program Files\Tableau\Tableau Public 2026.3in	abpublic.exe`) or Tableau Desktop.

### Step 2: Connect to the Cleaned Dataset
1. Under **Connect** -> click **Text file**.
2. Select `Electric_Vehicle_Market_Insights/Dataset/Cleaned/cleaned_ev_dataset.csv`.
3. In the Data Source view, verify that 299,999 records are loaded.
4. Ensure `manufacturing_country` has its Geographic Role set to **Country/Region**.

### Step 3: Build the Worksheets and Master Dashboard
Follow the explicit step-by-step instructions in [`Tableau/Dashboard_Specification/tableau_visualization_specification.md`](file:///c:/Users/Sanjana/OneDrive/Documents/Skillwallet%20project/Electric_Vehicle_Market_Insights/Tableau/Dashboard_Specification/tableau_visualization_specification.md) to build:
* The 6 KPI Cards (`KPI_Total_Models`, `KPI_Total_Manufacturers`, `KPI_Avg_Customer_Rating`, `KPI_Avg_Driving_Range`, `KPI_Avg_Battery_Capacity`, `KPI_Total_Annual_Sales`).
* Viz 2: Category Performance & Distribution (Horizontal Bar Chart).
* Viz 3: Market Share by Manufacturer (Donut Chart).
* Viz 4: Customer Rating Records by EV Category (Bar Chart with 4.09★ Reference Line).
* Viz 5: Annual EV Sales Trend by Model Year (Line Chart with markers).
* Viz 6: Battery Technology Market Share (Pie Chart).
* Viz 7: Electric Vehicle Distribution by Manufacturing Country (Choropleth Map).
* Master Dashboard: Arrange in 1440x900 container grid as specified in [`dashboard_layout_plan.md`](file:///c:/Users/Sanjana/OneDrive/Documents/Skillwallet%20project/Electric_Vehicle_Market_Insights/Tableau/Dashboard_Specification/dashboard_layout_plan.md).

### Step 4: Sign in and Save to Tableau Public
1. Top Menu -> **Server** -> **Tableau Public** -> **Sign In...** (enter your Tableau Public credentials).
2. Click **Server** -> **Tableau Public** -> **Save to Tableau Public As...**
3. Name your workbook: `Electric Vehicle Market Performance & Insights`.
4. Click **Save** -> Tableau will generate the extract and publish it to the cloud.

### Step 5: Obtain and Embed the Public URL
1. Once published, your browser will open the Tableau Public view.
2. Copy the URL from your browser address bar (e.g., `https://public.tableau.com/views/YourWorkbook/Dashboard`).
3. In the Flask web application, click the **"Configure Embed URL"** button on the home page, paste your public URL, and click **Save & Update View**. The embedded container will immediately render your live interactive visualization!

---

## 5. Summary of Empirical Findings

| Market Dimension | Key Empirical Metric | Strategic Business Implication |
| :--- | :--- | :--- |
| **Fleet Scale** | **299,999 records** (17,980 unique models) | Mature multi-segment market covering micro-mobility to heavy freight. |
| **OEM Competition** | **200 distinct OEMs** (Top OEM VoltWorks = 0.54% share) | Highly decentralized market; no monopoly exists. |
| **Dominant Categories** | Two-Wheelers (9.83%), Sedans (8.62%), Hatchbacks (8.57%) | Mass adoption is driven by affordable urban transit and commuter sedans. |
| **Battery Duopoly** | **NMC (33.84%)** and **LFP (32.05%)** = 65.89% share | LFP leads fleet durability (2,501 cycles); NMC leads energy density. |
| **Emerging Tech** | **Solid-State (2,998 cycles)**; **Sodium-Ion (9.98% share)** | Solid-state captures the luxury tier; sodium-ion de-risks entry supply chains. |
| **Capital Cost Driver** | Battery capacity vs price: **r = +0.8373** | Battery pack kWh is the single greatest manufacturing cost component. |
| **Customer Satisfaction** | Clustered between **4.085★ and 4.094★** (Fleet Avg: 4.09★) | Universal satisfaction parity across budget and luxury segments. |
| **Assembly Geography** | Asian nations (India, China, S. Korea, Vietnam, Japan) = **50.13%** | Asia is the global manufacturing engine for electric mobility. |
| **Climate Decarbonization**| Electric Buses save **9.04 tons CO2/yr** (3x passenger cars) | Subsidies should prioritize transit buses for maximum carbon abatement ROI. |

---

## 6. Empirical Performance Testing Results

Actual performance benchmarks recorded on production hardware:
* **Dataset Ingestion Speed:** 299,999 records loaded in **0.899 seconds** (Throughput: 333,676 rows/second).
* **In-Memory RAM Footprint:** **228.57 MB**.
* **Fleet KPI Aggregation Latency:** **28.83 ms**.
* **Single Filter Latency:** **12.10 ms to 35.65 ms**.
* **Multi-Dimensional Complex Filter Latency:** **3.14 ms to 6.29 ms**.
* **Web Server Status:** 100% of Flask routes verified with **HTTP 200 OK**.
* **Browser Compatibility:** Certified across Google Chrome, Microsoft Edge, Mozilla Firefox, and Apple Safari.

---

## 7. Project Completion Checklist

- [x] Phase 1 Data Profiling & Quality Audit (`dataset_profile.csv`, `data_quality_report.txt`)
- [x] Phase 1 Deduplication & Domain Imputation (`cleaned_ev_dataset.csv`)
- [x] Phase 1 14-Topic Exploratory Data Analysis (`ev_eda_analysis.ipynb`, `ev_eda_summary.txt`)
- [x] Phase 1 Tableau Data Dictionary (`tableau_data_dictionary.xlsx`)
- [x] Phase 2 Tableau Visualization Specifications (All 6 KPIs and 7 Visualizations)
- [x] Phase 2 Master Dashboard Layout Plan (1440x900 container grid)
- [x] Phase 2 Interactive Filter & Cross-Filtering Engine
- [x] Phase 2 7-Scene Tableau Story Architecture
- [x] Phase 2 Quality Testing Protocol (25-point QA checklist)
- [x] Phase 3 Python Flask Web Application (`app.py`, templates, responsive CSS, main.js)
- [x] Phase 3 Empirical Performance Testing & Benchmarking Report
- [x] Phase 3 Comprehensive 25-Section Academic Project Report (`.docx` and `.md`)
- [x] Phase 3 5–7 Minute Screen-Sharing Oral Presentation Script (`.docx` and `.md`)
- [x] Phase 3 Comprehensive Viva Voce Preparation Guide (28 Questions & Answers)
- [x] Phase 3 Final Deliverables Organization into `Electric_Vehicle_Market_Insights/`
