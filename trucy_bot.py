import discord
from discord.ext import commands
import lib_trucy_bot as ltb
import datetime

# Instanciate the bot
bot = commands.Bot(command_prefix='!')

config = ltb.load_from_json("config.json")

# Token
token = config['token']

# NSFW channel IDs
nsfw_channel_ids = config['nsfw_channel_ids']

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
    timestring = ltb.arizona_time().strftime("%H:%M")
    await context.send(f'Arizonian time is {timestring}')

@bot.command()
async def frtime(context):
    timestring = ltb.paris_time().strftime("%H:%M")
    await context.send(f'Paris time is {timestring}')

@bot.command()
async def ass(context):
    if context.channel.id not in nsfw_channel_ids:
        return
    await context.send('ASS BASTARD BELOW')

@bot.command()
async def countdown(context):
    if context.channel.id not in nsfw_channel_ids:
        return
    delta = ltb.time_to_paris()
    await context.send(f'Meeting up in {delta["weeks"]} weeks and {delta["days"]} days')

@bot.command()
async def carl(context):
    with open(ltb.random_carl(), "rb") as fh:
        f = discord.File(fh)
    await context.send(file=f)

@bot.command()
async def carlcount(context):
    number_of_carls = ltb.carl_count()
    await context.send(f'I have {number_of_carls} carls!')

@bot.command()
async def saveconfig(context):
    ltb.save_to_json(config, "config.json")

@bot.command()
async def golf(context):
    await context.send(":desbarres:")

bot.run(token)
