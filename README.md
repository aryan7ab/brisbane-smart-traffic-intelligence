# brisbane-smart-traffic-intelligence
# 🚦 MoveWise Brisbane

> A Smart Mobility Intelligence Platform for forecasting pedestrian, cyclist and scooter movements across Brisbane using Machine Learning, historical traffic data and weather analytics.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-green)

---

# 📖 Overview

MoveWise Brisbane is an end-to-end Smart Mobility Analytics platform developed to help understand and forecast active transport movements across Brisbane.

The platform combines:

- Brisbane City Council traffic counter data
- Bureau of Meteorology historical weather data
- Advanced feature engineering
- Machine Learning
- Interactive visual analytics

to provide intelligent traffic forecasts and decision support for planners, transport engineers and smart city initiatives.

---

# 🎯 Objectives

The project aims to:

- Forecast pedestrian, cyclist and scooter movements
- Understand how weather influences active transport
- Compare traffic under different weather scenarios
- Support data-driven transport planning
- Demonstrate an end-to-end Machine Learning workflow

---

# 📂 Project Structure

```
brisbane-smart-traffic-intelligence/

│
├── app/
│   ├── app.py
│   ├── config.py
│   ├── helper.py
│   └── insights.py
│
├── data/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── src/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 📊 Exploratory Data Analysis

The project includes extensive exploratory analysis, including:

- Yearly traffic trends
- Monthly traffic trends
- Seasonal analysis
- Weekday vs Weekend analysis
- Counter age analysis
- Mode-wise distribution
- Infrastructure analysis
- Brisbane monitoring network map
- Correlation heatmaps
- Weather impact analysis

---

# 🌦 Weather Integration

Historical weather observations from the Bureau of Meteorology were integrated with Brisbane traffic counts to analyse the impact of:

- Rainfall
- Temperature
- Wind Speed
- Sunshine Duration

Additional engineered features include:

- Rainy Day
- Heavy Rain
- Hot Day
- Cold Morning
- Comfortable Weather
- Windy Day
- Temperature Range
- Rolling Statistics
- Lag Features
- Cyclical Time Features

---

# 🤖 Machine Learning

Three regression models were evaluated:

| Model | Purpose |
|--------|----------|
| Linear Regression | Baseline forecasting model |
| Random Forest | Ensemble learning |
| XGBoost | Gradient boosting |

Performance was compared using RMSE, with Linear Regression providing the best generalisation performance on the processed dataset.

---

# 🚀 MoveWise Brisbane Dashboard

The Streamlit application includes:

✅ Interactive Traffic Prediction

✅ Intelligent Monitoring Site Selection

✅ Dynamic Transport Mode Selection

✅ Weather-based Prediction

✅ KPI Dashboard

✅ AI Planning Insights

✅ Weather Scenario Explorer

✅ Interactive Brisbane Monitoring Map

✅ Site Analytics Dashboard

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Scikit-Learn
- XGBoost
- Joblib

---

# 📈 Key Features

- End-to-end Machine Learning pipeline
- Weather-aware traffic prediction
- Interactive dashboard
- Explainable AI insights
- Scenario simulation
- Brisbane spatial visualisation
- Modular application architecture

---

# 💼 Potential Applications

MoveWise Brisbane can support:

- Smart City initiatives
- Transport planning
- Infrastructure investment
- Active transport analysis
- Mobility forecasting
- Urban analytics

---

# ▶️ Running the Project

Clone the repository

```bash
git clone https://github.com/aryan7ab/brisbane-smart-traffic-intelligence.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch the Streamlit application

```bash
streamlit run app/app.py
```

---

# 📌 Future Improvements

- Real-time weather integration
- Live Brisbane traffic feeds
- Deep Learning forecasting models
- Time-series forecasting (LSTM / Prophet)
- Mobile-friendly interface
- Cloud deployment with continuous integration

---

# 👨‍💻 Author

**Aryan Bhardwaj**

Master of Data Science  
The University of Queensland

GitHub:
https://github.com/aryan7ab

---

# 📜 License

This project is released under the MIT License.
