import discord
from bot import Bot

class Help(discord.Cog):
    '''
    help comment
    '''
    def __init__(self,bot:Bot):
        self.bot=bot

def setup(bot:Bot):
    bot.add_cog(Help(bot))