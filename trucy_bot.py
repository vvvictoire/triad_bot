import discord
import lib_trucy_bot as ltb
import sqlite3

# Database
connection = sqlite3.connect('trucy_bot.db')

# Token
token_file = open('discord_client_token.txt')
token = token_file.read()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello there'):
        await message.channel.send('General Kenobi!')

    if message.content.startswith('!usd'):
        amount = float(message.content.split()[1])
        await message.channel.send('{0} € in USD is ${1}'.format(amount, ltb.eur_to_usd(amount)))

    if message.content.startswith('!eur'):
        amount = float(message.content.split()[1])
        await message.channel.send('${0} in EUR is {1} €'.format(amount, ltb.usd_to_eur(amount)))

    if message.content.startswith('!c'):
        amount = float(message.content.split()[1])
        await message.channel.send('{0}°F = {1}°C'.format(amount, ltb.far_to_cel(amount)))

    if message.content.startswith('!f'):
        amount = float(message.content.split()[1])
        await message.channel.send('{0}°C = {1}°F'.format(amount, ltb.cel_to_far(amount)))
client.run(token)
