import discord 
from bot import Bot

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Short Input"))
        self.add_item(discord.ui.InputText(label="Long Input", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Modal Results")
        embed.add_field(name="Short Input", value=self.children[0].value)
        embed.add_field(name="Long Input", value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])
class test(discord.Cog):
    @discord.slash_command(name="modal_slash")
    async def modal_slash(self,ctx: discord.ApplicationContext):
        """Shows an example of a modal dialog being invoked from a slash command."""
        modal = MyModal(title="Modal via Slash Command")
        await ctx.send_modal(modal)
def setup(bot:Bot):
    bot.add_cog(test(bot))