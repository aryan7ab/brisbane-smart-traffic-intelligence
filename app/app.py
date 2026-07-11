import streamlit as st
import plotly.express as px

from config import (
    load_model,
    load_data,
    load_feature_columns,
    load_master_dataset
)

from helper import (
    simulate_traffic,
    compare_weather_scenarios
)

from insights import generate_insights


# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="MoveWise Brisbane",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# Load Assets
# ======================================================

model = load_model()
feature_columns = load_feature_columns()
df = load_data()
master_dataset = load_master_dataset()

# ======================================================
# Header
# ======================================================

st.title("🚦 MoveWise Brisbane")

st.markdown("""
### Smart Mobility Intelligence Platform

Predict pedestrian, cyclist and scooter movements across Brisbane using historical traffic patterns, weather conditions and machine learning.
""")

st.success(
    "🚀 AI-powered decision support for planners, transport engineers and smart city initiatives."
)

# ======================================================
# Sidebar
# ======================================================

st.sidebar.header("🎛 Control Panel")
st.sidebar.markdown("""
Configure the monitoring site, transport mode and weather conditions to generate traffic predictions.
""")

# -----------------------------
# Site Selection
# -----------------------------

sites = (
    df[["Site_ID", "Site Name"]]
    .drop_duplicates()
    .sort_values("Site Name")
)

sites["Display"] = (
    sites["Site Name"]
    + " ("
    + sites["Site_ID"]
    + ")"
)

selected_site = st.sidebar.selectbox(
    "📍 Monitoring Site",
    sites["Display"]
)

site_id = selected_site.split("(")[1].replace(")", "")

# -----------------------------
# Intelligent Mode Dropdown
# -----------------------------

available_modes = (
    df[df["Site_ID"] == site_id]["Mode"]
    .dropna()
    .sort_values()
    .unique()
)

mode = st.sidebar.selectbox(
    "🚶 Transport Mode",
    available_modes
)

st.sidebar.info(
    f"""
**Selected Site**

📍 {selected_site}

**Available Transport Modes**

🚶 {' | '.join(available_modes)}
"""
)

st.sidebar.divider()

# -----------------------------
# Weather Inputs
# -----------------------------

rainfall = st.sidebar.slider(
    "🌧 Rainfall (mm)",
    0,
    50,
    0
)

max_temp = st.sidebar.slider(
    "🌡 Maximum Temperature (°C)",
    10,
    45,
    25
)

min_temp = st.sidebar.slider(
    "🌡 Minimum Temperature (°C)",
    0,
    30,
    15
)

wind = st.sidebar.slider(
    "💨 Wind Speed (km/h)",
    0,
    60,
    15
)

sunshine = st.sidebar.slider(
    "☀ Sunshine Hours",
    0,
    12,
    8
)

predict = st.sidebar.button(
    "🔮 Predict Traffic",
    use_container_width=True
)

st.sidebar.divider()

st.sidebar.caption(
"""
MoveWise Brisbane • Version 1.0

Developed using Python, Streamlit, Scikit-learn and Plotly.

Data Sources:
Brisbane City Council & Bureau of Meteorology.
"""
)


# ======================================================
# Tabs
# ======================================================

prediction_tab, scenario_tab, analytics_tab, about_tab = st.tabs(
    [
        "🚦 Prediction",
        "🌦 Scenario Explorer",
        "🗺 Site Analytics",
        "ℹ️ About"
    ]
)

# ======================================================
# Before Prediction
# ======================================================

if not predict:

    st.info(
        "👈 Select a monitoring site, transport mode and weather conditions, then click **Predict Traffic**."
    )

# ======================================================
# Prediction
# ======================================================

