from discord.ext import commands
import lib_triad_bot as ltb


class Time(commands.Cog):
    """Time in other timezones, and countdowns"""
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command()
    async def aztime(self, context):
        """Current time in Arizona"""
        timestring = ltb.arizona_time().strftime("%H:%M")
        await context.send(f'Arizonian time is {timestring}')

    @commands.command()
    async def frtime(self, context):
        """Current time in France"""
        timestring = ltb.paris_time().strftime("%H:%M")
        await context.send(f'Paris time is {timestring}')

    @commands.command()
    async def countdown(self, context):
        """How many days until The Meetup?"""
        delta = ltb.time_to_paris()
        await context.send(
            f'Meeting up in {delta["weeks"]} weeks and {delta["days"]} days')
