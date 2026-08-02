from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/weather")
def weather():
    return {
        "city": "Murfreesboro",
        "temperature" : 87,
        "condition": "Sunny"
    }

app.run(host="0.0.0.0", port=5000)