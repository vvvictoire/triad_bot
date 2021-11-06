"""Money commands"""
from discord.ext import commands


class Money(commands.Cog):
    """Converting currencies"""
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    def usd_to_eur(self, amount):
        """Convert USD to EUR"""
        return amount * 0.86

    def eur_to_usd(self, amount):
        """Convert EUR to USD"""
        return amount * 1.16

    @commands.command()
    async def usd(self, context, amount):
        """Convert the EUR amount into USB"""
        amount = float(amount)
        dollars = self.eur_to_usd(amount)
        await context.send(f'{amount} € in USD is ${dollars:.2f}')

    @commands.command()
    async def eur(self, context, amount):
        """Convert the USD amount into EUR"""
        amount = float(amount)
        euros = self.usd_to_eur(amount)
        await context.send(f'${amount} in EUR is {euros:.2f} €')
