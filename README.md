# Weather Dashboard App - Backend

This is the backend service for the Weather Dashboard App.
It provides a REST API to fetch current weather for the following cities: New York , Sydney , Cape Town ,Bangkok

## Prerequisites:

- Python 3.11 + (if runnign locally)
- pip
- Docker (if running containerized)
- OpenWeatherMap API key (free signup at - https://openweathermap.org/api)

## Local installation (Without Docker):
``` bash
git clone https://github.com/VictorB13/weather-app_backend.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirments.txt #install dependencies
export OPENWEATHER_API_KEY=your_api_key_here   # Linux/Mac
python backend.py #run the server - Server will start on: http://127.0.0.1:5001
curl http://127.0.0.1:5001/weather/newyork #test endpoints
```

## Installation with Docker:

```bash 
dockr build -t weather-api #build the image
docekr run -e OPENWEATHER_API_KEY=your_api_key_here -p 5001:5001 weather-backend
curl http://localhost:5001/weather/sydney #test endpoints
```

Notes
-----

- Make sure the OPENWEATHER_API_KEY is set before running the server.




