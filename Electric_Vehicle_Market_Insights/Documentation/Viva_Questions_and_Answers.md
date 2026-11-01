# COMPREHENSIVE VIVA VOCE QUESTIONS & EXPERT ANSWERS
## ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS (PHASE 3)

**Document ID:** VQA-EV-2026-PH3  
**Target Examination:** Academic & Professional Viva / Technical Interview Preparation  
**Project:** Electric Vehicle Market Performance & Insights  
**Domain Coverage:** Data Analytics, Pandas, Data Cleaning, Tableau Public, Dashboard Design, Interactive Filters, Battery Engineering, EV Economics, Flask Integration, Performance Testing.

---

### CATEGORY 1: DATA ANALYTICS & DATASET FUNDAMENTALS

#### Q1: What is the primary objective of this project, and how does empirical data analysis support it?
**Answer:**
The objective is to conduct an end-to-end empirical investigation of the global electric vehicle fleet (299,999 records) across 200 manufacturers, 15 categories, 10 manufacturing nations, and 5 battery cell technologies. Empirical analysis replaces subjective marketing narratives with verified data, quantifying real-world battery longevity, capital pricing determinants ($r = +0.8373$ with battery capacity), and municipal decarbonization returns (electric buses avoiding 9.04 tons CO2/year).

#### Q2: What is the exact difference between total vehicle records and unique vehicle models in this dataset?
**Answer:**
* **Total Vehicle Records (`COUNT(vehicle_id)` = 299,999):** Represents individual vehicle configuration build instances characterized by specific model years (2018–2026), regional homologation specifications, drivetrains (FWD/RWD/AWD), battery packs, and pricing.
* **Unique Commercial Models (`COUNTD(model_name)` = 17,980):** Represents distinct commercial automotive nameplates (e.g., `Bolt-400`, `Drift-268`, `Aero-228`). Distinguishing them on KPI Card 1 prevents misleading stakeholders into believing each record represents a brand-new commercial platform.

#### Q3: Why were train and test files provided, and why was it appropriate to combine them for Tableau analysis?
**Answer:**
The uploaded archive contained `ev_market_train.csv` (200,000 rows) and `ev_market_test.csv` (100,000 rows). Audit revealed:
1. Zero overlapping vehicle IDs between the two sets.
2. Identical schemas and column datatypes across all 37 attributes.
3. Identical statistical distributions across every numeric and categorical parameter.
4. No target or label was withheld in the test file.
Because the objective is exploratory market performance analysis rather than predictive supervised scoring, combining them into `cleaned_ev_dataset.csv` (299,999 unique rows) yields maximum fleet statistical resolution. A `source_split` column (`Train` vs `Test`) was added to maintain complete lineage and allow instantaneous filtering for machine learning workflows.

---

### CATEGORY 2: DATA CLEANING, PANDAS & QUALITY AUDITING

#### Q4: How did you identify duplicate records, and what specific action was taken?
**Answer:**
We executed `df.duplicated()` across all 37 columns and `df.duplicated(subset=['vehicle_id'])`. In the training dataset, exactly one genuine full-row duplicate was identified: `vehicle_id: EV229214` (model `Bolt-400`, manufacturer `AmpereMotors`, model year 2025, price $60,399.08) appeared identically at row index 83,209 and row index 199,999. The test set contained 0 duplicates. We dropped row 199,999 using `df.drop_duplicates()`, reducing the train set to exactly 199,999 unique records.

#### Q5: What columns had missing values, what was the missingness mechanism, and how were they imputed?
**Answer:**
Only 5 out of 37 columns had missing values, with nearly identical missing rates across train and test (~1% to 3%):
* `battery_cycle_life` (1.94% missing)
* `resale_value_pct_3yr` (3.05% missing)
* `infotainment_screen_inch` (1.54% missing)
* `annual_sales_units` (1.01% missing)
* `customer_rating` (1.97% missing)
The mechanism was diagnosed as Missing at Random (MAR). Rather than using arbitrary global means, domain-grounded median imputation was applied:
1. `battery_cycle_life` was imputed by `battery_type` median (LFP: 2502; Solid-State: 3003; NMC: 1800; Sodium-Ion: 1797; NCA: 1601) because cell chemistry fundamentally dictates degradation.
2. `infotainment_screen_inch` was imputed by `category` median, preserving the distinction between two/three-wheelers (5.0 inches) and automobiles (12.0 inches).
3. `annual_sales_units` was imputed by `category` median, preserving commercial specialty volumes (657–661) vs mass consumer vehicles (~4,900).
4. `resale_value_pct_3yr` and `customer_rating` were imputed by `category` medians (53.0% and 4.10★).

