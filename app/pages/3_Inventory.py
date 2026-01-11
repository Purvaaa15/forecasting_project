import streamlit as st
import pandas as pd
import plotly.express as px

inventory = pd.read_csv("../data/outputs/inventory_status.csv")
inventory["date"] = pd.to_datetime(inventory["date"])

st.title("📦 Inventory Position")

fig = px.line(
    inventory,
    x="date",
    y="stock_balance",
    title="Inventory Balance Over Time"
)

st.plotly_chart(fig, use_container_width=True)

st.caption("Negative stock indicates potential stockout risk.")