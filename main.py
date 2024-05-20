import streamlit as st
import plotly.express as px
import pandas as pd
from backend import get_data

st.header("Weather Forecast for the Upcoming Days")

city = st.text_input(label="Place:")

days = st.slider(label="Forecast Days",
                 min_value=1,
                 max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox(label="Select data to view",
                         options=["Temperature", "Sky"])

st.subheader(f"{option} for the next {days} in {city}")

data = get_data(city, days, option)


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)