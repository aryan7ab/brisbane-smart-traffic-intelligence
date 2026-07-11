def generate_insights(
    rainfall,
    max_temp,
    wind,
    percent_change
):

    insights = []

    # Rainfall
    if rainfall >= 20:
        insights.append(
            "🌧 Heavy rainfall is expected to significantly reduce active transport demand."
        )
    elif rainfall > 0:
        insights.append(
            "🌦 Light rainfall may slightly reduce cyclist and pedestrian activity."
        )
    else:
        insights.append(
            "☀ Dry weather conditions favour active transport."
        )

    # Temperature
    if max_temp >= 35:
        insights.append(
            "🔥 High temperatures may discourage outdoor movement."
        )
    elif 20 <= max_temp <= 28:
        insights.append(
            "😊 Comfortable temperatures are favourable for walking and cycling."
        )

    # Wind
    if wind >= 25:
        insights.append(
            "💨 Strong winds may reduce cyclist activity."
        )

    # Compared to normal
    if percent_change > 10:
        insights.append(
            "📈 Predicted traffic is well above the historical average."
        )
    elif percent_change < -10:
        insights.append(
            "📉 Predicted traffic is noticeably below historical levels."
        )
    else:
        insights.append(
            "➡ Predicted traffic is close to typical conditions."
        )

    return insights