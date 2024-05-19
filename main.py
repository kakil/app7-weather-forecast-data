import streamlit as st
import pandas as pd

st.header("Weather Forecast for the Upcoming Days")

city = st.text_input(label="Place:")

days = st.slider(label="Forecast Days",
                 min_value=1,
                 max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox(label="Select data to view",
                         options=["Temperature", "Sky"])

st.subheader(f"{option} for the next {days} in {city}")

