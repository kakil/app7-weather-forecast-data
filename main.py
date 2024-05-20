import streamlit as st
import plotly.express as px
import pandas as pd
from backend import get_data, convert_to_fahrenheit


# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Upcoming Days")

city = st.text_input(label="Place:")

days = st.slider(label="Forecast Days",
                 min_value=1,
                 max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox(label="Select data to view",
                         options=["Temperature", "Sky"])

if city:
    try:
        filtered_data = get_data(city,days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            new_temperatures = [convert_to_fahrenheit(temp) for temp in temperatures]

            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=new_temperatures, labels={"x": "Date", "y": "Temperature (F)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=85)

        st.subheader(f"{option} for the next {days} day(s) in {city}")
    except (NameError, KeyError):
        st.error("City NOT FOUND!")
    except Exception as e:
        st.error(f"An error occurred: {e}")



