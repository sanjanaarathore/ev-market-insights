import sys
import os

# Add Flask_Web_App to path
sys.path.insert(0, os.path.abspath("Electric_Vehicle_Market_Insights/Flask_Web_App"))
from app import app

client = app.test_client()

endpoints = [
    ('/', 'Home Page'),
    ('/tableau', 'Tableau Embed Page'),
    ('/findings', 'Analytical Findings Page'),
    ('/compare', 'Spec Comparator Page'),
    ('/api/kpi', 'KPI JSON API'),
    ('/api/category-stats', 'Category Stats API'),
    ('/api/spec-compare?cat1=Sedan&cat2=Electric%20Bus', 'Comparator API')
]

print("=== TESTING FLASK WEB APPLICATION ENDPOINTS ===")
all_passed = True
for url, name in endpoints:
    resp = client.get(url)
    status = resp.status_code
    print(f"Endpoint [{url}] ({name}): Status {status} - {'PASSED' if status == 200 else 'FAILED'}")
    if status != 200:
        all_passed = False

if all_passed:
    print("\nSUCCESS: All Flask application endpoints tested and verified with HTTP 200 OK!")
else:
    print("\nWARNING: Some endpoints failed.")

