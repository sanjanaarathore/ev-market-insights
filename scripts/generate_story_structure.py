import os

output_path = r"deliverables/tableau_story_structure.md"
root_path = r"tableau_story_structure.md"

content = """# TABLEAU STORY STRUCTURE: GLOBAL ELECTRIC VEHICLE INTELLIGENCE
## ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS (PHASE 2)

**Document ID:** TSS-EV-2026-PH2  
**Story Title:** Global EV Market Evolution & Technology Trajectory  
**Story Size:** 1366 x 768 px (Optimized for Web Presentation & Tableau Public Story Viewer)  
**Story Navigation:** Clean Top Navigator with Story Point Captions

---

## 1. Story Flow & Narrative Architecture

```mermaid
flowchart LR
    S1["Scene 1: Market Overview"] --> S2["Scene 2: Category Dynamics"]
    S2 --> S3["Scene 3: OEM Competition"]
    S3 --> S4["Scene 4: Battery Chemistries"]
    S4 --> S5["Scene 5: Sales Trajectories"]
    S5 --> S6["Scene 6: Assembly Geography"]
    S6 --> S7["Scene 7: Strategic Conclusions"]
```

---

## 2. Detailed Scene-by-Scene Specifications

---

### SCENE 1: Global EV Market Overview
* **Story Point Caption:** `1. Global EV Market Overview`
* **Visual Displayed:** Full Executive Dashboard (`ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS` with KPI cards + all visualizations in unified view)
* **Narrative Description:**
  > "The global electric vehicle landscape has reached mature commercial scale across 299,999 evaluated vehicle records, spanning 17,980 commercial models, 200 automotive manufacturers, and 10 manufacturing nations. With cumulative annual fleet sales exceeding 2.34 billion units and an average certified driving range of 324.5 km, electrification is penetrating every consumer, commercial, and micro-mobility segment."
* **Key Visual Focus:**
  * Highlight the top KPI scorecard: 299,999 total models, 200 OEMs, 4.09★ customer rating, 324.5 km range, 78.2 kWh battery, 2.34B sales units.
* **Executive Takeaway:**
  * Electric mobility is no longer a niche luxury experiment; it is a multi-segment global industrial reality operating across 7 continental regions.

---

### SCENE 2: Category Performance & Fleet Distribution
* **Story Point Caption:** `2. EV Category Dynamics`
* **Visual Displayed:** `Viz2_Category_Performance` (Full View with segment breakdown and price/range tooltips)
* **Narrative Description:**
  > "Urban and micro-mobility solutions represent the volume foundation of the electric transition. Two-Wheeler Scooters lead global offerings with 29,478 models (9.83% of the fleet), followed closely by Sedans (25,851 models, 8.62%), Hatchbacks (25,713 models, 8.57%), and Compact SUVs (25,706 models, 8.57%). Conversely, heavy commercial vehicles (Electric Buses and Trucks) comprise 9.62% of the fleet but serve high-tonnage transit requirements with battery capacities up to 410 kWh."
* **Key Visual Focus:**
  * Horizontal bar chart ranked by model volume.
  * Contrast between high-volume urban commuters ($2,550 avg MSRP, 105 km range) and heavy commercial transit ($274,380 avg MSRP, 300 kWh battery).
* **Executive Takeaway:**
  * Emerging market adoption is propelled by two- and three-wheelers, while developed economies drive sedan and compact SUV adoption.

---

### SCENE 3: Manufacturer Competition & Portfolio Dispersion
* **Story Point Caption:** `3. OEM Competitive Landscape`
* **Visual Displayed:** `Viz3_Manufacturer_Market_Share` (Donut Chart paired with Top OEM Sales Table)
* **Narrative Description:**
  > "Competition in the global electric vehicle ecosystem is remarkably distributed across 200 automotive OEMs, with no single manufacturer establishing a monopolistic stranglehold. The market leader by model diversity, VoltWorks, accounts for 1,627 models (0.54% share), followed by VelocityGroup (1,611 models), CircuitWorks (1,597 models), and AmpereGroup (1,589 models). By sales volume, AmpereWorks leads with 13.84 million units delivered."
* **Key Visual Focus:**
  * Donut chart demonstrating equitable market share distribution.
  * Central donut hole KPI displaying `200 Active OEMs`.
* **Executive Takeaway:**
  * Low market concentration reflects intense technological competition and regional specialization, creating opportunities for both legacy automakers and agile EV-pureplays.

---

### SCENE 4: Battery Technology Adoption & Durability
* **Story Point Caption:** `4. Battery Technology Matrix`
* **Visual Displayed:** `Viz6_Battery_Technology_Share` (Pie Chart with Durability & Degradation Callouts)
* **Narrative Description:**
  > "Cathode chemistry remains the decisive battleground for vehicle performance and manufacturing cost. NMC (Nickel Manganese Cobalt) and LFP (Lithium Iron Phosphate) together dominate nearly 66% of the global market (NMC: 101,508 models, 33.84%; LFP: 96,137 models, 32.05%). LFP delivers superior longevity (mean 2,501 cycles) and low 5-year degradation (10.12%), while Solid-State technology commands premium adoption with an industry-leading 2,998 rated cycle life."
* **Key Visual Focus:**
  * Clear color-coded pie chart highlighting the 5 chemistries.
  * Callouts contrasting Solid-State durability (3,000 cycles, 7.4% degradation) with Sodium-Ion entry-level adoption (10% market share).
* **Executive Takeaway:**
  * The dual-track strategy of LFP for mass-market/commercial vehicles and NMC/Solid-State for premium long-range vehicles defines the current technological equilibrium.

---

### SCENE 5: Annual EV Sales Trajectory by Model Year
* **Story Point Caption:** `5. Annual Sales Trends`
* **Visual Displayed:** `Viz5_Sales_Trend_by_Model_Year` (Line Chart with Data Point Annotations)
* **Narrative Description:**
  > "Analyzing sales across model release vintages (2018 to 2026) reveals consistent annual delivery volumes, maintaining a steady baseline between 255.2 million and 265.7 million units per vintage. Model year 2019 marks the historical peak with 265.7 million units delivered, while newer vintages (2024: 264.9M; 2025: 257.1M; 2026: 257.2M) demonstrate sustained commercial adoption as fleet renewal cycles continue."
* **Key Visual Focus:**
  * Line chart highlighting stability across model years.
  * Explicit note clarifying that the metric represents total annual unit sales recorded for each model vintage.
* **Executive Takeaway:**
  * Electric vehicle demand is structurally entrenched across successive model generations, unaffected by temporary macroeconomic fluctuations.

---

### SCENE 6: Manufacturing Geography & Sovereign Assembly
* **Story Point Caption:** `6. Global Assembly Hubs`
* **Visual Displayed:** `Viz7_Manufacturing_Country_Map` (Global Choropleth Map with Trade Flow Callouts)
* **Narrative Description:**
  > "Vehicle assembly is distributed across 10 sovereign automotive manufacturing hubs. India leads global assembly with 30,285 models (10.10%), followed by South Korea (30,155 models, 10.05%), China (30,142 models, 10.05%), Vietnam (30,030 models, 10.01%), and the United States (30,029 models, 10.01%). European manufacturing hubs (France, Germany, UK, Sweden) collectively contribute 29.87% of global vehicle models."
* **Key Visual Focus:**
  * Geographic choropleth highlighting the multi-polar nature of EV manufacturing.
  * Balanced distribution (~10% per nation) showing that global supply chains have localized production near major consumption markets.
* **Executive Takeaway:**
  * The emergence of Asian nations (China, India, South Korea, Vietnam) producing over 40% of models highlights Asia's dominance in powertrain and battery manufacturing clusters.

---

### SCENE 7: Strategic Insights & Decarbonization Roadmap
* **Story Point Caption:** `7. Strategic Takeaways & ROI`
* **Visual Displayed:** Executive Summary Scorecard (Multi-metric matrix: Pricing vs Battery Capacity + Customer Satisfaction + CO2 Abatement)
* **Narrative Description:**
  > "Key Strategic Findings from the Global Fleet Analysis:
  > 1. Commercial Electrification is the Highest-Impact Climate Lever: Electric Buses and Trucks abate ~9.0 metric tons of CO2 annually per vehicle—nearly 3x the impact of standard passenger cars (3.04 tons/yr).
  > 2. Battery Sizing Dictates Capital Cost: Installed battery capacity exhibits a dominant r = +0.8373 correlation with vehicle price.
  > 3. Customer Satisfaction is Universally High: Across all 15 segments, average owner satisfaction remains clustered at 4.09★ out of 5.0, confirming strong product-market fit."
* **Key Visual Focus:**
  * Strategic takeaways formatted in high-contrast executive text callouts.
  * Reference to Phase 3 Flask web application deployment.
* **Executive Takeaway:**
  * Transitioning urban municipal transit and commercial delivery fleets yields the fastest return on carbon reduction capital.
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)
with open(root_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated: {output_path} and {root_path}")