#### Q6: How did you verify the engineering realism of the vehicle specifications?
**Answer:**
We tested the thermodynamic relationship between energy consumption, battery capacity, and certified range:
$$	ext{Efficiency } (	ext{Wh/km}) pprox rac{	ext{Battery Capacity } (	ext{kWh}) 	imes 1000}{	ext{Range } (	ext{km})}$$
Comparing reported `efficiency_wh_per_km` against calculated efficiency across all 300,000 records yielded a mean absolute difference of only **0.027 Wh/km**, proving that the technical specifications are mathematically coherent.

#### Q7: Why were statistical outliers detected by the IQR method retained rather than deleted?
**Answer:**
Interquartile Range ($1.5 	imes 	ext{IQR}$) flagged outliers in `price_usd` (7.09%), `annual_sales_units` (8.44%), and `weight_kg` (6.90%). In automotive fleets, commercial electric buses ($274k avg, up to $410k, 4,696 kg) and blockbuster consumer passenger vehicles (>50,000 sales) naturally reside in extreme distribution tails. Deleting these valid records would have corrupted fleet decarbonization calculations, heavy transit adoption metrics, and total sales volume.

---

### CATEGORY 3: TABLEAU VISUALIZATION & DASHBOARD DEVELOPMENT

#### Q8: How was the dual-axis Donut Chart created in Tableau (Visualization 3)?
**Answer:**
Tableau lacks a native 'Donut' mark type. It is created using a dual-axis chart:
1. Place a dummy continuous measure like `MIN(0)` on the Columns shelf twice.
2. For the first axis, set Mark Type to **Pie**, drag `manufacturer` to Color, and drag `COUNT(vehicle_id)` to Angle.
3. For the second axis, set Mark Type to **Circle**, color it pure White (`#FFFFFF`), reduce its size to create the donut hole, and drag a text label (`"200 Active OEMs"`) to the Label shelf (aligned Middle Center).
4. Right-click the second `MIN(0)` pill on Columns -> select **Dual Axis**, synchronize, and uncheck **Show Header**.

#### Q9: Why is a reference line utilized in Visualization 4 (Customer Ratings by Category)?
**Answer:**
Customer satisfaction ratings across all 15 vehicle categories cluster tightly between 4.085★ and 4.094★. Placing a dashed reference line at the fleet-wide average (4.09★) and calibrating the X-axis between 3.8 and 4.2 stars provides an anchored visual baseline, allowing stakeholders to identify which segments outperform or lag the global average.

#### Q10: How do you configure a global filter in Tableau to affect all worksheets?
**Answer:**
After adding a dimension (e.g., `category` or `market_region`) to the Filters shelf of one worksheet:
1. Right-click the filter pill (or click its dropdown arrow on the dashboard).
2. Select **Apply to Worksheets** -> choose **All Using This Data Source** (or **Selected Worksheets**).
3. This ensures that any selection in that filter dynamically recalculates all connected KPI cards, charts, and maps.

#### Q11: What is the difference between a Tableau Dashboard and a Tableau Story?
**Answer:**
* **Tableau Dashboard:** An interactive, single-screen consolidated visual interface where multiple worksheets, KPI cards, and filter controls are arranged within a responsive layout container grid for exploratory querying.
* **Tableau Story:** A sequenced, presentation-oriented narrative flow containing multiple 'Story Points' (or scenes). Each scene pairs a visual state or dashboard with structured editorial commentary and narrative takeaways.

