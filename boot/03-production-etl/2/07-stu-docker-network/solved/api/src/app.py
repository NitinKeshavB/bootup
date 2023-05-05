import requests 
import os 
from flask import Flask 

# create flask app 
app = Flask(__name__)

# import env vars 
API_KEY = os.environ.get("API_KEY")
CITY = os.environ.get("CITY")

# implement api 
@app.route("/")
def api():
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric")
    if response.status_code == 200: 
        temperature = response.json()["main"]["temp"]
        return {"temperature": temperature}
    else: 
        raise Exception("There was an error! Did you specify an API key and a city name?")

# run app 
if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=5000)
