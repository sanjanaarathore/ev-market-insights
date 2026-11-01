import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc_dir = "Electric_Vehicle_Market_Insights/Documentation"
docx_path = os.path.join(doc_dir, "Presentation_Script.docx")
md_path = os.path.join(doc_dir, "Presentation_Script.md")

print("Generating 5-7 Minute Presentation Script (DOCX & MD)...")

doc = docx.Document()
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

NAVY = RGBColor(31, 78, 120)
GRAY = RGBColor(89, 89, 89)
BLACK = RGBColor(30, 30, 30)

# Title
p_title = doc.add_paragraph()
r_title = p_title.add_run("ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS")
r_title.font.name = 'Arial'
r_title.font.size = Pt(22)
r_title.font.bold = True
r_title.font.color.rgb = NAVY
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER

p_sub = doc.add_paragraph()
r_sub = p_sub.add_run("5–7 Minute Screen-Sharing Oral Presentation Script & Slide-by-Slide Delivery Guide")
r_sub.font.name = 'Arial'
r_sub.font.size = Pt(12)
r_sub.font.italic = True
r_sub.font.color.rgb = GRAY
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(24)

# Script content breakdown
script_sections = [
    {
        "time": "0:00 - 0:45 (45 sec)",
        "heading": "1. Introduction & Team Details",
        "visual": "Slide 1: Title Slide & Web App Landing Page Hero Banner",
        "speaker": "Hello everyone, and welcome. Today, I am proud to present our project titled 'Electric Vehicle Market Performance & Insights'. My name is [Your Name], Senior Data Analyst and Project Lead. Over the past several months, our team set out to construct an end-to-end data intelligence system that explores the performance, battery architectures, commercial sales, and environmental impact of the global electric vehicle fleet. In this 6-minute demonstration, I will walk you through our data pipeline, our enterprise Tableau Public dashboards, our 7-scene narrative story, and our live Python Flask web application."
    },
    {
        "time": "0:45 - 1:30 (45 sec)",
        "heading": "2. Problem Statement",
        "visual": "Slide 2: Industry Pain Points & Research Questions",
        "speaker": "The automotive industry is in the midst of its greatest transition since the assembly line. Yet, despite massive investments, market stakeholders suffer from significant information asymmetry. Automotive executives, supply chain planners, and municipal policymakers often lack verified, cross-brand data on questions like: Which battery chemistries actually deliver superior longevity? Is the market dominated by a few monopolistic OEMs, or is competition decentralized? And crucially, where should climate capital be allocated to achieve the highest carbon reduction per dollar? Our project answers these questions using direct, empirical data analysis."
    },
    {
        "time": "1:30 - 2:15 (45 sec)",
        "heading": "3. Dataset Overview & Engineering Scope",
        "visual": "Slide 3: Dataset Architecture & 37-Column Mindmap",
        "speaker": "Let's look at the data. We evaluated a standardized global database comprising 300,000 electric vehicle records spanning 37 technical, financial, and environmental parameters. The dataset represents vehicles manufactured between 2018 and 2026, across 15 vehicle categories—from two-wheeler scooters and family hatchbacks to multi-ton electric freight trucks and transit buses. The fleet encompasses 200 distinct global automotive manufacturers assembled in 10 sovereign nations across 7 continental regions. Every record tracks critical attributes such as gross battery capacity, cathode chemistry, EPA/WLTP driving range, DC fast charging duration, retail price, crash safety ratings, and annual carbon savings."
    },
    {
        "time": "2:15 - 3:15 (60 sec)",
        "heading": "4. Data Preprocessing & Quality Assurance",
        "visual": "Slide 4: Data Quality Audit & Methodology Flowchart",
        "speaker": "Before building any dashboards, our top priority was uncompromising data integrity. We conducted an exhaustive audit of both the training and testing partitions. First, row-level deduplication identified exactly one genuine duplicate record in the training set—vehicle ID EV229214, which was duplicated identically across all 37 fields. We safely dropped this duplicate, leaving exactly 199,999 unique train records and 100,000 test records. Second, we confirmed zero missing values across 32 features, while the remaining 5 features had random missingness between 1% and 3%. Rather than arbitrary global imputation, we applied domain-driven median imputation: battery cycle life was imputed using medians by battery chemistry; infotainment screen size and sales were imputed using medians by vehicle category. Finally, we proved the physical realism of the data: testing the formula 'Efficiency equals battery capacity times 1000 divided by range' revealed a mean difference of only 0.027 Wh/km, confirming engineering consistency."
    },
    {
        "time": "3:15 - 4:15 (60 sec)",
        "heading": "5. Tableau Visualizations & Master Dashboard Demonstration",
        "visual": "Slide 5: Live Screen-Share of Master Tableau Dashboard (1440x900)",
        "speaker": "Now, let me share my screen and direct your attention to our master Tableau Public dashboard: 'ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS'. At the top, our executive scorecard immediately reveals key fleet metrics: 299,999 total vehicle configuration records representing 17,980 unique commercial models, 200 active OEMs, an average certified driving range of 324.5 km, an average battery capacity of 78.2 kWh, and over 2.34 billion cumulative sales units. Moving into the visual body: On the left, our horizontal bar chart shows category distribution, where Two-Wheeler Scooters lead with 29,478 models, followed by Sedans, Hatchbacks, and Compact SUVs. Next to it, our dual-axis donut chart visualizes OEM market share across 200 manufacturers, clearly proving that no single brand dominates the market—the top OEM, VoltWorks, accounts for only 0.54% of models. Below, our line chart demonstrates stable annual deliveries of approximately 258 million units per model vintage, our pie chart shows the NMC and LFP battery duopoly commanding nearly 66% of vehicles, and our geographic choropleth map illustrates that Asian hubs assemble over 50% of the world's electric vehicles."
    },
    {
        "time": "4:15 - 5:15 (60 sec)",
        "heading": "6. Dashboard Interactivity & 7-Scene Tableau Story",
        "visual": "Slide 6: Live Interaction Demo (Filtering by Category and Country) + Story Navigator",
        "speaker": "What makes this dashboard powerful is its interactive cross-filtering engine. Let's see this in action: if I click on 'Electric Bus' in the category chart, watch how the entire dashboard instantly updates! Our KPI cards recalculate to show an average battery capacity of 300.2 kWh and an average price of $274,000. If I filter by 'Germany' on our geographic map, we instantly isolate German-assembled models. Beyond the single-view dashboard, we authored a 7-scene Tableau Story that walks stakeholders step-by-step through: Market Overview, Category Dynamics, OEM Competition, Battery Chemistry tradeoffs, Sales Trajectories, Global Assembly Geography, and Strategic Decarbonization ROI."
    },
    {
        "time": "5:15 - 6:00 (45 sec)",
        "heading": "7. Important Empirical Findings & Business Implications",
        "visual": "Slide 7: Strategic Insights Matrix & Business ROI Summary",
        "speaker": "Our analysis yielded three transformative business takeaways. First, Commercial Electrification is the single highest-impact climate lever: one electric bus avoids 9.04 metric tons of CO2 annually—triple the impact of a passenger car (3.04 tons/yr). Municipal transit electrification delivers the greatest return on carbon reduction capital. Second, Battery Sizing Dictates Capital Cost: battery pack capacity correlates at an overwhelming r = +0.8373 with vehicle retail price. Automakers must prioritize aerodynamic efficiency and rapid charging rather than bloating battery packs. Third, Customer Satisfaction is Universally Clustered at 4.09 out of 5 stars across all 15 segments, proving that budget two-wheelers fulfill commuter expectations just as effectively as six-figure luxury sedans."
    },
    {
        "time": "6:00 - 6:30 (30 sec)",
        "heading": "8. Flask Web Integration & Conclusion",
        "visual": "Slide 8: Flask Web Portal & Architecture Diagram",
        "speaker": "Finally, we deployed our findings into a production-grade Python Flask web application. It features live REST APIs, an interactive vehicle segment comparator, and an embedded Tableau Public container utilizing Tableau's Embedding API v3. In conclusion, this project provides a rigorous, verified, and interactive data platform connecting data analytics, business intelligence, and full-stack web engineering. Thank you for your time, and I am now excited to open the floor for questions."
    }
]

