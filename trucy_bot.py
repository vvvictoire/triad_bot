import discord
from discord.ext import commands
import lib_trucy_bot as ltb
import sqlite3

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
    await context.send(f'n{amount} € in USD is ${dollars}')

@bot.command()
async def eur(context, amount):
    amount = float(amount)
    euros = ltb.usd_to_eur(amount)
    await context.send(f'n${amount} in EUR is {euros}')

@bot.command()
async def c(context, temperature):
    temperature = float(temperature)
    celsius = ltb.far_to_cel(temperature)
    await context.send(f'{temperature}°F = {celsius}°C')

@bot.command()
async def f(context, temperature):
    temperature = float(temperature)
    farenheit = ltb.cel_to_far(temperature)
    await context.send(f'{temperature}°C = {farenheit}°F')

bot.run(token)
