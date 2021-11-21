"""Main script for triadbot"""
from discord.ext import commands

from modules import admin
from modules import copypasta
from modules import money
from modules import temperature
from modules import time
from modules import weather
from modules import config

# Load the config
CONFIG_FILENAME = 'config.json'


def main():
    configuration = config.Config(CONFIG_FILENAME)
    # Instanciate the bot
    bot = commands.Bot(command_prefix=configuration.config['command_prefix'],
                       description=configuration.config['description'])

    @bot.event
    async def on_ready():
        """Fires after being connected(?)"""
        print(f'Logged in as {bot.user}')

    bot.add_cog(weather.Weather(bot, configuration))
    bot.add_cog(money.Money(bot))
    bot.add_cog(temperature.Temperature(bot))
    bot.add_cog(time.Time(bot))
    bot.add_cog(copypasta.Copypasta(bot, configuration))
    bot.add_cog(admin.Admin(bot, configuration))
    bot.run(configuration.config['_keys']['token'])


if __name__ == '__main__':
    main()
