from flask import Flask, request
import requests

app = Flask(__name__)



@app.route("/weather")
def weather():
    city = request.args.get("city", "Murfreesboro")

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=35.85&longitude=-86.39&current=temperature_2m"
    )

    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)