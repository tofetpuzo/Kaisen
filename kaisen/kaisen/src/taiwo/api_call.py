import logging
import os
from http import HTTPStatus

import requests

from exceptions import APIException

"""
NB:
    # create an env fist then you use the command below
    # export URL="api_url"
"""


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="api_call.log",
    filemode="w",
)

# note1 = "6.5095° N, 3.3711° E"
# note2 = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
# note3 = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
# note4 = "https://api.open-meteo.com/v1/forecast?latitude=6.5095&longitude=3.3711&hourly=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"


def test_api(latitude, longitude, hourly="temperature_2m,wind_speed_10m"):
    # latitude = 6.5095  # Yaba, Lagos latitude
    # longitude = 3.3711  # Yaba, Lagos longitude
    api_url = os.environ.get("URL")
    try:
        url = f"{api_url}/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

        response = requests.get(url)  # aiohttp, httpx
        data = response.json()

        if response.status_code == HTTPStatus.OK:
            temperature_data = data.get("hourly", "this key does not exist").get(
                "temperature_2m", "this key does not exist"
            )
            humidity_data = data.get("hourly", {}).get("relative_humidity_2m", {})
            wind_data = data.get("hourly", {}).get("wind_speed_10m", {})
            logging.info(
                f"Temperature forecast for the next few hours: {temperature_data[:5]}"
            )  # Print first 5 hours
            logging.info(
                f"Relative humidity forecast for the next few hours: {humidity_data[:5]}"
            )  # Print first 5 hours
            logging.info(
                f"Wind speed forecast for the next few hours: {wind_data[:5]}"
            )  # Print first 5 hours
            return print(
                {
                    "temperature_data": temperature_data,
                    "humidity_data": humidity_data,
                    "wind_data": wind_data,
                }
            )
        else:
            logging.info("Failed to fetch weather data.")

    except Exception as e:
        APIException("API Error", HTTPStatus.BAD_REQUEST)
        logging.error(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")
    test_api(latitude, longitude)
