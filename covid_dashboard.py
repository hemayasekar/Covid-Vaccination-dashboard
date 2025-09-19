import pandas as pd
import streamlit as st
import plotly.express as px

# Load processed dataset
df = pd.read_csv("clean_covid_vaccinations.csv", parse_dates=["date"])

st.title("🌍 COVID-19 Vaccination Dashboard")
st.write("Explore global vaccination progress interactively.")

# Sidebar filters
country = st.sidebar.selectbox("Select Country", df["country"].unique())

# Filter data
country_data = df[df["country"] == country]

# Plot total vaccinations over time
fig = px.line(
    country_data,
    x="date",
    y="total_vaccinations",
    title=f"Total Vaccinations in {country} Over Time",
    labels={"total_vaccinations": "Total Vaccinations", "date": "Date"}
)
st.plotly_chart(fig)

# Plot daily vaccinations
fig2 = px.bar(
    country_data,
    x="date",
    y="daily_vaccinations",
    title=f"Daily Vaccinations in {country}",
    labels={"daily_vaccinations": "Daily Vaccinations", "date": "Date"}
)
st.plotly_chart(fig2)

# Global summary
st.subheader("🌐 Global Overview")
global_summary = df.groupby("country")["total_vaccinations"].max().sort_values(ascending=False).head(10)
st.write("Top 10 Countries by Total Vaccinations")
st.bar_chart(global_summary)
