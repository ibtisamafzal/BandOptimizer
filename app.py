import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="BandOptimizer - AI Bandwidth Allocation Tool",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit header and footer for a clean UI
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# App title with styling
st.markdown(
    """
    <h1 style="text-align: center; color: #4CAF50; font-size: 3rem; margin-bottom: 1rem;">
        BandOptimizer 🌐
    </h1>
    <p style="text-align: center; font-size: 1.2rem; color: gray;">
        Dynamically allocate bandwidth for schools and health centers based on real-time needs.
    </p>
    """,
    unsafe_allow_html=True,
)

# Sidebar instructions (optional)
st.sidebar.title("Instructions")
st.sidebar.info(
    """
    1. Upload bandwidth usage files for schools and health centers.\n
    2. Click on "Analyze" to see usage patterns.\n
    3. View recommendations for bandwidth allocation.
    """
)

# File upload
school_data = st.file_uploader("Upload School Bandwidth Usage CSV", type=["csv"])
health_data = st.file_uploader("Upload Health Center Bandwidth Usage CSV", type=["csv"])

if school_data and health_data:
    # Read uploaded files
    school_df = pd.read_csv(school_data)
    health_df = pd.read_csv(health_data)

    # Display tables
    st.markdown("### Uploaded Data")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Schools Data")
        st.dataframe(school_df.head())
    with col2:
        st.markdown("#### Health Centers Data")
        st.dataframe(health_df.head())

    # Visualize bandwidth usage
    st.markdown("### Bandwidth Usage Analysis")
    col3, col4 = st.columns(2)

    # School usage visualization
    with col3:
        st.markdown("#### Schools Bandwidth Usage")
        try:
            fig1 = px.line(
                school_df,
                x="timestamp",
                y="Current Bandwidth Usage (Mbps)",
                color="School ID",
                title="Schools Bandwidth Usage",
            )
            st.plotly_chart(fig1, use_container_width=True)
        except Exception as e:
            st.error(f"Error in visualizing school data: {e}")

    # Health center usage visualization
    with col4:
        st.markdown("#### Health Centers Bandwidth Usage")
        try:
            fig2 = px.line(
                health_df,
                x="timestamp",  # Corrected column name
                y="Current Bandwidth Usage (Mbps)",
                color="Health Center ID",
                title="Health Centers Bandwidth Usage",
            )
            st.plotly_chart(fig2, use_container_width=True)
        except Exception as e:
            st.error(f"Error in visualizing health center data: {e}")

        # Recommendation
    st.markdown("### Recommendations")

    if school_data and health_data:
        # Identify peak usage hours for schools
        school_df["hour"] = pd.to_datetime(school_df["timestamp"]).dt.hour
        school_peak_hour = school_df.groupby("hour")["Current Bandwidth Usage (Mbps)"].mean().idxmax()
        
        # Identify peak usage hours for health centers
        health_df["hour"] = pd.to_datetime(health_df["timestamp"]).dt.hour
        health_peak_hour = health_df.groupby("hour")["Current Bandwidth Usage (Mbps)"].mean().idxmax()
        
        # Average usage for schools and health centers
        avg_school_usage = school_df["Current Bandwidth Usage (Mbps)"].mean()
        avg_health_usage = health_df["Current Bandwidth Usage (Mbps)"].mean()
        
        st.write(
            f"""
            Based on the uploaded data:
            - Schools have peak usage at **{school_peak_hour}:00** with an average bandwidth usage of **{avg_school_usage:.2f} Mbps**.
            - Health centers have peak usage at **{health_peak_hour}:00** with an average bandwidth usage of **{avg_health_usage:.2f} Mbps**.
            
            Recommendations:
            - Allocate more bandwidth to schools during their peak hours ({school_peak_hour}:00).
            - Allocate more bandwidth to health centers during their peak hours ({health_peak_hour}:00).
            - Adjust allocation dynamically based on usage patterns.
            """
        )
else:
    st.warning("Please upload both school and health center bandwidth usage files to see recommendations.")