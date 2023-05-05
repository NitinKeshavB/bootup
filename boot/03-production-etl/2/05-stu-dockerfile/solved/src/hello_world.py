import requests 
import os 
from art import tprint

API_KEY = os.environ.get("API_KEY")
NAME = os.environ.get("NAME")
CITY = os.environ.get("CITY")

print("Hello World!")
print(f"It's a wonderful day today")
tprint(NAME)

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric")
if response.status_code == 200: 
    temperature = response.json()["main"]["temp"]
    print(f"It is currently {temperature} degrees celcius.")
else: 
    print("There was an error! Did you specify an API key and a city name?")

