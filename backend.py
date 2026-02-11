from dotenv import load_dotenv
from flask import Flask, jsonify
import requests
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITIES = {
    "newyork": "New York",
    "sydney": "Sydney",
    "capetown": "Cape Town",
    "bangkok": "Bangkok"
}

@app.route("/weather/<city_key>")
def get_weather(city_key):
    if city_key not in CITIES:
        return jsonify({"error": "City not supported"}), 404

    city_name = CITIES[city_key]

    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city_name}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather"}), 500

    data = response.json()

    result = {
        "city": city_name,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
