from discord.ext import commands
import lib_triad_bot as ltb


class Weather(commands.Cog):
    """Commands for the weather"""
    def __init__(self, bot, config) -> None:
        super().__init__()
        self.bot = bot
        self.config = config.config

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
                self.config['weather_cities'][country]['latitude'],
                self.config['weather_cities'][country]['longitude'],
                self.config['_keys']['openweathermap_api_key'],
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
                self.config['weather_cities'][country]['latitude'],
                self.config['weather_cities'][country]['longitude'],
                self.config['_keys']['openweathermap_api_key'],
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
