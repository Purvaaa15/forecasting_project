import streamlit as st
import pandas as pd
import plotly.express as px

forecast = pd.read_csv("../data/outputs/forecast.csv")
forecast["date"] = pd.to_datetime(forecast["date"])

st.title("📈 Demand Forecast")

fig = px.line(
    forecast,
    x="date",
    y="forecast_quantity",
    markers=True,
    title="Future Demand Forecast"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Forecast Table")
st.dataframe(forecast)

st.download_button(
    "⬇ Download Forecast",
    forecast.to_csv(index=False),
    file_name="forecast.csv"
)