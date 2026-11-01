# ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS
## 5–7 MINUTE SCREEN-SHARING PRESENTATION SCRIPT

### 1. Introduction & Team Details (0:00 - 0:45 (45 sec))
**Visual Display / Action:** *Slide 1: Title Slide & Web App Landing Page Hero Banner*

> "Hello everyone, and welcome. Today, I am proud to present our project titled 'Electric Vehicle Market Performance & Insights'. My name is [Your Name], Senior Data Analyst and Project Lead. Over the past several months, our team set out to construct an end-to-end data intelligence system that explores the performance, battery architectures, commercial sales, and environmental impact of the global electric vehicle fleet. In this 6-minute demonstration, I will walk you through our data pipeline, our enterprise Tableau Public dashboards, our 7-scene narrative story, and our live Python Flask web application."

---

### 2. Problem Statement (0:45 - 1:30 (45 sec))
**Visual Display / Action:** *Slide 2: Industry Pain Points & Research Questions*

> "The automotive industry is in the midst of its greatest transition since the assembly line. Yet, despite massive investments, market stakeholders suffer from significant information asymmetry. Automotive executives, supply chain planners, and municipal policymakers often lack verified, cross-brand data on questions like: Which battery chemistries actually deliver superior longevity? Is the market dominated by a few monopolistic OEMs, or is competition decentralized? And crucially, where should climate capital be allocated to achieve the highest carbon reduction per dollar? Our project answers these questions using direct, empirical data analysis."

---

### 3. Dataset Overview & Engineering Scope (1:30 - 2:15 (45 sec))
**Visual Display / Action:** *Slide 3: Dataset Architecture & 37-Column Mindmap*

> "Let's look at the data. We evaluated a standardized global database comprising 300,000 electric vehicle records spanning 37 technical, financial, and environmental parameters. The dataset represents vehicles manufactured between 2018 and 2026, across 15 vehicle categories—from two-wheeler scooters and family hatchbacks to multi-ton electric freight trucks and transit buses. The fleet encompasses 200 distinct global automotive manufacturers assembled in 10 sovereign nations across 7 continental regions. Every record tracks critical attributes such as gross battery capacity, cathode chemistry, EPA/WLTP driving range, DC fast charging duration, retail price, crash safety ratings, and annual carbon savings."

---

### 4. Data Preprocessing & Quality Assurance (2:15 - 3:15 (60 sec))
**Visual Display / Action:** *Slide 4: Data Quality Audit & Methodology Flowchart*

> "Before building any dashboards, our top priority was uncompromising data integrity. We conducted an exhaustive audit of both the training and testing partitions. First, row-level deduplication identified exactly one genuine duplicate record in the training set—vehicle ID EV229214, which was duplicated identically across all 37 fields. We safely dropped this duplicate, leaving exactly 199,999 unique train records and 100,000 test records. Second, we confirmed zero missing values across 32 features, while the remaining 5 features had random missingness between 1% and 3%. Rather than arbitrary global imputation, we applied domain-driven median imputation: battery cycle life was imputed using medians by battery chemistry; infotainment screen size and sales were imputed using medians by vehicle category. Finally, we proved the physical realism of the data: testing the formula 'Efficiency equals battery capacity times 1000 divided by range' revealed a mean difference of only 0.027 Wh/km, confirming engineering consistency."

---

### 5. Tableau Visualizations & Master Dashboard Demonstration (3:15 - 4:15 (60 sec))
**Visual Display / Action:** *Slide 5: Live Screen-Share of Master Tableau Dashboard (1440x900)*

> "Now, let me share my screen and direct your attention to our master Tableau Public dashboard: 'ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS'. At the top, our executive scorecard immediately reveals key fleet metrics: 299,999 total vehicle configuration records representing 17,980 unique commercial models, 200 active OEMs, an average certified driving range of 324.5 km, an average battery capacity of 78.2 kWh, and over 2.34 billion cumulative sales units. Moving into the visual body: On the left, our horizontal bar chart shows category distribution, where Two-Wheeler Scooters lead with 29,478 models, followed by Sedans, Hatchbacks, and Compact SUVs. Next to it, our dual-axis donut chart visualizes OEM market share across 200 manufacturers, clearly proving that no single brand dominates the market—the top OEM, VoltWorks, accounts for only 0.54% of models. Below, our line chart demonstrates stable annual deliveries of approximately 258 million units per model vintage, our pie chart shows the NMC and LFP battery duopoly commanding nearly 66% of vehicles, and our geographic choropleth map illustrates that Asian hubs assemble over 50% of the world's electric vehicles."

---

### 6. Dashboard Interactivity & 7-Scene Tableau Story (4:15 - 5:15 (60 sec))
**Visual Display / Action:** *Slide 6: Live Interaction Demo (Filtering by Category and Country) + Story Navigator*

> "What makes this dashboard powerful is its interactive cross-filtering engine. Let's see this in action: if I click on 'Electric Bus' in the category chart, watch how the entire dashboard instantly updates! Our KPI cards recalculate to show an average battery capacity of 300.2 kWh and an average price of $274,000. If I filter by 'Germany' on our geographic map, we instantly isolate German-assembled models. Beyond the single-view dashboard, we authored a 7-scene Tableau Story that walks stakeholders step-by-step through: Market Overview, Category Dynamics, OEM Competition, Battery Chemistry tradeoffs, Sales Trajectories, Global Assembly Geography, and Strategic Decarbonization ROI."

---

### 7. Important Empirical Findings & Business Implications (5:15 - 6:00 (45 sec))
**Visual Display / Action:** *Slide 7: Strategic Insights Matrix & Business ROI Summary*

> "Our analysis yielded three transformative business takeaways. First, Commercial Electrification is the single highest-impact climate lever: one electric bus avoids 9.04 metric tons of CO2 annually—triple the impact of a passenger car (3.04 tons/yr). Municipal transit electrification delivers the greatest return on carbon reduction capital. Second, Battery Sizing Dictates Capital Cost: battery pack capacity correlates at an overwhelming r = +0.8373 with vehicle retail price. Automakers must prioritize aerodynamic efficiency and rapid charging rather than bloating battery packs. Third, Customer Satisfaction is Universally Clustered at 4.09 out of 5 stars across all 15 segments, proving that budget two-wheelers fulfill commuter expectations just as effectively as six-figure luxury sedans."

---

### 8. Flask Web Integration & Conclusion (6:00 - 6:30 (30 sec))
**Visual Display / Action:** *Slide 8: Flask Web Portal & Architecture Diagram*

> "Finally, we deployed our findings into a production-grade Python Flask web application. It features live REST APIs, an interactive vehicle segment comparator, and an embedded Tableau Public container utilizing Tableau's Embedding API v3. In conclusion, this project provides a rigorous, verified, and interactive data platform connecting data analytics, business intelligence, and full-stack web engineering. Thank you for your time, and I am now excited to open the floor for questions."

---

