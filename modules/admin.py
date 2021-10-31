from discord.ext import commands
import copy
import lib_triad_bot as ltb
from modules.config import Config


class Admin(commands.Cog):
    """Admin commands (you shouldn’t be around here tbh)"""
    def __init__(self, bot, CONFIG_FILENAME) -> None:
        super().__init__()
        self.bot = bot
        self.CONFIG_FILENAME = CONFIG_FILENAME

    def admin_locked(context):
        return context.message.author.id in Config.config['admins']

    @commands.command()
    @commands.check(admin_locked)
    async def saveconfig(self, context):
        """Exports the config to CONFIG_FILENAME"""
        ltb.save_to_json(Config.config, self.CONFIG_FILENAME)
        await context.send("Config saved!")

    @commands.command()
    @commands.check(admin_locked)
    async def dumpconf(self, context):
        """Dumps the current config (except the _keys)"""
        conf = copy.deepcopy(Config.config)
        del conf['_keys']
        conf = ltb.json_to_string(conf)
        await context.send(ltb.pretty_print_json(conf))

    @commands.command()
    @commands.check(admin_locked)
    async def shutdown(self, context):
        """Shuts off the bot"""
        await context.send('Good night!')
        exit()
