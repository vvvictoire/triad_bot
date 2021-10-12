import datetime
import json
import os
import random

import pytz


def usd_to_eur(amount):
    return amount*0.86


def eur_to_usd(amount):
    return amount*1.16


def far_to_cel(amount):
    return (amount - 32)*5/9


def cel_to_far(amount):
    return amount*1.8 + 32


def arizona_time():
    MST = pytz.timezone('America/Phoenix')
    return datetime.datetime.now(MST)


def paris_time():
    CET = pytz.timezone('Europe/Paris')
    return datetime.datetime.now(CET)


def time_to_paris():
    CET = pytz.timezone('Europe/Paris')
    arrival = datetime.datetime(2022, 2, 12, tzinfo=CET)
    now = datetime.datetime.now(CET)
    delta = arrival - now
    weeks = delta.days // 7
    days = delta.days % 7
    return {"weeks": weeks, "days": days}


def random_carl():
    carls = os.listdir('rare_carls')
    carl = random.choice(carls)
    return "rare_carls/" + carl


def carl_count():
    carls = os.listdir('rare_carls')
    return len(carls)


def save_to_json(object_to_save, filename):
    json_string = json.dumps(object_to_save)
    f = open(filename, "w")
    f.write(json_string)
    f.close()


def load_from_json(filename):
    f = open(filename, "r")
    data = json.load(f)
    return data
