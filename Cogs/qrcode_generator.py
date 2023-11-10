import discord
from bot import Bot
import qrcode

class Qrcode(discord.Cog):

    def __init__(self,bot:Bot):
        self.bot=bot

    @discord.slash_command(name='qrcode產生器',description='QRCode產生器')
    async def Qrcode_(self,ctx:discord.ApplicationContext,text:discord.Option(str,description="輸入文字或網址")):

        qr=qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4 
        )
        
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image()      
        img.save('qrcode.png')

        with open('qrcode.png','rb') as f:
            qrcode_file = discord.File(f)
            await ctx.send_response(file=qrcode_file)

def setup(bot:Bot):
    bot.add_cog(Qrcode(bot))