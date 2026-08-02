from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


@app.route("/weather")
def weather():
    city = request.args.get("city", "").strip()

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        location_response = requests.get(
            GEOCODING_URL,
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json",
            },
            timeout=10,
        )
        location_response.raise_for_status()

        location_data = location_response.json()
        results = location_data.get("results", [])

        if not results:
            return jsonify({"error": "City not found"}), 404

        location = results[0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        location_name = location["name"]

        weather_response = requests.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "wind_speed_10m,"
                    "weather_code"
                ),
                "daily": "temperature_2m_max,temperature_2m_min",
                "temperature_unit": "fahrenheit",
                "wind_speed_unit": "mph",
                "timezone": "auto",
            },
            timeout=10,
        )
        weather_response.raise_for_status()

        weather_data = weather_response.json()

        return jsonify({
            "city": location_name,
            "current": weather_data["current"],
            "daily": weather_data["daily"],
        })

    except requests.RequestException:
        app.logger.exception("Weather service request failed")
        return jsonify({"error": "Unable to retrieve weather data"}), 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)