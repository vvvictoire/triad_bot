"""Weather commands"""
import datetime
import requests
from discord.ext import commands


class Weather(commands.Cog):
    """Commands for the weather"""
    def __init__(self, bot, config) -> None:
        super().__init__()
        self.bot = bot
        self.config = config.config

    def get_weather(self, latitude, longitude, api_key, units):
        """latitude and longitude must have 2 decimal places (I think)"""
        url = 'https://api.openweathermap.org/data/2.5/onecall?'
        arguments = f'units={units}&lat={latitude}&lon={longitude}&appid={api_key}'
        url = url + arguments
        request = requests.get(url)
        weather = request.json()
        return weather

    def stringify_weather(self, weather, unit_symbol="C"):
        """Turn a weather into a presentable string"""
        main = weather['weather'][0]['main']
        description = weather['weather'][0]['description']
        current_timestamp = weather['dt']
        timezone_offset = weather.get('timezone_offset', 0)
        date = self.date_from_unix(current_timestamp + timezone_offset)
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

    def date_from_unix(self, timestamp):
        """Convert a unix timestamp to a date"""
        time = datetime.datetime.fromtimestamp(timestamp)
        time_string = time.strftime("%A %d %b")
        return time_string

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
            weather = self.get_weather(
                self.config['weather_cities'][country]['latitude'],
                self.config['weather_cities'][country]['longitude'],
                self.config['_keys']['openweathermap_api_key'],
                units)
            stringified_weather = self.stringify_weather(weather['current'],
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
            weather = self.get_weather(
                self.config['weather_cities'][country]['latitude'],
                self.config['weather_cities'][country]['longitude'],
                self.config['_keys']['openweathermap_api_key'],
                units)
            daily_weather = weather['daily']
            stringified_weather = ""
            for day in daily_weather:
                stringified_weather += (self.stringify_weather(
                                        day, unit_symbol) + "\n")
            await context.send(stringified_weather)
        except KeyError:
            await context.send('I’m not configured for this country :(')
            return
