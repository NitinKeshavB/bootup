import requests 
import os 
from art import tprint

NAME = os.environ.get("NAME")
API_ENDPOINT = os.environ.get("API_ENDPOINT")

print("Hello World!")
print(f"It's a wonderful day today")
tprint(NAME)

response = requests.get(f"http://{API_ENDPOINT}")
temperature = response.json()["temperature"]
print(f"The temperature is {temperature}")
