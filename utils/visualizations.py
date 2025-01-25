import matplotlib.pyplot as plt
import streamlit as st

def plot_usage_trends(data):
    """
    Plot bandwidth usage trends over time.
    """
    fig, ax = plt.subplots()
    ax.plot(data['timestamp'], data['bandwidth_usage'], label='Bandwidth Usage')
    ax.set_title("Bandwidth Usage Trends")
    ax.set_xlabel("Time")
    ax.set_ylabel("Usage (MB)")
    ax.legend()
    st.pyplot(fig)
