import discord
from discord.ext import commands
import lib_trucy_bot as ltb
import sqlite3
import datetime

# Instanciate the bot
bot = commands.Bot(command_prefix='!')

# Database
connection = sqlite3.connect('trucy_bot.db')

# Token
token_file = open('discord_client_token.txt')
token = token_file.read()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def usd(context, amount):
    amount = float(amount)
    dollars = ltb.eur_to_usd(amount)
    await context.send(f'{amount} € in USD is ${dollars:.2f}')

@bot.command()
async def eur(context, amount):
    amount = float(amount)
    euros = ltb.usd_to_eur(amount)
    await context.send(f'${amount} in EUR is {euros:.2f} €')

@bot.command()
async def c(context, temperature):
    temperature = float(temperature)
    celsius = ltb.far_to_cel(temperature)
    await context.send(f'{temperature}°F = {celsius:.2f}°C')

@bot.command()
async def f(context, temperature):
    temperature = float(temperature)
    farenheit = ltb.cel_to_far(temperature)
    await context.send(f'{temperature}°C = {farenheit:.2f}°F')

@bot.command()
async def aztime(context):
    az_timezone = ltb.arizona_time()
    timestring = datetime.datetime.now(az_timezone).strftime("%H:%M")
    await context.send(f'Arizonian time is {timestring}')

@bot.command()
async def frtime(context):
    fr_timezone = ltb.paris_time()
    timestring = datetime.datetime.now(fr_timezone).strftime("%H:%M")
    await context.send(f'Paris time is {timestring}')

bot.run(token)
