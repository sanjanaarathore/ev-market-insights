"""
========================================================================================
VOLTVISION ANALYTICS - ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS
========================================================================================
Interactive Business Intelligence Dashboard, Exploratory Data Analysis & Segment Comparator
Fleet Size: 299,999 Validated Global EV Records | 200 OEMs | 15 Vehicle Categories
Platform: Streamlit Community Cloud & Tableau Public
========================================================================================
"""

import os
import sys
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="VoltVision Analytics - Global EV Market Insights",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# CUSTOM CSS STYLING
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Gradient Banner */
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f766e 100%);
        padding: 2.2rem 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.8rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .hero-tagline {
        color: #2dd4bf;
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 0.3rem;
    }
    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        margin: 0;
        background: linear-gradient(90deg, #ffffff, #38bdf8, #2dd4bf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #94a3b8;
        margin-top: 0.5rem;
        margin-bottom: 1.2rem;
        font-weight: 400;
    }
    .hero-badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
    }
    .hero-badge {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 500;
        color: #e2e8f0;
    }
    
    /* KPI Metric Cards */
    .kpi-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 1.1rem 1.3rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 1rem;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.08);
    }
    .kpi-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        font-weight: 700;
        color: #64748b;
        letter-spacing: 0.5px;
    }
    .kpi-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0f172a;
        margin: 0.25rem 0;
    }
    .kpi-sub {
        font-size: 0.78rem;
        color: #10b981;
        font-weight: 600;
    }
    
    /* Findings Card */
    .finding-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.4rem;
        border-left: 5px solid #0f766e;
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }
    .finding-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.4rem;
    }
    .finding-stat {
        font-weight: 700;
        color: #0f766e;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ROBUST DATASET RESOLUTION (MEMORY-OPTIMIZED)
# -----------------------------------------------------------------------------
def locate_dataset_file():
    """Searches across repository tree to reliably locate cleaned_ev_dataset.csv."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cwd = os.getcwd()
    
    search_paths = [
        os.path.join(script_dir, "Electric_Vehicle_Market_Insights", "Dataset", "Cleaned", "cleaned_ev_dataset.csv"),
        os.path.join(script_dir, "Dataset", "Cleaned", "cleaned_ev_dataset.csv"),
        os.path.join(script_dir, "cleaned_ev_dataset.csv"),
        os.path.join(cwd, "Electric_Vehicle_Market_Insights", "Dataset", "Cleaned", "cleaned_ev_dataset.csv"),
        os.path.join(cwd, "Dataset", "Cleaned", "cleaned_ev_dataset.csv"),
        os.path.join(cwd, "cleaned_ev_dataset.csv"),
        "Electric_Vehicle_Market_Insights/Dataset/Cleaned/cleaned_ev_dataset.csv",
        "Dataset/Cleaned/cleaned_ev_dataset.csv",
        "cleaned_ev_dataset.csv"
    ]
    
    for path in search_paths:
        if os.path.isfile(path):
            return path
            
    # Recursive search if not in standard locations
    for base in [cwd, script_dir]:
        for root, _, files in os.walk(base):
            if "cleaned_ev_dataset.csv" in files:
                return os.path.join(root, "cleaned_ev_dataset.csv")
                
    return None

@st.cache_data(show_spinner="Loading and optimizing global EV fleet records...")
def load_and_optimize_data():
    csv_path = locate_dataset_file()
    if not csv_path:
        st.error("⚠️ Dataset `cleaned_ev_dataset.csv` could not be located in repository.")
        st.stop()
        
    try:
        df = pd.read_csv(csv_path, low_memory=False)
        
        # Ensure column alias compatibility
        if 'price_usd' in df.columns and 'base_price_usd' not in df.columns:
            df['base_price_usd'] = df['price_usd']
        elif 'base_price_usd' in df.columns and 'price_usd' not in df.columns:
            df['price_usd'] = df['base_price_usd']
            
        if 'charging_dc_fast_time_min' in df.columns and 'charging_time_dc_fast_mins' not in df.columns:
            df['charging_time_dc_fast_mins'] = df['charging_dc_fast_time_min']
        elif 'charging_time_dc_fast_mins' in df.columns and 'charging_dc_fast_time_min' not in df.columns:
            df['charging_dc_fast_time_min'] = df['charging_time_dc_fast_mins']
            
        # Memory optimization dtypes
        dtype_dict = {
            'vehicle_id': 'string',
            'manufacturer': 'category',
            'model_name': 'string',
            'model_year': 'int16',
            'category': 'category',
            'battery_type': 'category',
            'range_km': 'float32',
            'battery_capacity_kwh': 'float32',
            'price_usd': 'float32',
            'base_price_usd': 'float32',
            'efficiency_wh_per_km': 'float32',
            'customer_rating': 'float32',
            'manufacturing_country': 'category',
            'annual_sales_units': 'float32',
            'co2_saved_tons_per_year': 'float32',
            'charging_dc_fast_time_min': 'float32',
            'resale_value_pct_3yr': 'float32'
        }
        
        for col, dt in dtype_dict.items():
            if col in df.columns:
                try:
                    df[col] = df[col].astype(dt)
                except Exception:
                    pass
                    
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        st.stop()

df_raw = load_and_optimize_data()

# -----------------------------------------------------------------------------
# SIDEBAR FILTERS & CONTROLS
# -----------------------------------------------------------------------------
st.sidebar.markdown("### ⚡ **VoltVision Analytics**")
st.sidebar.caption("Global EV Performance & Market Intelligence")

nav_choice = st.sidebar.radio(
    "Navigation Menu:",
    [
        "📊 Executive KPI Dashboard",
        "📈 Interactive Visualizations",
        "📑 Tableau Public Embedding",
        "⚖️ Vehicle Segment Comparator",
        "💡 Key Analytical Findings",
        "📁 Dataset Explorer & Export"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Fleet Filters")

# Filter: EV Categories
all_categories = sorted(df_raw['category'].dropna().unique().tolist())
selected_categories = st.sidebar.multiselect(
    "Vehicle Category:",
    options=all_categories,
    default=all_categories
)
if not selected_categories:
    selected_categories = all_categories

# Filter: Battery Technologies
all_batteries = sorted(df_raw['battery_type'].dropna().unique().tolist())
selected_batteries = st.sidebar.multiselect(
    "Battery Technology:",
    options=all_batteries,
    default=all_batteries
)
if not selected_batteries:
    selected_batteries = all_batteries

# Filter: Model Year Range
min_yr = int(df_raw['model_year'].min()) if not df_raw.empty else 2018
max_yr = int(df_raw['model_year'].max()) if not df_raw.empty else 2025
if min_yr >= max_yr:
    max_yr = min_yr + 1

selected_year_range = st.sidebar.slider(
    "Model Year Span:",
    min_value=min_yr,
    max_value=max_yr,
    value=(min_yr, max_yr),
    step=1
)

# Filter: Price Range
min_price = float(df_raw['price_usd'].min()) if not df_raw.empty else 15000.0
max_price = float(df_raw['price_usd'].max()) if not df_raw.empty else 200000.0
if min_price >= max_price:
    max_price = min_price + 1000.0

selected_price_range = st.sidebar.slider(
    "Base MSRP Range ($USD):",
    min_value=int(min_price),
    max_value=int(max_price),
    value=(int(min_price), int(max_price)),
    step=5000
)

# Filter Application
filtered_df = df_raw[
    (df_raw['category'].isin(selected_categories)) &
    (df_raw['battery_type'].isin(selected_batteries)) &
    (df_raw['model_year'] >= selected_year_range[0]) &
    (df_raw['model_year'] <= selected_year_range[1]) &
    (df_raw['price_usd'] >= selected_price_range[0]) &
    (df_raw['price_usd'] <= selected_price_range[1])
]

# Reset Filters Note
st.sidebar.caption(f"Showing **{len(filtered_df):,}** of **{len(df_raw):,}** total vehicles ({len(filtered_df)/len(df_raw)*100:.1f}%).")
st.sidebar.markdown("---")
st.sidebar.markdown("""
**Platform:** VoltVision Analytics  
**Analyst:** Sanjana Rathore  
**Target:** Global EV Ecosystem  
""")

# -----------------------------------------------------------------------------
# HERO BANNER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div class="hero-tagline">⚡ VOLTVISION ANALYTICS PLATFORM</div>
    <div class="hero-title">ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS</div>
    <div class="hero-subtitle">A Data-Driven Exploration of Global EV Manufacturing, Battery Technologies, and Market Trends</div>
    <div class="hero-badge-container">
        <span class="hero-badge">🚗 299,999 Fleet Records</span>
        <span class="hero-badge">🏭 200 Automotive OEMs</span>
        <span class="hero-badge">🔋 5 Battery Chemistries</span>
        <span class="hero-badge">🌍 10 Manufacturing Nations</span>
        <span class="hero-badge">🌱 1.06M Tons Annual CO2 Offset</span>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# GLOBAL METRICS ROW (6 KPI CARDS)
# -----------------------------------------------------------------------------
kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)

with kpi1:
    total_models = filtered_df['model_name'].nunique() if not filtered_df.empty else 0
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total EV Models</div>
        <div class="kpi-value">{total_models:,}</div>
        <div class="kpi-sub">{len(filtered_df):,} Fleet Records</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    total_oems = filtered_df['manufacturer'].nunique() if not filtered_df.empty else 0
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Active OEMs</div>
        <div class="kpi-value">{total_oems:,}</div>
        <div class="kpi-sub">Global Automakers</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    avg_rating = filtered_df['customer_rating'].mean() if not filtered_df.empty else 0
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Avg Satisfaction</div>
        <div class="kpi-value">{avg_rating:.2f} ★</div>
        <div class="kpi-sub">Benchmark: 4.09 ★</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    avg_range = filtered_df['range_km'].mean() if not filtered_df.empty else 0
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Avg Driving Range</div>
        <div class="kpi-value">{avg_range:.1f}</div>
        <div class="kpi-sub">Kilometers / Charge</div>
    </div>
    """, unsafe_allow_html=True)

