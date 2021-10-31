import copy
import discord
from discord.ext import commands
import modules.money
import modules.temperature
import modules.time

import lib_triad_bot as ltb

# Important config

CONFIG_FILENAME = 'config.json'
config = ltb.load_from_json(CONFIG_FILENAME)
# Instanciate the bot
bot = commands.Bot(command_prefix=config['command_prefix'])
bot.description = config['description']


def admin_locked(context):
    return context.message.author.id in config['admins']


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


class Weather(commands.Cog):
    """Commands for the weather"""
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command()
    async def w(self, context, country, units="metric"):
        """Gives current weather of a location"""
        # If we don’t want metric, use imperial and Farenheit
        if units != "metric":
            units = "imperial"
            unit_symbol = 'F'
        # If we want metric, just use Celsius
        else:
            unit_symbol = 'C'
        try:
            weather = ltb.get_weather(
                config['weather_cities'][country]['latitude'],
                config['weather_cities'][country]['longitude'],
                config['_keys']['openweathermap_api_key'],
                units)
            stringified_weather = ltb.stringify_weather(weather['current'],
                                                        unit_symbol)
            await context.send(stringified_weather)
        except KeyError:
            await context.send('I’m not configured for this country :(')
            return

    @commands.command()
    async def wr(self, context, country, units="metric"):
        """Gives a weather report for the next 7 days"""
        # If we don’t want metric, use imperial and Farenheit
        if units != "metric":
            units = "imperial"
            unit_symbol = 'F'
        # If we want metric, just use Celsius
        else:
            unit_symbol = 'C'
        try:
            weather = ltb.get_weather(
                config['weather_cities'][country]['latitude'],
                config['weather_cities'][country]['longitude'],
                config['_keys']['openweathermap_api_key'],
                units)
            daily_weather = weather['daily']
            stringified_weather = ""
            for day in daily_weather:
                stringified_weather += (ltb.stringify_weather(
                                        day, unit_symbol) + "\n")
            await context.send(stringified_weather)
        except KeyError:
            await context.send('I’m not configured for this country :(')
            return


class Copypasta(commands.Cog):
    """Copypasting commands"""
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command()
    async def ass(self, context):
        """Sends a random As Above, So Below message"""
        await context.send('ASS BASTARD BELOW')
        # as HECKIN soos

    @commands.command()
    async def carl(self, context):
        """Shows a random Rare Carl!"""
        with open(ltb.random_carl(), "rb") as fh:
            f = discord.File(fh)
        await context.send(file=f)

    @commands.command()
    async def carlcount(self, context):
        """Displays how many Rare Carls do we have"""
        number_of_carls = ltb.carl_count()
        await context.send(f'I have {number_of_carls} carls!')

    @commands.command()
    async def goodshit(self, context):
        """When something is go౦ԁ sHit👌"""
        await context.send('''​👌👀👌👀👌👀👌👀👌👀 good shit go౦ԁ sHit👌 thats ✔
    some good👌👌shit right👌👌there👌👌👌 right✔there ✔✔if i do ƽaү so my self
    💯 i say so 💯 thats what im talking about right there right there (chorus:
    ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ💯 👌👌 👌НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒ​ᵒᵒᵒ👌 👌👌 👌 💯 👌
    👀 👀 👀 👌👌Good shit'''.replace("\n", ''))

    @commands.command()
    async def golf(self, context, emoji):
        """SIESTA GO TO SLEEP"""
        invisible = f"<:invisible:{config['emojis']['invisible']}>"
        siesta = f"<:siesta:{config['emojis']['siesta']}>"
        await context.send(invisible + emoji + "\n" + siesta + invisible
                           + ":person_golfing:")

    @commands.command()
    async def regional(self, context, *message):
        """Puts a message in regional indicators"""
        reconstituted_message = ' '.join(message)
        print(reconstituted_message)
        await context.send("TODO :eye:")

    @commands.command()
    async def navyseal(self, context):
        """Only use it if you have over 300 confirmed gorilla warfares"""
        copypasta = ltb.read_from_file("copypastas/navy_seal.txt")
        await context.send(copypasta)

    @commands.command()
    async def IQ(self, context):
        """Wubba lubba dub dub"""
        copypasta = ltb.read_from_file("copypastas/IQ.txt")
        await context.send(copypasta)


class Admin(commands.Cog):
    """Admin commands (you shouldn’t be around here tbh)"""
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command()
    @commands.check(admin_locked)
    async def saveconfig(self, context):
        """Exports the config to CONFIG_FILENAME"""
        ltb.save_to_json(config, CONFIG_FILENAME)
        await context.send("Config saved!")

    @commands.command()
    @commands.check(admin_locked)
    async def dumpconf(self, context):
        """Dumps the current config (except the _keys)"""
        conf = copy.deepcopy(config)
        del conf['_keys']
        conf = ltb.json_to_string(conf)
        await context.send(ltb.pretty_print_json(conf))

    @commands.command()
    @commands.check(admin_locked)
    async def shutdown(self, context):
        """Shuts off the bot"""
        await context.send('Good night!')
        exit()


bot.add_cog(Weather(bot))
bot.add_cog(modules.money.Money(bot))
bot.add_cog(modules.temperature.Temperature(bot))
bot.add_cog(modules.time.Time(bot))
bot.add_cog(Copypasta(bot))
bot.add_cog(Admin(bot))
bot.run(config['_keys']['token'])