else:

    prediction = simulate_traffic(
        df=df,
        model=model,
        feature_columns=feature_columns,
        site_id=site_id,
        mode=mode,
        rainfall=rainfall,
        max_temp=max_temp,
        min_temp=min_temp,
        wind=wind,
        sunshine=sunshine
    )

    if prediction is None:

        st.error(
            "No historical data exists for this site and transport mode."
        )

    else:

        historical_avg = df[
            (df["Site_ID"] == site_id) &
            (df["Mode"] == mode)
        ]["Count"].mean()

        difference = prediction - historical_avg

        percent_change = (
            difference / historical_avg
        ) * 100

        # ======================================================
        # Prediction Tab
        # ======================================================

        with prediction_tab:

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "🚦 Predicted Daily Traffic",
                    f"{prediction:,.0f}"
                )

            with col2:

                st.metric(
                    "📊 Historical Daily Average",
                    f"{historical_avg:,.0f}"
                )

            with col3:

                st.metric(
                    "📈 Change vs Historical Average",
                    f"{percent_change:+.1f}%",
                    delta=f"{difference:+.0f}"
                )

            st.divider()

            #st.subheader("💡 AI Planning Insights")

            insights = generate_insights(
                rainfall,
                max_temp,
                wind,
                percent_change
            )
            with st.container():
                st.subheader("💡 AI Planning Insights")
                for insight in insights:
                    st.markdown(f"✅ {insight}")
    
        # ======================================================
        # Scenario Explorer
        # ======================================================

        with scenario_tab:

            st.subheader("🌦 Weather Scenario Explorer")

            st.write(
                """
                Compare predicted traffic under several
                common Brisbane weather conditions.
                """
            )

            scenario_df = compare_weather_scenarios(
                df=df,
                model=model,
                feature_columns=feature_columns,
                site_id=site_id,
                mode=mode
            )

            st.dataframe(
                scenario_df,
                use_container_width=True,
                hide_index=True
            )

            fig = px.bar(
                scenario_df,
                x="Scenario",
                y="Predicted Traffic",
                color="Scenario",
                text="Predicted Traffic",
                title="Predicted Traffic under Different Weather Scenarios"
            )

            fig.update_traces(
                textposition="outside"
            )

            fig.update_layout(
                showlegend=False,
                height=500,
                xaxis_title="Scenario",
                yaxis_title="Predicted Daily Traffic"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # ======================================================
        # Site Analytics
        # ======================================================

        with analytics_tab:
            st.subheader("🗺 Brisbane Monitoring Network")

            # --------------------------------------------
            # Site Statistics
            # --------------------------------------------

            site_df = df[
            (df["Site_ID"] == site_id) &
            (df["Mode"] == mode)]

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "📊 Historical Average",
                    f"{site_df['Count'].mean():,.0f}")
                
            with col2:
                st.metric(
            "📈 Maximum Recorded",
            f"{site_df['Count'].max():,.0f}")
                
            with col3:
                st.metric(
            "📝 Observations",
            len(site_df))

            st.divider()

            # --------------------------------------------
            # Create Site Map Data
            # --------------------------------------------

            site_map = (
                master_dataset[
                [
                "Site_ID",
                "Site Name",
                "Latitude",
                "Longitude"
                ]].drop_duplicates())

            avg_counts = (
                df.groupby("Site_ID")["Count"]
                .mean()
                .reset_index()
                .rename(
                    columns={
                    "Count": "Average Traffic"}))

            site_map = site_map.merge(
                avg_counts,
                on="Site_ID",
                how="left")

            site_map["Selected"] = (
                site_map["Site_ID"] == site_id)

            # --------------------------------------------
            # Plotly Map
            # --------------------------------------------

            fig = px.scatter_mapbox(
            site_map, lat="Latitude", lon="Longitude", hover_name="Site Name",
            hover_data={
            "Site_ID": True,
            "Average Traffic": ":.0f",
            "Latitude": False,
            "Longitude": False,
            "Selected": False },

            color="Selected",

            size="Average Traffic",

            zoom=11,

            height=650,

            mapbox_style="carto-positron")

            fig.update_layout(
                margin=dict(
                l=0,
                r=0,
                t=0,
                b=0),
            showlegend=False)

            st.plotly_chart(
            fig,
            use_container_width=True)

        # ======================================================
        # About
        # ======================================================

        with about_tab:

            st.subheader("About MoveWise Brisbane")

            st.markdown(
                """
### MoveWise Brisbane

MoveWise Brisbane is a Smart Mobility Decision Support System that predicts pedestrian, cyclist and scooter movements across Brisbane using historical traffic and weather data.

### Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly
- Bureau of Meteorology Weather Data
- Brisbane City Council Traffic Data

### Project Features

- Interactive traffic prediction
- Weather scenario comparison
- AI planning insights
- Historical traffic analytics
- Smart mobility dashboard

Developed as an end-to-end Machine Learning and Smart City Analytics project.
                """
            )

            st.markdown("---")

