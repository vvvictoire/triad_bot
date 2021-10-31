from discord.ext import commands
import lib_triad_bot as ltb


class Temperature(commands.Cog):
    """Converting temperatures"""
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command()
    async def c(self, context, temperature):
        """Converts degrees Farenheit to degrees Celsius"""
        temperature = float(temperature)
        celsius = ltb.far_to_cel(temperature)
        await context.send(f'{temperature}°F = {celsius:.2f}°C')

    @commands.command()
    async def f(self, context, temperature):
        """Converts degrees Celsius to degrees Farenheit"""
        temperature = float(temperature)
        farenheit = ltb.cel_to_far(temperature)
        await context.send(f'{temperature}°C = {farenheit:.2f}°F')
