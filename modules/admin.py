"""Admin commands"""
import copy

from discord.ext import commands

from modules import lib_triad_bot as ltb


class Admin(commands.Cog):
    """Admin commands (you shouldn’t be around here tbh)"""
    def __init__(self, bot, config) -> None:
        super().__init__()
        self.bot = bot
        self.config = config

    @commands.command()
    @commands.is_owner()
    async def saveconfig(self, context):
        """Exports the config to CONFIG_FILENAME (disabled for now)"""
        # ltb.save_to_json(Config.config, self.CONFIG_FILENAME)
        # await context.send("Config saved!")

    @commands.command()
    @commands.is_owner()
    async def dumpconf(self, context):
        """Dumps the current config (except the _keys)"""
        conf = copy.deepcopy(self.config.config)
        del conf['_keys']
        conf = ltb.json_to_string(conf)
        await context.send(ltb.pretty_print_json(conf))

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, context):
        """Shuts off the bot"""
        await context.send('Good night!')
        exit()
