import os 
from art import tprint
import requests 

API_ENDPOINT = os.environ.get("API_ENDPOINT")

print("Hello World!")

print("The random number of the day is:")

response = requests.get(f"http://{API_ENDPOINT}")#hello_world_api:5000
if response.status_code == 200: 
    number = response.json()["number"]
    tprint(f"{number}")
else: 
    print("Something went wrong")

