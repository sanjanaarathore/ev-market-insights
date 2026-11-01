import os
import shutil

base_dir = "Electric_Vehicle_Market_Insights"

subdirs = [
    os.path.join(base_dir, "Dataset", "Original"),
    os.path.join(base_dir, "Dataset", "Cleaned"),
    os.path.join(base_dir, "Analysis", "Notebooks"),
    os.path.join(base_dir, "Analysis", "Reports"),
    os.path.join(base_dir, "Tableau", "Dashboard_Specification"),
    os.path.join(base_dir, "Tableau", "Story_Specification"),
    os.path.join(base_dir, "Tableau", "Screenshots"),
    os.path.join(base_dir, "Flask_Web_App", "templates"),
    os.path.join(base_dir, "Flask_Web_App", "static", "css"),
    os.path.join(base_dir, "Flask_Web_App", "static", "js"),
    os.path.join(base_dir, "Flask_Web_App", "static", "img"),
    os.path.join(base_dir, "Documentation")
]

for d in subdirs:
    os.makedirs(d, exist_ok=True)
    print(f"Directory verified: {d}")

# Copy Dataset files
if os.path.exists("archive/ev_market_train.csv"):
    shutil.copy2("archive/ev_market_train.csv", os.path.join(base_dir, "Dataset", "Original", "ev_market_train.csv"))
    shutil.copy2("archive/ev_market_test.csv", os.path.join(base_dir, "Dataset", "Original", "ev_market_test.csv"))
    print("Original datasets copied.")

if os.path.exists("cleaned_ev_dataset.csv"):
    shutil.copy2("cleaned_ev_dataset.csv", os.path.join(base_dir, "Dataset", "Cleaned", "cleaned_ev_dataset.csv"))
    if os.path.exists("cleaned_data/cleaned_ev_train.csv"):
        shutil.copy2("cleaned_data/cleaned_ev_train.csv", os.path.join(base_dir, "Dataset", "Cleaned", "cleaned_ev_train.csv"))
        shutil.copy2("cleaned_data/cleaned_ev_test.csv", os.path.join(base_dir, "Dataset", "Cleaned", "cleaned_ev_test.csv"))
    print("Cleaned datasets copied.")

# Copy Notebooks & Analysis
if os.path.exists("ev_eda_analysis.ipynb"):
    shutil.copy2("ev_eda_analysis.ipynb", os.path.join(base_dir, "Analysis", "Notebooks", "ev_eda_analysis.ipynb"))

if os.path.exists("dataset_profile.csv"):
    shutil.copy2("dataset_profile.csv", os.path.join(base_dir, "Analysis", "Reports", "dataset_profile.csv"))
if os.path.exists("data_quality_report.txt"):
    shutil.copy2("data_quality_report.txt", os.path.join(base_dir, "Analysis", "Reports", "data_quality_report.txt"))
if os.path.exists("ev_eda_summary.txt"):
    shutil.copy2("ev_eda_summary.txt", os.path.join(base_dir, "Analysis", "Reports", "ev_eda_summary.txt"))
if os.path.exists("tableau_data_dictionary.xlsx"):
    shutil.copy2("tableau_data_dictionary.xlsx", os.path.join(base_dir, "Analysis", "Reports", "tableau_data_dictionary.xlsx"))

# Copy Tableau Specs
if os.path.exists("tableau_visualization_specification.md"):
    shutil.copy2("tableau_visualization_specification.md", os.path.join(base_dir, "Tableau", "Dashboard_Specification", "tableau_visualization_specification.md"))
if os.path.exists("dashboard_layout_plan.md"):
    shutil.copy2("dashboard_layout_plan.md", os.path.join(base_dir, "Tableau", "Dashboard_Specification", "dashboard_layout_plan.md"))
if os.path.exists("filter_implementation_guide.md"):
    shutil.copy2("filter_implementation_guide.md", os.path.join(base_dir, "Tableau", "Dashboard_Specification", "filter_implementation_guide.md"))
if os.path.exists("tableau_testing_checklist.md"):
    shutil.copy2("tableau_testing_checklist.md", os.path.join(base_dir, "Tableau", "Dashboard_Specification", "tableau_testing_checklist.md"))
if os.path.exists("chart_wise_analytical_findings.md"):
    shutil.copy2("chart_wise_analytical_findings.md", os.path.join(base_dir, "Tableau", "Dashboard_Specification", "chart_wise_analytical_findings.md"))
if os.path.exists("tableau_story_structure.md"):
    shutil.copy2("tableau_story_structure.md", os.path.join(base_dir, "Tableau", "Story_Specification", "tableau_story_structure.md"))

print("Structure initialization completed successfully!")

