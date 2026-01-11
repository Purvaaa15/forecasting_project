import streamlit as st
import pandas as pd

decision = pd.read_csv("../data/outputs/decision_summary.csv")

st.title("🚨 Alerts & Warnings")

if decision.loc[4, "Value"] == True:
    st.error("⚠️ Forecasted demand exceeds available stock.")
else:
    st.success("✅ No stockout risk detected.")

if decision.loc[5, "Value"] == True:
    st.warning("⚠️ Overstock risk detected. Capital may be blocked.")