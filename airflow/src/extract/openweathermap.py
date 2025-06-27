import os
import requests
from dotenv import load_dotenv

load_dotenv()

OWM_API_KEY = os.getenv('OWM_API_KEY')
OWM_URL = 'https://api.openweathermap.org/data/2.5/weather'
CITY = 'Curitiba,BR'

def fetch_weather() -> dict:
    params = {
        'q': CITY,
        'appid': OWM_API_KEY,
        'units': 'metric',
    }
    resp = requests.get(OWM_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()
