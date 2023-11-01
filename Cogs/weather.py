import discord
from bot import Bot

class Weather(discord.Cog):
    ...

def setup(bot:Bot):
    bot.add_cog(Weather(bot))