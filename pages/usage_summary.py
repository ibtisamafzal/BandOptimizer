import pandas as pd
import streamlit as st

st.title("Bandwidth Usage Summary")

# Sample usage data
data = pd.DataFrame(
    {
        "Entity": ["School A", "School B", "Health Center A", "Health Center B"],
        "Average Usage (Mbps)": [40, 55, 30, 45],
        "Peak Usage (Mbps)": [70, 85, 60, 75],
    }
)

# Display summary in table format
st.write("### Summary Table")
st.dataframe(data)

# Visualize summary data
st.write("### Usage Comparison")
st.bar_chart(data.set_index("Entity"))
