import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY');

def get_available_currencies():
    """Returns currencies that are currently listed in API"""
    global API_KEY
    URL = f"http://data.fixer.io/api/symbols?access_key={API_KEY}"
    result = requests.get(URL)
    json_data = json.loads(result.text)
    symbols_dict = json_data['symbols']
    return symbols_dict

def get_latest_rates():
    """Returns latest currency rates with base EUR and update timestamp"""
    global API_KEY
    URL = f"http://data.fixer.io/api/latest?access_key={API_KEY}"
    result = requests.get(URL)
    json_data = json.loads(result.text)
    return json_data