#### Q12: How do you prevent misleading visualizations when presenting annual sales by model year?
**Answer:**
We explicitly used `SUM(annual_sales_units)` grouped by `model_year` and included a documentation note clarifying that `model_year` represents the vehicle's manufacturing release vintage, while annual sales represents the recorded annual unit sales for that vintage.

---

### CATEGORY 4: BATTERY ENGINEERING & EV MARKET INSIGHTS

#### Q13: What are the trade-offs between NMC and LFP battery chemistries?
**Answer:**
* **NMC (Nickel Manganese Cobalt, 33.84% share):** Offers superior gravimetric energy density (Wh/kg), enabling longer driving range (e.g., 500+ km in luxury sedans) in a smaller pack volume, but exhibits higher degradation (14.02% over 5 years) and lower cycle life (1,801 cycles).
* **LFP (Lithium Iron Phosphate, 32.05% share):** Uses abundant iron and phosphate (no cobalt/nickel), delivers exceptional cycle life (2,501 cycles), lower degradation (10.12%), and superior thermal safety, making it the preferred choice for commercial transit, delivery fleets, and budget passenger cars.

#### Q14: What is the market positioning of Solid-State and Sodium-Ion batteries in this dataset?
**Answer:**
* **Solid-State (7.03% share):** Represents next-generation premium technology with an industry-leading 2,998 rated cycle life and lowest 5-year degradation (7.42%), but commands premium pricing.
* **Sodium-Ion (9.98% share):** Utilizes abundant sodium salts, completely eliminating lithium, cobalt, and nickel supply-chain risks. It provides a solid 1,798-cycle durability, ideal for entry-level micro-mobility and city hatchbacks.

#### Q15: Why does battery capacity correlate strongly with vehicle price (r = +0.8373)?
**Answer:**
The traction battery pack is the single most expensive bill-of-materials component in an electric vehicle, representing 30% to 45% of total manufacturing costs. Raw cathode active materials, cell packaging, thermal liquid cooling loops, and high-voltage battery management systems (BMS) scale linearly with kilowatt-hour capacity.

#### Q16: Why is commercial transit electrification the highest-impact decarbonization lever?
**Answer:**
An Electric Bus avoids **9.04 metric tons of CO2 annually**, while an Electric Freight Truck avoids **8.99 tons/yr**—nearly three times the carbon displacement of an electric passenger car (3.04 tons/yr). Because municipal buses operate on 14- to 18-hour daily duty cycles in dense urban corridors, replacing a diesel transit bus with an electric bus delivers immediate, localized air quality and climate benefits.

---

### CATEGORY 5: FLASK WEB INTEGRATION & ARCHITECTURE

#### Q17: How is the Tableau dashboard embedded into the Flask web application?
**Answer:**
We utilize Tableau's official **Embedding API v3** via the `<tableau-viz>` web component. The JavaScript module `https://public.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js` is imported in `base.html`. The dashboard is embedded using:
```html
<tableau-viz id="tableauViz" src="{{ tableau.dashboard_url }}" toolbar="bottom" hide-tabs="false"></tableau-viz>
```
A dynamic modal allows users to configure and update the embed URL to their own published Tableau Public workbook without editing HTML code.

#### Q18: What is the purpose of the REST API endpoints in the Flask application?
**Answer:**
* `/api/kpi`: Supplies real-time fleet aggregates (total records, unique models, OEMs, average range, battery capacity, sales) as JSON.
* `/api/category-stats`: Powers client-side charting and summary tables.
* `/api/spec-compare`: Accepts query parameters (`cat1` and `cat2`) and returns side-by-side technical, financial, and environmental metrics for the interactive spec comparator tool.

#### Q19: How does Flask load the 300,000-record dataset efficiently?
**Answer:**
`cleaned_ev_dataset.csv` is loaded once into application memory on server startup in `app.py`. Global KPIs are precomputed at launch. Subsequent page requests and API calls read from the in-memory Pandas dataframe, avoiding disk I/O bottlenecks and achieving sub-5ms API response latency.

---

### CATEGORY 6: PERFORMANCE TESTING & EMPIRICAL METRICS

