import discord
from discord.ext import commands

import lib_triad_bot as ltb

# Important config

CONFIG_FILENAME = 'config.json'
config = ltb.load_from_json(CONFIG_FILENAME)
# Instanciate the bot
bot = commands.Bot(command_prefix=config['command_prefix'])


def admin_locked(context):
    return context.message.author.id in config['admins']


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
    await context.send('ASS BASTARD BELOW')


@bot.command()
async def countdown(context):
    delta = ltb.time_to_paris()
    await context.send(
        f'Meeting up in {delta["weeks"]} weeks and {delta["days"]} days')


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
@commands.check(admin_locked)
async def saveconfig(context):
    ltb.save_to_json(config, CONFIG_FILENAME)
    await context.send("Config saved!")


@bot.command()
async def goodshit(context):
    await context.send('''​👌👀👌👀👌👀👌👀👌👀 good shit go౦ԁ sHit👌 thats ✔
some good👌👌shit right👌👌there👌👌👌 right✔there ✔✔if i do ƽaү so my self
💯 i say so 💯 thats what im talking about right there right there (chorus:
ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ💯 👌👌 👌НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒ​ᵒᵒᵒ👌 👌👌 👌 💯 👌
👀 👀 👀 👌👌Good shit'''.replace("\n", ''))


@bot.command()
async def golf(context, emoji):
    invisible = f"<:invisible:{config['emojis']['invisible']}>"
    siesta = f"<:siesta:{config['emojis']['siesta']}>"
    await context.send(invisible + emoji + "\n" + siesta + invisible
                       + ":person_golfing:")


@bot.command()
@commands.check(admin_locked)
async def dumpconf(context):
    conf = ltb.load_from_json(CONFIG_FILENAME)
    del conf['token']
    conf = ltb.json_to_string(conf)
    await context.send(f"```json\n{conf}```")


bot.run(config['token'])
