import discord
from bot import Bot
import requests


url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWA-877EA591-BC8A-4DD2-8B60-4272DAC4BBAC&downloadType=WEB&format=JSON'
data = requests.get(url)  

class Weather(discord.Cog):
    def __init__(self,bot:Bot):
        self.bot=bot
    async def get_animal_types(self,ctx: discord.AutocompleteContext):
       
        locate = ctx.options['location']
        match locate:
            case '基隆':
                return
            case '台北':
                return
            case '桃園':
                return
            case '新竹':
                return
            case '苗栗':
                return
            case '台中':
                return
            case '彰化':
                return
            case '南投':
                return
            case '雲林':
                return
            case '嘉義':
                return
            case '台南':
                return
            case '高雄':
                return
            case '屏東':
                return
            case '宜蘭':
                return
            case '花蓮':
                return
            case '台東':
                return
            case '澎湖':
                return
            case '金門':
                return
            case '連江':
                return
    @discord.slash_command(name="查詢天氣")
    async def get_weather_info(self,ctx: discord.ApplicationContext,location:discord.Option(str,['基隆','台北','新北','桃園','新竹','苗栗','台中','彰化','南投','雲林','嘉義','台南','高雄','屏東','宜蘭','花蓮','台東','澎湖','金們','連江'])):
        data_json = data.json() 
        embed=discord.Embed()

def setup(bot:Bot):
    bot.add_cog(Weather(bot))