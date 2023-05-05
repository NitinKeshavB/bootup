from flask import Flask
import random 

app = Flask(__name__)

@app.route("/")
def index():
    # returns a random number between 0 to 100 
    return { "number": random.randint(0, 100)}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000 )
