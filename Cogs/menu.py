import discord
from bot import Bot

class MyView(discord.ui.View):
    '''
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Choose a Flavor!", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Vanilla",
                description="Pick this if you like vanilla!"
            ),
            discord.SelectOption(
                label="Chocolate",
                description="Pick this if you like chocolate!"
            ),
            discord.SelectOption(
                label="Strawberry",
                description="Pick this if you like strawberry!"
            )
        ]
    )
    async def select_callback(self, select:discord.ui.Select, interaction): # the function called when the user is done selecting options
        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")
    '''
    '''
    @discord.ui.select(
        select_type=discord.ComponentType.user_select
    )
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f"Hello, {select.values[0].mention}")'
    
    '''
    '''
    @discord.ui.select(
        select_type=discord.ComponentType.channel_select,
        channel_types=[discord.ChannelType.text]
    )
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f"You selected {select.values[0].mention}")
    '''

    '''
    @discord.ui.button(label="Button 1", row=0, style=discord.ButtonStyle.primary)
    async def first_button_callback(self, button, interaction):
        await interaction.response.send_message("You pressed me!")

    @discord.ui.button(label="Button 2", row=0, style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message("You pressed me!")
    ''' 
    
    '''
    async def on_timeout(self) :#discord.ui.View.on_timeout
        self.disable_all_items()
        await self.message.edit(content="You took too long! Disabled all the components.", view=self)
    '''
    @discord.ui.select(
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Vanilla",
                description="Pick this if you like vanilla!"
            ),
            discord.SelectOption(
                label="Chocolate",
                description="Pick this if you like chocolate!"
            ),
            discord.SelectOption(
                label="Strawberry",
                description="Pick this if you like strawberry!"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")
    

class Menu(discord.Cog):
    def __init__(self,bot:Bot):
        self.bot=Bot
    @discord.slash_command(name='pong') # Create a slash command
    async def pong(self,ctx:discord.ApplicationContext):
        await ctx.respond("pong!", view=MyView(timeout=7)) # Send a message with our View class that contains the button
def setup(bot:Bot):
    bot.add_cog(Menu(bot))