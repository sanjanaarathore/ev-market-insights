import shutil
import os

files_to_sync = [
    "dataset_profile.csv",
    "data_quality_report.txt",
    "cleaned_ev_dataset.csv",
    "ev_eda_summary.txt",
    "tableau_data_dictionary.xlsx"
]

for fname in files_to_sync:
    src = os.path.join("deliverables", fname)
    dst = fname
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Synced {src} -> {dst}")
print("Synchronization complete!")

