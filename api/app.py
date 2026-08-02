from flask import Flask


app = Flask(__name__)



@app.route("/weather")
def weather():
    return {
        "city": "Murfreesboro",
        "temperature" : 87,
        "condition": "Sunny"
    }

app.run(host="0.0.0.0", port=5000)