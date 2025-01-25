import time
import pandas as pd
import streamlit as st

st.title("Real-Time Bandwidth Analysis")

# Simulate real-time data streaming
data = pd.DataFrame(
    {
        "Time": pd.date_range(start="2025-01-01 08:00:00", periods=10, freq="1T"),
        "Usage (Mbps)": [30, 45, 60, 50, 70, 80, 55, 65, 75, 85],
    }
)

# Display data in real-time
placeholder = st.empty()

for i in range(len(data)):
    placeholder.write(data.iloc[: i + 1])  # Show data up to the current time
    time.sleep(1)
