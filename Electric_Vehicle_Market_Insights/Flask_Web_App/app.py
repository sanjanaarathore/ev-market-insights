import os
import json
import pandas as pd
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Load cleaned dataset once on application startup
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "Dataset", "Cleaned", "cleaned_ev_dataset.csv")
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "cleaned_ev_dataset.csv")

print(f"Loading dataset from: {DATA_PATH}...")
try:
    df = pd.read_csv(DATA_PATH)
    print(f"Successfully loaded {len(df):,} records into Flask application memory.")
except Exception as e:
    print(f"Error loading dataset: {e}")
    df = pd.DataFrame()

# Precompute global KPIs
if not df.empty:
    GLOBAL_KPIS = {
        'total_records': f"{len(df):,}",
        'unique_models': f"{df['model_name'].nunique():,}",
        'total_manufacturers': f"{df['manufacturer'].nunique()}",
        'avg_rating': f"{df['customer_rating'].mean():.2f}",
        'avg_range': f"{df['range_km'].mean():.1f} km",
        'avg_battery': f"{df['battery_capacity_kwh'].mean():.1f} kWh",
        'total_sales': f"{df['annual_sales_units'].sum() / 1e9:.2f}B Units",
        'total_sales_raw': int(df['annual_sales_units'].sum()),
        'total_co2_saved': f"{df['co2_saved_tons_per_year'].sum():,.0f} Tons/Year"
    }
else:
    GLOBAL_KPIS = {}

# Default Tableau Public Embed URLs (Configurable placeholders)
TABLEAU_CONFIG = {
    'dashboard_url': 'https://public.tableau.com/views/ElectricVehicleMarketPerformance/Dashboard',
    'story_url': 'https://public.tableau.com/views/ElectricVehicleMarketPerformance/Story',
    'placeholder_notice': True
}

@app.route('/')
def home():
    """Main landing page featuring project intro, objectives, KPIs, Tableau embed, findings, and tech stack."""
    # Compute category preview
    if not df.empty:
        cat_summary = df.groupby('category').agg(
            model_count=('vehicle_id', 'count'),
            avg_range=('range_km', 'mean'),
            avg_price=('price_usd', 'mean'),
            avg_rating=('customer_rating', 'mean')
        ).reset_index().sort_values(by='model_count', ascending=False).to_dict('records')
    else:
        cat_summary = []

    return render_template('index.html', kpis=GLOBAL_KPIS, categories=cat_summary, tableau=TABLEAU_CONFIG)

@app.route('/tableau')
def tableau_view():
    """Dedicated interactive Tableau dashboard and story viewer page."""
    return render_template('tableau.html', kpis=GLOBAL_KPIS, tableau=TABLEAU_CONFIG)

@app.route('/findings')
def findings_view():
    """Comprehensive analytical findings breakdown across all 14 research questions."""
    return render_template('findings.html', kpis=GLOBAL_KPIS)

@app.route('/compare')
def compare_view():
    """Interactive vehicle category and OEM specification comparator tool."""
    categories = sorted(df['category'].unique().tolist()) if not df.empty else []
    manufacturers = sorted(df['manufacturer'].unique().tolist())[:50] if not df.empty else []
    return render_template('compare.html', categories=categories, manufacturers=manufacturers)

# --- API Endpoints ---
@app.route('/api/kpi')
def api_kpi():
    """Returns real-time fleet KPIs."""
    return jsonify(GLOBAL_KPIS)

@app.route('/api/category-stats')
def api_category_stats():
    """Returns aggregated performance metrics by vehicle category."""
    if df.empty:
        return jsonify([])
    stats = df.groupby('category').agg({
        'vehicle_id': 'count',
        'range_km': 'mean',
        'battery_capacity_kwh': 'mean',
        'price_usd': 'mean',
        'annual_sales_units': 'sum',
        'customer_rating': 'mean',
        'co2_saved_tons_per_year': 'mean'
    }).round(2).reset_index().to_dict('records')
    return jsonify(stats)

@app.route('/api/spec-compare')
def api_spec_compare():
    """API for comparing two vehicle categories or segments."""
    cat1 = request.args.get('cat1', 'Sedan')
    cat2 = request.args.get('cat2', 'Compact SUV')
    
    if df.empty:
        return jsonify({})
    
    def get_stats(cat_name):
        sub = df[df['category'] == cat_name]
        if sub.empty:
            return {}
        return {
            'category': cat_name,
            'models_count': len(sub),
            'avg_range': round(float(sub['range_km'].mean()), 1),
            'avg_battery': round(float(sub['battery_capacity_kwh'].mean()), 1),
            'avg_price': round(float(sub['price_usd'].mean()), 2),
            'avg_efficiency': round(float(sub['efficiency_wh_per_km'].mean()), 1),
            'avg_acceleration': round(float(sub['acceleration_0_100_sec'].mean()), 2),
            'avg_rating': round(float(sub['customer_rating'].mean()), 2),
            'avg_co2_saved': round(float(sub['co2_saved_tons_per_year'].mean()), 2),
            'total_sales': int(sub['annual_sales_units'].sum())
        }
    
    return jsonify({
        'segment1': get_stats(cat1),
        'segment2': get_stats(cat2)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting Flask server on http://127.0.0.1:{port}...")
    app.run(host='0.0.0.0', port=port, debug=False)

