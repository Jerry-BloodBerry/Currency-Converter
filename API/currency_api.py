import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_available_currencies():
    """Returns currencies that are currently listed in API"""
    try:
        global API_KEY
        URL = f"http://data.fixer.io/api/symbols?access_key={API_KEY}"
        result = requests.get(URL)
        json_data = json.loads(result.text)
        return json_data
    except requests.exceptions.RequestException:
        return {'success': False, 'error': {'info': 'No internet connection. Check your connection and then reopen '
                                                    'the app.'}}


def get_latest_rates():
    """Returns latest currency rates with base EUR and update timestamp"""
    try:
        global API_KEY
        URL = f"http://data.fixer.io/api/latest?access_key={API_KEY}"
        result = requests.get(URL)
        json_data = json.loads(result.text)
        return json_data
    except requests.exceptions.RequestException:
        return {'success': False, 'error': {'info': 'No internet connection. Check your connection and then reopen '
                                                    'the app.'}}
