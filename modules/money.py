from discord.ext import commands
import lib_triad_bot as ltb


class Money(commands.Cog):
    """Converting currencies"""
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command()
    async def usd(self, context, amount):
        """Convert the EUR amount into USB"""
        amount = float(amount)
        dollars = ltb.eur_to_usd(amount)
        await context.send(f'{amount} € in USD is ${dollars:.2f}')

    @commands.command()
    async def eur(self, context, amount):
        """Convert the USD amount into EUR"""
        amount = float(amount)
        euros = ltb.usd_to_eur(amount)
        await context.send(f'${amount} in EUR is {euros:.2f} €')
