import streamlit as st
import pandas as pd

decision = pd.read_csv("../data/outputs/decision_summary.csv")

st.title("🏠 Business Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Current Stock",
    int(float(decision.loc[0, "Value"]))
)

col2.metric(
    "Avg Monthly Demand",
    int(float(decision.loc[1, "Value"]))
)

col3.metric(
    "6-Month Forecast Demand",
    int(float(decision.loc[2, "Value"]))
)

st.divider()

if decision.loc[4, "Value"] == True:
    st.error("⚠️ Restock Required Soon")
else:
    st.success("✅ Stock Levels Are Safe")