from discord.ext import commands
import modules.money
import modules.temperature
import modules.time
from modules.config import Config
import modules.weather
import modules.copypasta
import modules.admin

import lib_triad_bot as ltb

# Important config

CONFIG_FILENAME = 'config.json'
config = ltb.load_from_json(CONFIG_FILENAME)
Config.config = config
# Instanciate the bot
bot = commands.Bot(command_prefix=Config.config['command_prefix'])
bot.description = Config.config['description']


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


bot.add_cog(modules.weather.Weather(bot))
bot.add_cog(modules.money.Money(bot))
bot.add_cog(modules.temperature.Temperature(bot))
bot.add_cog(modules.time.Time(bot))
bot.add_cog(modules.copypasta.Copypasta(bot))
bot.add_cog(modules.admin.Admin(bot, CONFIG_FILENAME))
bot.run(Config.config['_keys']['token'])
