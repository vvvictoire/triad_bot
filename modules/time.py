"""Time commands"""
import datetime

import pytz
from discord.ext import commands


class Time(commands.Cog):
    """Time in other timezones, and countdowns"""
    def __init__(self, bot, config) -> None:
        super().__init__()
        self.bot = bot
        self.config = config.config

    def arizona_time(self):
        """Get now Arizona time"""
        mst = pytz.timezone('America/Phoenix')
        return datetime.datetime.now(mst)

    def paris_time(self):
        """Get now Paris time"""
        cet = pytz.timezone('Europe/Paris')
        return datetime.datetime.now(cet)

    def time_to_meetup(self):
        """Return a delta between now and the meetup"""
        cet = pytz.timezone('Europe/Paris')
        arrival = datetime.datetime(2022, 2, 12, tzinfo=cet)
        now = datetime.datetime.now(cet)
        delta = arrival - now
        weeks = delta.days // 7
        days = delta.days % 7
        return {"weeks": weeks, "days": days}

    @commands.command()
    async def aztime(self, context):
        """Current time in Arizona"""
        timestring = self.arizona_time().strftime("%H:%M")
        await context.send(f'Arizonian time is {timestring}')

    @commands.command()
    async def frtime(self, context):
        """Current time in France"""
        timestring = self.paris_time().strftime("%H:%M")
        await context.send(f'Paris time is {timestring}')

    @commands.command()
    async def countdown(self, context):
        """How many days until The Meetup?"""
        delta = self.time_to_meetup()
        await context.send(
            f'Meeting up in {delta["weeks"]} weeks and {delta["days"]} days')