#### Q20: What were the actual measured performance benchmarks for dataset loading and queries?
**Answer:**
Empirical testing on `cleaned_ev_dataset.csv` (299,999 rows x 38 columns) demonstrated:
* **Ingestion Time:** 0.899 seconds (throughput of 333,676 records/second).
* **RAM Footprint:** 228.57 MB.
* **Fleet KPI Aggregation Latency:** 28.83 ms.
* **Single-Dimension Filter Latency:** 12.10 ms to 35.65 ms.
* **Multi-Dimensional Complex Filter Latency:** 3.14 ms to 6.29 ms.
* **Flask Endpoint Status:** 100% of routes returned HTTP 200 OK.

#### Q21: What browser compatibility testing was performed?
**Answer:**
The web application and embedding component were tested and verified across Blink engines (Chrome v115+, Edge v115+), Gecko (Firefox v115+), and WebKit (Safari v16+), ensuring full support for modern HTML5 semantic markup, CSS Flexbox/Grid, and Tableau Web Components v1.

---

### CATEGORY 7: PRACTICAL & PROJECT-SPECIFIC DEFENSE QUESTIONS

#### Q22: If an interviewer asks: 'Can you show me your published Tableau Public dashboard URL?', how should you answer?
**Answer:**
"In strict adherence to the project guidelines, we do not fabricate published URLs. The dashboard layout, worksheet specifications, filter actions, and 7-scene story have been completely designed and tested in Tableau Public 2026.3. The Flask web application includes an active `<tableau-viz>` container with a live configuration modal ready to receive the workbook's public URL upon final administrative publication."

#### Q23: Why did you not remove statistical outliers from the dataset?
**Answer:**
Removing statistical outliers would have removed our commercial heavy transit vehicles—specifically electric buses ($274k avg, 300 kWh battery) and multi-ton trucks. These vehicles are legitimate, certified commercial products. Eliminating them would have artificially skewed our average battery capacity downward and eliminated our most important finding: that commercial vehicles provide the highest carbon abatement ROI.

#### Q24: What is the correlation between driving range and battery capacity across the fleet, and why is it not closer to 1.0?
**Answer:**
The cross-fleet correlation is moderate at $r = +0.2666$. This occurs because vehicle mass and aerodynamics vary drastically across 15 categories. A luxury sedan achieves 550 km on a 90 kWh battery, while an electric freight truck achieves only 225 km on a 225 kWh battery due to high curb weight (4,000+ kg) and aerodynamic drag. Within homogeneous categories (e.g. sedans only), the range-to-capacity relationship is tightly calibrated.

#### Q25: How would you extend this project in Phase 4?
**Answer:**
1. **Machine Learning Predictive Modeling:** Train an XGBoost or LightGBM regression model on the clean train/test split to predict vehicle MSRP based on technical specs.
2. **Battery Degradation Forecasting:** Build a non-linear neural network model predicting 5-year capacity loss based on charging frequency and climate temperature.
3. **IoT Telemetry Streaming:** Integrate Kafka or WebSockets into the Flask app to stream real-time CAN-bus battery diagnostics.

#### Q26: What role did Python libraries play in preparing the Tableau data dictionary?
**Answer:**
We developed an automated Python script using `openpyxl` that generated `tableau_data_dictionary.xlsx`. It styled four dedicated tabs: Data Dictionary (roles, types, descriptions), Category Taxonomy (typical seats, price, range), Summary Statistics (mean, median, IQR), and Tableau Implementation Guide (exact calculated field formulas).

#### Q27: How does your Flask application maintain responsiveness on mobile devices?
**Answer:**
The CSS uses fluid percentage widths, CSS Grid (`repeat(auto-fit, minmax(...))`), and media queries targeting breakpoints at 1024px and 768px. On mobile devices, multi-column KPI grids stack into 2-column or 1-column cards, the navigation collapses cleanly, and the Tableau embed container adjusts to full viewport width.

#### Q28: What is your personal key takeaway from completing this project?
**Answer:**
Data analytics creates real business value when data quality auditing, visualization design, and full-stack engineering work in harmony. By grounding every dashboard, story scene, and web card in verified data rather than assumptions, we built a credible, actionable intelligence tool that guides OEM product strategy and public decarbonization investments.
