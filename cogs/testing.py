import discord
from discord.ext import commands

from utils.util import Pag
#from discord_components import *

class View(discord.ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @discord.ui.select(custom_id="Some identifier", placeholder="Placeholder", min_values=1, max_values=1, options=[discord.SelectOption(label="Hello", emoji="😳")])
    async def callback(self, select: discord.ui.select, interaction: discord.Interaction):
        await interaction.response.send_message('Hello', ephemeral=True) # to get the select options, you can use interaction.data

class Tesing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(name="test1")
    async def testing1(self ,ctx):
        
        await ctx.send('Test', view=View())
    
def setup(bot):
    bot.add_cog(Tesing(bot))