md_content = "# ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS\n## 5–7 MINUTE SCREEN-SHARING PRESENTATION SCRIPT\n\n"

for s in script_sections:
    h = doc.add_heading(f"{s['heading']} ({s['time']})", level=2)
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    for r in h.runs:
        r.font.name = 'Arial'
        r.font.color.rgb = NAVY
        r.font.size = Pt(13)
        r.font.bold = True
    
    p_v = doc.add_paragraph()
    r_v = p_v.add_run(f"Visual Display / Action: {s['visual']}")
    r_v.font.name = 'Arial'
    r_v.font.size = Pt(9.5)
    r_v.font.italic = True
    r_v.font.color.rgb = GRAY
    
    p_spk = doc.add_paragraph()
    p_spk.paragraph_format.space_after = Pt(12)
    p_spk.paragraph_format.line_spacing = 1.15
    r_spk = p_spk.add_run(f'"{s["speaker"]}"')
    r_spk.font.name = 'Arial'
    r_spk.font.size = Pt(10.5)
    r_spk.font.color.rgb = BLACK
    
    md_content += f"### {s['heading']} ({s['time']})\n"
    md_content += f"**Visual Display / Action:** *{s['visual']}*\n\n"
    md_content += f'> "{s["speaker"]}"\n\n---\n\n'

doc.save(docx_path)
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Presentation Script (DOCX) saved to: {docx_path}")
print(f"Presentation Script (MD) saved to: {md_path}")

