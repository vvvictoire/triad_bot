import datetime
import json
import os
import random
import requests
import pytz


# Weather
def get_weather(latitude, longitude, api_key, units):
    """latitude and longitude must have 2 decimal places (I think)"""
    url = 'https://api.openweathermap.org/data/2.5/onecall?'
    arguments = f'units={units}&lat={latitude}&lon={longitude}&appid={api_key}'
    url = url + arguments
    request = requests.get(url)
    weather = request.json()
    return weather


def stringify_weather(weather, unit_symbol="C"):
    main = weather['weather'][0]['main']
    description = weather['weather'][0]['description']
    current_timestamp = weather['dt']
    timezone_offset = weather.get('timezone_offset', 0)
    date = date_from_unix(current_timestamp + timezone_offset)
    weather_string = f'{date}: {main}, {description} '
    temperature = None
    feels_like = None
    try:
        temperature = weather['temp']['day']
        feels_like = weather['feels_like']['day']
    except TypeError:
        temperature = weather['temp']
        feels_like = weather['feels_like']
    temperature_string = f'{temperature}°{unit_symbol}, '
    temperature_string += f'feels like {feels_like}°{unit_symbol}'
    return weather_string + temperature_string


# Money functions
def usd_to_eur(amount):
    return amount*0.86


def eur_to_usd(amount):
    return amount*1.16


# Temperature functions
def far_to_cel(amount):
    return (amount - 32)*5/9


def cel_to_far(amount):
    return amount*1.8 + 32


# Time functions
def arizona_time():
    MST = pytz.timezone('America/Phoenix')
    return datetime.datetime.now(MST)


def paris_time():
    CET = pytz.timezone('Europe/Paris')
    return datetime.datetime.now(CET)


def date_from_unix(timestamp):
    time = datetime.datetime.fromtimestamp(timestamp)
    time_string = time.strftime("%A %d %b")
    return time_string


def time_to_paris():
    CET = pytz.timezone('Europe/Paris')
    arrival = datetime.datetime(2022, 2, 12, tzinfo=CET)
    now = datetime.datetime.now(CET)
    delta = arrival - now
    weeks = delta.days // 7
    days = delta.days % 7
    return {"weeks": weeks, "days": days}


# Copypasta functions
def random_carl():
    carls = os.listdir('rare_carls')
    carl = random.choice(carls)
    return "rare_carls/" + carl


def carl_count():
    carls = os.listdir('rare_carls')
    return len(carls)


# Admin functions
def save_to_json(object_to_save, filename):
    json_string = json.dumps(object_to_save)
    f = open(filename, "w")
    f.write(json_string)
    f.close()


def load_from_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data


def json_to_string(_json):
    return json.dumps(_json, indent=2)


def pretty_print_json(_json):
    return(f"```json\n{_json}```")


def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()
