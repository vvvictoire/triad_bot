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
    return MST

def paris_time():
    CET = pytz.timezone('Europe/Paris')
    return CET
