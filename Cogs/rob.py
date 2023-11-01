import discord
from bot import Bot

'''
    class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
        @discord.ui.button(label="Button 1", style=discord.ButtonStyle.primary,disabled=True)
        async def first_button_callback(self, button, interaction):
            await interaction.response.send_message("You pressed me!")

        @discord.ui.button(label="Button 2", style=discord.ButtonStyle.primary,disabled=True)
        async def second_button_callback(self, button, interaction):
            await interaction.response.send_message("You pressed me!")

        @discord.ui.button(label="Button 3", style=discord.ButtonStyle.primary)
        async def button_callback(self, button, interaction):
        button.disabled = True # set button.disabled to True to disable the button
        button.label = "No more pressing!" # change the button's label to something else
        await interaction.response.edit_message(view=self) # edit the message's view
        @discord.ui.button(emoji="😀", label="Button 4", style=discord.ButtonStyle.primary)
        async def button_callback(self, button, interaction):
            self.disable_all_items()
            await interaction.response.edit_message(view=self)

        @discord.ui.button(label="Button 5", style=discord.ButtonStyle.primary)
        async def second_button_callback(self, button, interaction):
            self.disable_all_items()
            await interaction.response.edit_message(view=self)

'''
class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) # timeout of the view must be set to None

    @discord.ui.button(label="A button", custom_id="button-1", style=discord.ButtonStyle.primary, emoji="😎")
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You pressed me!",ephemeral=True)

class Rob(discord.Cog):
    def __init__(self,bot:Bot):
        self.bot=Bot
    @discord.slash_command(name='button') # Create a slash command
    async def button(self,ctx:discord.ApplicationContext):
        await ctx.send(f"Press the button! View persistence status: {MyView.is_persistent(MyView())}", view=MyView()) # Send a message with our View class that contains the button

def setup(bot):
    bot.add_cog(Rob(bot))
