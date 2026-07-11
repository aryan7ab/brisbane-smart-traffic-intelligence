import pandas as pd


def simulate_traffic(
    df,
    model,
    feature_columns,
    site_id,
    mode,
    rainfall,
    max_temp,
    min_temp,
    wind,
    sunshine
):
    """
    Predict daily traffic movements for a selected site,
    transport mode and weather conditions.
    """

    site_data = df[
        (df["Site_ID"] == site_id) &
        (df["Mode"] == mode)
    ]

    if site_data.empty:
        return None

    row = site_data.iloc[-1].copy()

    # -----------------------------------
    # Weather Variables
    # -----------------------------------

    row["Rainfall"] = rainfall
    row["Max_Temp"] = max_temp
    row["Min_Temp"] = min_temp
    row["Max_Wind"] = wind
    row["Sunshine_Duration"] = sunshine

    # -----------------------------------
    # Derived Weather Features
    # -----------------------------------

    row["Rainy_Day"] = rainfall > 0
    row["Heavy_Rain"] = rainfall >= 10

    row["Hot_Day"] = max_temp >= 30
    row["Cold_Morning"] = min_temp <= 10

    row["Windy_Day"] = wind >= 20

    row["Comfortable_Weather"] = (
        rainfall == 0
        and
        20 <= max_temp <= 28
    )

    row["Temp_Range"] = max_temp - min_temp

    features = row.drop("Count")

    features = features.reindex(feature_columns)

    prediction = model.predict(
        pd.DataFrame([features])
    )[0]

    return max(0, prediction)


def compare_weather_scenarios(
    df,
    model,
    feature_columns,
    site_id,
    mode
):
    """
    Compare multiple weather scenarios
    for the same monitoring site.
    """

    scenarios = [

        {
            "Scenario": "☀️ Sunny Day",
            "Rainfall": 0,
            "Max_Temp": 26,
            "Min_Temp": 16,
            "Wind": 10,
            "Sunshine": 10
        },

        {
            "Scenario": "🌦 Light Rain",
            "Rainfall": 5,
            "Max_Temp": 23,
            "Min_Temp": 17,
            "Wind": 15,
            "Sunshine": 5
        },

        {
            "Scenario": "🌧 Heavy Rain",
            "Rainfall": 25,
            "Max_Temp": 22,
            "Min_Temp": 18,
            "Wind": 20,
            "Sunshine": 1
        },

        {
            "Scenario": "🔥 Heatwave",
            "Rainfall": 0,
            "Max_Temp": 37,
            "Min_Temp": 24,
            "Wind": 12,
            "Sunshine": 11
        },

        {
            "Scenario": "🌤 Perfect Weekend",
            "Rainfall": 0,
            "Max_Temp": 24,
            "Min_Temp": 15,
            "Wind": 8,
            "Sunshine": 9
        }

    ]

    results = []

    for s in scenarios:

        prediction = simulate_traffic(
            df=df,
            model=model,
            feature_columns=feature_columns,
            site_id=site_id,
            mode=mode,
            rainfall=s["Rainfall"],
            max_temp=s["Max_Temp"],
            min_temp=s["Min_Temp"],
            wind=s["Wind"],
            sunshine=s["Sunshine"]
        )

        results.append({

            "Scenario": s["Scenario"],

            "Predicted Traffic": round(prediction)

        })

    return pd.DataFrame(results)