import discord
from bot import Bot

class qrcode(discord.Cog):
    ...
def setup(bot:Bot):
    bot.add_cog(qrcode(bot))