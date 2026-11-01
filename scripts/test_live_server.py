import threading
import time
import urllib.request
import urllib.error
import sys
import os

# Add Flask_Web_App to sys.path
app_dir = os.path.abspath("Electric_Vehicle_Market_Insights/Flask_Web_App")
sys.path.insert(0, app_dir)

from app import app

# Run app in a separate background thread
server_thread = threading.Thread(target=lambda: app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False))
server_thread.daemon = True
server_thread.start()

print("Waiting for local server to spin up on http://127.0.0.1:5000...")
time.sleep(2)

test_urls = [
    ("http://127.0.0.1:5000/", "Home Landing Page"),
    ("http://127.0.0.1:5000/tableau", "Tableau Dedicated View"),
    ("http://127.0.0.1:5000/findings", "Analytical Findings Page"),
    ("http://127.0.0.1:5000/compare", "Spec Comparator Page"),
    ("http://127.0.0.1:5000/static/css/style.css", "CSS Stylesheet"),
    ("http://127.0.0.1:5000/static/js/main.js", "JavaScript File"),
    ("http://127.0.0.1:5000/api/kpi", "KPI JSON API"),
    ("http://127.0.0.1:5000/api/category-stats", "Category Stats API"),
    ("http://127.0.0.1:5000/api/spec-compare?cat1=Sedan&cat2=Electric%20Bus", "Comparator API")
]

all_passed = True
for url, desc in test_urls:
    try:
        t0 = time.perf_counter()
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            status = resp.status
            content_type = resp.headers.get('Content-Type')
            data = resp.read()
            dt = (time.perf_counter() - t0) * 1000
            print(f"[OK 200] {desc} ({url}): {len(data):,} bytes in {dt:.1f}ms - Type: {content_type}")
    except Exception as e:
        print(f"[ERROR] Failed {desc} ({url}): {e}")
        all_passed = False

if all_passed:
    print("\nALL ROUTES AND ASSETS RETURNED STATUS 200 OK! ZERO SERVER ERRORS!")
    sys.exit(0)
else:
    print("\nSOME ROUTES FAILED!")
    sys.exit(1)

