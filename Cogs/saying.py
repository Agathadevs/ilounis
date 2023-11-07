import discord
from bot import Bot
import requests
from bs4 import BeautifulSoup
import random

url = 'https://www.lib.ncnu.edu.tw/index.php/tw/2012-03-07-13-55-04/%E7%89%B9%E5%88%A5%E5%B1%95%E7%A4%BA%E3%80%81%E7%89%B9%E5%88%A5%E6%B4%BB%E5%8B%95/2012-03-01-01-36-27.html'
data = requests.get(url) 
soup=BeautifulSoup(data.text,'html5lib')
soup=soup.css.select('tbody > tr')

description_=[]

description_list=soup[0].find_all('td')
for i in description_list:
    description_.append(i.get_text())

class saying(discord.Cog):
    def __init__(self,bot:Bot):
         self.bot=bot
    
    @discord.slash_command(name='佳句')
    async def 名言(self,ctx: discord.ApplicationContext):

        Introduction_sentences=soup[random.randint(1,852)].find_all('td')
        start=0
        dict={}
        for i in Introduction_sentences:
            if i.text.strip():
                ...
            else:
                i.string='無'
            material={description_[start]:i.get_text()}
            dict.update(material)
            start+=1

        embed=discord.Embed(title='📖佳句',
                            description=f"「{dict['佳句']}」",
                            color=0x1297a3,
                            fields=[discord.EmbedField( name='作者',
                                                        value=f"> {dict['作者']}",
                                                        inline=True),
                                    discord.EmbedField( name='作者簡介',
                                                        value=f"> {dict['作者簡介']}",
                                                        inline=True),
                                    discord.EmbedField( name="書名",
                                                        value=f"> {dict['書名']}",
                                                        inline=True)])
        
        await ctx.respond(embed=embed)
 
def setup(bot:Bot):
    bot.add_cog(saying(bot))