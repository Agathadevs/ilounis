import discord,json
from discord.ext import commands
import discord
from discord import option
from discord import Option
from bot import Bot

class main(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    math=discord.SlashCommandGroup("math","Math related commands")

    @math.command()
    async def add(self,ctx, num1: discord.Option(int),  num2:discord.Option(int)):
        sum = num1 + num2
        await ctx.respond(f"{num1} plus {num2} is {sum}.") 

    @discord.slash_command(name='ping',description="機器人延遲")
    async def ping(self,ctx:discord.ApplicationContext):
        '''
        :bot's latency:
        '''
        await ctx.respond(f"Pong! Latency is {self.bot.latency}")

    async def get_animal_types(self,ctx: discord.AutocompleteContext):
        """
        Here we will check if 'ctx.options['animal_type']' is a marine or land animal and return respective option choices
        """
        animal_type = ctx.options['animal_type']
        if animal_type == 'Marine':
            return ['Whale', 'Shark', 'Fish', 'Octopus', 'Turtle']
        else: # is land animal
            return ['Snake', 'Wolf', 'Lizard', 'Lion', 'Bird']

    @discord.slash_command(name="animal",description="test")
    async def animal(
        self,
        ctx: discord.ApplicationContext,
        animal_type: discord.Option(str, choices=['Marine', 'Land']),
        animal: discord.Option(str, autocomplete=lambda _: ['g'])
        ):
        await ctx.respond(f'You picked an animal type of `{animal_type}` that led you to pick `{animal}`!')

    @discord.slash_command(name="bmi",description="BMI計算機")
    async def bmi(self,ctx: discord.ApplicationContext,height:discord.Option(int,description="身高"),weight:discord.Option(int,description="體重")):
        BMI=weight / ((height/100)**2)
        await ctx.respond(f"{ctx.user.mention}你的BMI為**{BMI:.2f}**")
    

def setup(bot):
    bot.add_cog(main(bot))