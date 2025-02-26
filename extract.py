import requests
import json 


# API endpoint and parameters
API_KEY = "e846ba307a7de23f7de2228693f9ec0e"  # Replace with your actual API key
CITY = "New York"  
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}" 


# Send a GET request to the API
response = requests.get(URL)








   

    # Send a GET request to the API
response = requests.get(URL)
     # Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
        data = response.json() 

        city_name = data["name"]
        temperature = data["main"]["temp"]  # Temperature in Kelvin
        weather_description = data["weather"][0]["description"]
    
        # Convert temperature to Celsius
        temperature_celsius = temperature - 273.15
    
        # Print the extracted data
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature_celsius:.2f}°C")
        print(f"Description: {weather_description}")
else:
        print(f"Failed to fetch data. Status code: {response.status_code}") 


