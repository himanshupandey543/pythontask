import requests
import json
import os
API_KEY="7c6df112d4aecbd386378d71ade5c0b8"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"
def get_weather_data(location):
    params={
        "q":location,
        "appid":API_KEY,
        "units":"metric"
    }
    try:
        response=requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data=response.json()
        if data.get("cod")=="404":
            return {"error":"Location not found."}
        weather=data["weather"][0]
        main=data["main"]
        return {
            "location":data["name"],
            "country":data["sys"]["country"],
            "temperature":main["temp"],
            "humidity":main["humidity"],
            "description":weather["description"]
        }
    except requests.exceptions.RequestException as e:
        return{"error":f"An error occurred: {e}"}
    except KeyError:
        return{"error":"Could not parse weather data. Please check your API key and location."}
def main():
    print("Welcome to the Command-line Weather App!")
    print("-"*35)
    if API_KEY=="YOUR_API_KEY_HERE":
        print("Error: Please replace 'YOUR_API_KEY_HERE' with your actual API key.")
        return
    while True:
        location=input("\nEnter a city name or ZIP code(or 'exit' to quit): ")
        if location.lower()=='exit':
            break
        print("Fetching weather data...")
        weather_info=get_weather_data(location)
        if"error"in weather_info:
            print(f"Error:{weather_info['error']}")
        else:
            print("\n--- Current Weather ---")
            print(f"Location:{weather_info['location']},{weather_info['country']}")
            print(f"Condition:{weather_info['description'].title()}")
            print(f"Temperature:{weather_info['temperature']}°C")
            print(f"Humidity:{weather_info['humidity']}%")
            print("-" * 35)
if __name__ == "__main__":
    main()