with kpi5:
    avg_batt = filtered_df['battery_capacity_kwh'].mean() if not filtered_df.empty else 0
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Avg Battery Pack</div>
        <div class="kpi-value">{avg_batt:.1f}</div>
        <div class="kpi-sub">kWh Usable Capacity</div>
    </div>
    """, unsafe_allow_html=True)

with kpi6:
    total_sales = filtered_df['annual_sales_units'].sum() if not filtered_df.empty else 0
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Fleet Sales</div>
        <div class="kpi-value">{total_sales / 1e9:.2f}B</div>
        <div class="kpi-sub">Annual Units Delivered</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SECTION 1: EXECUTIVE KPI DASHBOARD
# -----------------------------------------------------------------------------
if nav_choice == "📊 Executive KPI Dashboard":
    st.subheader("📊 Executive Overview & Market Performance")
    
    col_left, col_right = st.columns([3, 2])
    
    with col_left:
        # Category Horizontal Bar Chart
        cat_df = filtered_df.groupby('category', observed=True).agg(
            model_count=('vehicle_id', 'count'),
            total_sales=('annual_sales_units', 'sum')
        ).reset_index().sort_values('model_count', ascending=True)
        
        fig_cat = px.bar(
            cat_df,
            x='model_count',
            y='category',
            orientation='h',
            title="<b>EV Category Distribution & Model Volume</b>",
            labels={'model_count': 'Total Vehicle Models', 'category': 'Vehicle Category'},
            color='model_count',
            color_continuous_scale='teal',
            text='model_count'
        )
        fig_cat.update_layout(height=420, margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_cat, use_container_width=True)
        
    with col_right:
        # Battery Technology Donut / Pie
        batt_df = filtered_df.groupby('battery_type', observed=True)['vehicle_id'].count().reset_index()
        fig_batt = px.pie(
            batt_df,
            names='battery_type',
            values='vehicle_id',
            title="<b>Battery Chemistry Adoption Share</b>",
            hole=0.45,
            color='battery_type',
            color_discrete_map={
                'NMC': '#0f766e',
                'LFP': '#0284c7',
                'NCA': '#f59e0b',
                'Sodium-Ion': '#8b5cf6',
                'Solid-State': '#ec4899'
            }
        )
        fig_batt.update_layout(height=420, margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_batt, use_container_width=True)
        
    # Second Row: Sales Trend & Top Manufacturers
    row2_col1, row2_col2 = st.columns([3, 2])
    
    with row2_col1:
        # Annual Sales Trend by Model Year
        sales_trend = filtered_df.groupby('model_year', observed=True)['annual_sales_units'].sum().reset_index()
        fig_trend = px.line(
            sales_trend,
            x='model_year',
            y='annual_sales_units',
            title="<b>Annual EV Sales Trend Across Model Years</b>",
            markers=True,
            labels={'model_year': 'Model Year', 'annual_sales_units': 'Annual Sales Volume (Units)'}
        )
        fig_trend.update_traces(line_color='#0f766e', line_width=3, marker_size=8)
        fig_trend.update_layout(height=380, margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_trend, use_container_width=True)
        
    with row2_col2:
        # Top 10 Manufacturers by Models
        top_oems = filtered_df.groupby('manufacturer', observed=True)['vehicle_id'].count().reset_index().sort_values('vehicle_id', ascending=False).head(10)
        fig_oem = px.bar(
            top_oems,
            x='vehicle_id',
            y='manufacturer',
            orientation='h',
            title="<b>Top 10 Manufacturers by Model Count</b>",
            labels={'vehicle_id': 'Models Offered', 'manufacturer': 'OEM'},
            color='vehicle_id',
            color_continuous_scale='Blues'
        )
        fig_oem.update_layout(height=380, yaxis={'categoryorder':'total ascending'}, margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_oem, use_container_width=True)

# -----------------------------------------------------------------------------
# SECTION 2: INTERACTIVE VISUALIZATIONS
# -----------------------------------------------------------------------------
elif nav_choice == "📈 Interactive Visualizations":
    st.subheader("📈 High-Fidelity Interactive Visualizations")
    st.markdown("Direct implementations of the 7 Tableau Public visualization specifications.")
    
    tab_v1, tab_v2, tab_v3, tab_v4 = st.tabs([
        "Customer Ratings & Satisfaction",
        "Geographic Assembly Distribution",
        "Range vs Battery Engineering",
        "CO2 Decarbonization by Segment"
    ])
    
    with tab_v1:
        # Rating Bar Chart with 4.09 Reference Line
        rating_df = filtered_df.groupby('category', observed=True)['customer_rating'].mean().reset_index().sort_values('customer_rating', ascending=False)
        fig_rating = px.bar(
            rating_df,
            x='category',
            y='customer_rating',
            title="<b>Average Customer Rating by Vehicle Category (Benchmark: 4.09★)</b>",
            labels={'category': 'Vehicle Segment', 'customer_rating': 'Average Rating (1-5★)'},
            color='customer_rating',
            color_continuous_scale='Greens',
            text=rating_df['customer_rating'].apply(lambda x: f"{x:.2f}")
        )
        fig_rating.add_hline(y=4.09, line_dash="dash", line_color="#dc2626", annotation_text="Global Fleet Mean: 4.09★")
        fig_rating.update_layout(height=480, yaxis_range=[3.8, 4.3])
        st.plotly_chart(fig_rating, use_container_width=True)
        
    with tab_v2:
        # Country Distribution Bar
        country_df = filtered_df.groupby('manufacturing_country', observed=True)['vehicle_id'].count().reset_index().sort_values('vehicle_id', ascending=False)
        fig_country = px.bar(
            country_df,
            x='manufacturing_country',
            y='vehicle_id',
            title="<b>Global EV Model Distribution by Manufacturing Country</b>",
            labels={'manufacturing_country': 'Country of Origin', 'vehicle_id': 'Total Vehicles Produced'},
            color='vehicle_id',
            color_continuous_scale='Viridis',
            text='vehicle_id'
        )
        fig_country.update_layout(height=480)
        st.plotly_chart(fig_country, use_container_width=True)
        
    with tab_v3:
        # Scatter: Range vs Battery Capacity colored by Price (Sampled for responsiveness)
        sample_size = min(3000, len(filtered_df))
        sample_df = filtered_df.sample(sample_size, random_state=42) if len(filtered_df) > 3000 else filtered_df
        fig_scatter = px.scatter(
            sample_df,
            x='battery_capacity_kwh',
            y='range_km',
            color='category',
            size='price_usd',
            hover_data=['model_name', 'manufacturer', 'battery_type', 'efficiency_wh_per_km'],
            title=f"<b>Engineering Frontier: Battery Capacity vs Range (Sampled {sample_size:,} Records)</b>",
            labels={'battery_capacity_kwh': 'Battery Capacity (kWh)', 'range_km': 'Driving Range (km)', 'price_usd': 'Base MSRP ($)'}
        )
        fig_scatter.update_layout(height=520)
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    with tab_v4:
        # CO2 displacement by Category
        co2_df = filtered_df.groupby('category', observed=True)['co2_saved_tons_per_year'].mean().reset_index().sort_values('co2_saved_tons_per_year', ascending=False)
        fig_co2 = px.bar(
            co2_df,
            x='category',
            y='co2_saved_tons_per_year',
            title="<b>Annual Carbon Displacement Potential by Vehicle Segment (Tons CO2 Saved / Year)</b>",
            labels={'category': 'Vehicle Segment', 'co2_saved_tons_per_year': 'Avg CO2 Saved (Tons/Yr)'},
            color='co2_saved_tons_per_year',
            color_continuous_scale='Tealgrn',
            text=co2_df['co2_saved_tons_per_year'].apply(lambda x: f"{x:.2f} t")
        )
        fig_co2.update_layout(height=480)
        st.plotly_chart(fig_co2, use_container_width=True)

# -----------------------------------------------------------------------------
# SECTION 3: TABLEAU PUBLIC EMBEDDING
# -----------------------------------------------------------------------------
elif nav_choice == "📑 Tableau Public Embedding":
    st.subheader("📑 Tableau Public Live Embedding Portal")
    st.markdown("Integrates the Tableau Public dashboard directly into Streamlit via official embedding.")
    
    col_input, col_btn = st.columns([4, 1])
    with col_input:
        tableau_url = st.text_input(
            "Tableau Public Published URL:",
            value="https://public.tableau.com/views/ElectricVehicleMarketPerformance/Dashboard"
        )
    with col_btn:
        st.write("")
        st.write("")
        st.link_button("🌐 Open in Tableau Public", tableau_url)
        
    st.info("ℹ️ **Tableau Public Integration:** Paste your published Tableau Public URL above to immediately preview the live cloud visualization within this dashboard.")
    
    embed_html = f"""
    <div style="width: 100%; border-radius: 12px; overflow: hidden; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
        <iframe src="{tableau_url}?:showVizHome=no&:embed=true"
                width="100%" height="820" frameborder="0">
        </iframe>
    </div>
    """
    st.components.v1.html(embed_html, height=840)

# -----------------------------------------------------------------------------
# SECTION 4: VEHICLE SEGMENT COMPARATOR
# -----------------------------------------------------------------------------
elif nav_choice == "⚖️ Vehicle Segment Comparator":
    st.subheader("⚖️ Interactive Vehicle Segment Benchmarking Engine")
    st.markdown("Compare technical specifications, economic metrics, and decarbonization ROI side-by-side across EV categories.")
    
    col_sel1, col_sel2 = st.columns(2)
    with col_sel1:
        cat_a = st.selectbox("Select Segment A:", all_categories, index=0)
    with col_sel2:
        default_b_idx = min(len(all_categories)-1, 7)
        cat_b = st.selectbox("Select Segment B:", all_categories, index=default_b_idx)
        
    df_a = df_raw[df_raw['category'] == cat_a]
    df_b = df_raw[df_raw['category'] == cat_b]
    
    st.markdown(f"### Benchmarking: **{cat_a}** vs. **{cat_b}**")
    
    metrics = [
        ("Fleet Sample Size", f"{len(df_a):,} units", f"{len(df_b):,} units"),
        ("Avg Driving Range", f"{df_a['range_km'].mean():.1f} km", f"{df_b['range_km'].mean():.1f} km"),
        ("Avg Battery Capacity", f"{df_a['battery_capacity_kwh'].mean():.1f} kWh", f"{df_b['battery_capacity_kwh'].mean():.1f} kWh"),
        ("Avg Base MSRP", f"${df_a['price_usd'].mean():,.0f}", f"${df_b['price_usd'].mean():,.0f}"),
        ("Energy Efficiency", f"{df_a['efficiency_wh_per_km'].mean():.1f} Wh/km", f"{df_b['efficiency_wh_per_km'].mean():.1f} Wh/km"),
        ("Avg Fast Charging Time", f"{df_a['charging_dc_fast_time_min'].mean():.1f} mins", f"{df_b['charging_dc_fast_time_min'].mean():.1f} mins"),
        ("Annual CO2 Displaced", f"{df_a['co2_saved_tons_per_year'].mean():.2f} tons/yr", f"{df_b['co2_saved_tons_per_year'].mean():.2f} tons/yr"),
        ("Avg Customer Rating", f"{df_a['customer_rating'].mean():.2f} ★", f"{df_b['customer_rating'].mean():.2f} ★"),
        ("3-Year Resale Value", f"{df_a['resale_value_pct_3yr'].mean():.1f}%", f"{df_b['resale_value_pct_3yr'].mean():.1f}%")
    ]
    
    comp_df = pd.DataFrame(metrics, columns=["Specification / Dimension", cat_a, cat_b])
    st.table(comp_df)
    
    # Visual comparison bar chart
    comp_chart_data = pd.DataFrame({
        "Metric": ["Range (km)", "Battery (kWh)", "Fast Charge (mins)", "Resale (%)", "CO2 Saved (t)"],
        cat_a: [
            df_a['range_km'].mean(),
            df_a['battery_capacity_kwh'].mean(),
            df_a['charging_dc_fast_time_min'].mean(),
            df_a['resale_value_pct_3yr'].mean(),
            df_a['co2_saved_tons_per_year'].mean() * 10
        ],
        cat_b: [
            df_b['range_km'].mean(),
            df_b['battery_capacity_kwh'].mean(),
            df_b['charging_dc_fast_time_min'].mean(),
            df_b['resale_value_pct_3yr'].mean(),
            df_b['co2_saved_tons_per_year'].mean() * 10
        ]
    })
    
    fig_comp = go.Figure()
    fig_comp.add_trace(go.Bar(name=cat_a, x=comp_chart_data['Metric'], y=comp_chart_data[cat_a], marker_color='#0f766e'))
    fig_comp.add_trace(go.Bar(name=cat_b, x=comp_chart_data['Metric'], y=comp_chart_data[cat_b], marker_color='#0284c7'))
    fig_comp.update_layout(barmode='group', title="<b>Comparative Engineering Profile</b>", height=420)
    st.plotly_chart(fig_comp, use_container_width=True)

# -----------------------------------------------------------------------------
# SECTION 5: KEY ANALYTICAL FINDINGS
# -----------------------------------------------------------------------------
elif nav_choice == "💡 Key Analytical Findings":
    st.subheader("💡 Key Analytical Findings & Business Implications")
    st.markdown("Synthesized insights derived from empirical calculations across the 299,999 validated records.")
    
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        st.markdown("""
        <div class="finding-card">
            <div class="finding-title">1. Market Duopoly in Battery Chemistry</div>
            <p><strong>NMC (33.84%)</strong> and <strong>LFP (32.05%)</strong> control a combined 65.89% duopoly of the global fleet. Solid-State cells demonstrate exceptional longevity (2,998 cycle life), while Sodium-Ion captures 10.01% as an affordable urban mobility solution.</p>
        </div>
        
        <div class="finding-card">
            <div class="finding-title">2. Commercial Decarbonization Leadership</div>
            <p><strong>Electric Buses</strong> achieve an unmatched carbon offset of <span class="finding-stat">9.04 tons CO2/year</span>—almost triple the decarbonization impact of standard passenger sedans (3.04 tons/year). Commercial fleet electrification yields the highest environmental ROI.</p>
        </div>
        
        <div class="finding-card">
            <div class="finding-title">3. Range & Battery Scaling Frontiers</div>
            <p>Fleet driving range averages <span class="finding-stat">324.5 km</span>, tightly anchored to a mean usable capacity of <span class="finding-stat">78.2 kWh</span>. Battery capacity exhibits the strongest statistical correlation with MSRP (<em>r = +0.8373</em>).</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_f2:
        st.markdown("""
        <div class="finding-card">
            <div class="finding-title">4. Competitive Automotive OEM Landscape</div>
            <p>The global fleet is distributed across <strong>200 automotive manufacturers</strong>. VoltWorks leads model variety (1,627 models), while AmpereWorks dominates cumulative sales with <strong>13.84M units</strong> delivered globally.</p>
        </div>
        
        <div class="finding-card">
            <div class="finding-title">5. High Customer Satisfaction Stability</div>
            <p>Customer satisfaction remains remarkably stable across categories, centering at a tight fleet mean of <span class="finding-stat">4.09 ± 0.49★</span>. Luxury and commercial long-haul vehicles score marginally higher due to superior range and infotainment.</p>
        </div>
        
        <div class="finding-card">
            <div class="finding-title">6. Asian Manufacturing Dominance</div>
            <p>China, India, South Korea, Vietnam, and Japan assemble <span class="finding-stat">50.13%</span> of global EV production. China serves as the undisputed epicentre for battery raw materials and cell manufacturing.</p>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SECTION 6: DATASET EXPLORER
# -----------------------------------------------------------------------------
elif nav_choice == "📁 Dataset Explorer & Export":
    st.subheader("📁 Production Dataset Explorer & Export")
    st.markdown("Search, inspect, and export the cleaned and validated Tableau-ready fleet records.")
    
    col_s, col_d = st.columns([3, 1])
    with col_s:
        search_query = st.text_input("Search Model Name or Manufacturer:", "")
        
    view_df = filtered_df
    if search_query:
        view_df = filtered_df[
            filtered_df['model_name'].str.contains(search_query, case=False, na=False) |
            filtered_df['manufacturer'].str.contains(search_query, case=False, na=False)
        ]
        
    with col_d:
        st.write("")
        st.write("")
        # Export top 5,000 rows to ensure instantaneous download without memory lag
        export_sample = view_df.head(5000)
        csv_data = export_sample.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Sample CSV (5k rows)",
            data=csv_data,
            file_name="voltvision_ev_sample.csv",
            mime="text/csv"
        )
        
    st.dataframe(
        view_df[[
            'vehicle_id', 'manufacturer', 'model_name', 'model_year', 'category',
            'battery_type', 'range_km', 'battery_capacity_kwh', 'price_usd',
            'efficiency_wh_per_km', 'customer_rating', 'manufacturing_country', 'annual_sales_units'
        ]].head(100),
        use_container_width=True
    )
    st.caption(f"Displaying first 100 rows of {len(view_df):,} matching vehicles.")

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; font-size: 0.85rem; padding: 1rem 0;">
    <strong>VoltVision Analytics</strong> | Electric Vehicle Market Performance & Insights<br>
    Developed with Streamlit, Plotly, Pandas & Tableau Public | © 2026 Sanjana Rathore
</div>
""", unsafe_allow_html=True)
