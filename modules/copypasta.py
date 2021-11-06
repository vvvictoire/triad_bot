"""Copypasta commands"""
import os
import random

import discord
from discord.ext import commands


class Copypasta(commands.Cog):
    """Copypasting commands"""
    def __init__(self, bot, config) -> None:
        super().__init__()
        self.bot = bot
        self.config = config.config

    def read_from_file(self, filename):
        """Reads a file"""
        with open(filename, 'r', encoding="utf-8") as file:
            return file.read()

    def random_carl(self):
        """Pick a random filename in rare_carls folder"""
        carls = os.listdir('rare_carls')
        carl = random.choice(carls)
        return "rare_carls/" + carl

    def carl_count(self):
        """Counts how many carls in rare_carls folder"""
        carls = os.listdir('rare_carls')
        return len(carls)

    @commands.command()
    async def ass(self, context):
        """Sends a random As Above, So Below message"""
        await context.send('ASS BASTARD BELOW')
        # as HECKIN soos

    @commands.command()
    async def carl(self, context):
        """Shows a random Rare Carl!"""
        with open(self.random_carl(), "rb") as filehandle:
            filehandle = discord.File(filehandle)
        await context.send(file=filehandle)

    @commands.command()
    async def carlcount(self, context):
        """Displays how many Rare Carls do we have"""
        number_of_carls = self.carl_count()
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
        invisible = f"<:invisible:{self.config['emojis']['invisible']}>"
        siesta = f"<:siesta:{self.config['emojis']['siesta']}>"
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
        copypasta = self.read_from_file("copypastas/navy_seal.txt")
        await context.send(copypasta)

    @commands.command()
    async def rick(self, context):
        """Wubba lubba dub dub"""
        copypasta = self.read_from_file("copypastas/IQ.txt")
        await context.send(copypasta)
