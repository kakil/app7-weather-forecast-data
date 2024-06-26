import os
import dotenv
import requests

dotenv.load_dotenv()

api_key = os.getenv("OPEN_WEATHER_API_KEY")

# Example URLs
# http://api.openweathermap.org/data/2.5/forecast?q=jacksonville&appid=e118605d36f22d7ae480a12ccff0fab0
# http://api.openweathermap.org/data/2.5/forecast?q=orange%20park&appid=e118605d36f22d7ae480a12ccff0fab0


def get_data(city, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


def convert_to_fahrenheit(temperature):
    return ((temperature / 10) * (9/5)) + 32


if __name__ == "__main__":
    print(get_data(city="orange%20park", forecast_days=3, kind="Temperature"))