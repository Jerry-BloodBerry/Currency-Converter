import requests
import json
import os
from dotenv import load_dotenv
import urllib3


load_dotenv()
API_KEY = os.getenv('API_KEY');


def internet_on():
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', "https://www.google.com/")
        #print(r.status)
    except:
        return False
    


def get_available_currencies():
    if internet_on() is False:
        print("Brak polaczenia z internetem")
        os.sys.exit()
    try:
        """Returns currencies that are currently listed in API"""
        global API_KEY
        URL = f"http://data.fixer.io/api/symbols?access_key={API_KEY}"
        result = requests.get(URL)
        json_data = json.loads(result.text)
        symbols_dict = json_data['symbols']
    except KeyError:
        print("Niewlasciwy klucz API!") 
        os.sys.exit()
    except ConnectionError:
        print("Blad polaczenia!") 
        os.sys.exit()
    return symbols_dict
        

def get_latest_rates():
    if internet_on() is False:
        print("Brak polaczenia z internetem")
        os.sys.exit()
    try:
        """Returns latest currency rates with base EUR and update timestamp"""
        global API_KEY
        URL = f"http://data.fixer.io/api/latest?access_key={API_KEY}"
        result = requests.get(URL)
        json_data = json.loads(result.text)
    except KeyError:
        print("Niewlasciwy klucz API!") 
        os.sys.exit()
    except ConnectionError:
        print("Blad polaczenia!") 
        os.sys.exit()
    return json_data

