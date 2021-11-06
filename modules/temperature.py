"""Temperature commands"""
from discord.ext import commands


class Temperature(commands.Cog):
    """Converting temperatures"""
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    def far_to_cel(self, amount):
        """Convert Farenheit to Celcius"""
        return (amount - 32) * 5 / 9

    def cel_to_far(self, amount):
        """Convert Celcius to Farenheit"""
        return amount*1.8 + 32

    @commands.command()
    async def c(self, context, temperature):
        """Converts degrees Farenheit to degrees Celsius"""
        temperature = float(temperature)
        celsius = self.far_to_cel(temperature)
        await context.send(f'{temperature}°F = {celsius:.2f}°C')

    @commands.command()
    async def f(self, context, temperature):
        """Converts degrees Celsius to degrees Farenheit"""
        temperature = float(temperature)
        farenheit = self.cel_to_far(temperature)
        await context.send(f'{temperature}°C = {farenheit:.2f}°F')
