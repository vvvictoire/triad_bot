from discord.ext import commands

import modules.admin as admin
import modules.copypasta as copypasta
import modules.money as money
import modules.temperature as temperature
import modules.time as time
import modules.weather as weather
from modules.config import Config

# Load the config
CONFIG_FILENAME = 'config.json'
config = Config(CONFIG_FILENAME)

# Instanciate the bot
bot = commands.Bot(command_prefix=config.config['command_prefix'],
                   description=config.config['description'])


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


bot.add_cog(weather.Weather(bot, config))
bot.add_cog(money.Money(bot))
bot.add_cog(temperature.Temperature(bot))
bot.add_cog(time.Time(bot))
bot.add_cog(copypasta.Copypasta(bot, config))
bot.add_cog(admin.Admin(bot, config))
bot.run(config.config['_keys']['token'])
