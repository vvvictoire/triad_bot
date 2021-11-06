"""Admin commands"""
import copy
import json

from discord.ext import commands


class Admin(commands.Cog):
    """Admin commands (you shouldn’t be around here tbh)"""
    def __init__(self, bot, config) -> None:
        super().__init__()
        self.bot = bot
        self.config = config

    def json_to_string(self, _json):
        """Pretty print a json object"""
        return json.dumps(_json, indent=2)

    def pretty_print_json(self, _json):
        """Even more pretty print a json object"""
        return f"```json\n{_json}```"

    def save_to_json(self, object_to_save, filename):
        """Write an object to a JSON"""
        json_string = json.dumps(object_to_save)
        with open(filename, "w", encoding="utf-8") as filehandle:
            filehandle.write(json_string)

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
        conf = self.json_to_string(conf)
        await context.send(self.pretty_print_json(conf))

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, context):
        """Shuts off the bot"""
        await context.send('Good night!')
        exit()
