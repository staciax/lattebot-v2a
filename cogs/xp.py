# Standard 
import discord , random , asyncio
from discord.ext import commands 
from datetime import datetime, timedelta, timezone

intents = discord.Intents.default()
intents.members = True

# Third party
from PIL import Image, ImageDraw , ImageFont , ImageEnhance , ImageFilter
from io import BytesIO
import requests

# Local
import utils
from user_config import * 
from utils.util import Pag

#xpchannel
bot_channel = BOT_CH
chat_channel = CHAT_CH
level = LVLROLE #level role
levelnum = LVLNUM #level number

class xp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded\n-----")
    
    @commands.command(name="set_ch_exp")
    async def set_channel_exp(self, ctx , channel: discord.TextChannel):
        if channel is None:
            await ctx.send("You did not give me a channel, therefore I will use the current one!")
        channel = channel or ctx.channel
        data = await self.bot.lvl_guild.find_by_custom({"guild_id": ctx.guild.id, "channel_id": channel.id})
        if data is None:
            data = {
                "guild_id": ctx.guild.id,
                "channel_id": channel.id
            }
            await self.bot.lvl_guild.upsert_custom({"guild_id": ctx.guild.id, "channel_id": channel.id}, data)
            await ctx.send("test")
        else:
            await ctx.send("test you have")
    
    @commands.command(name="del_ch_exp")
    async def delete_channel_exp(self, ctx , channel: discord.TextChannel):
        if channel is None:
            await ctx.send("You did not give me a channel, therefore I will use the current one!")
        channel = channel or ctx.channel
        data = {"guild_id": ctx.guild.id, "channel_id": channel.id}

        data_deleted = await self.bot.lvl_guild.delete_by_custom(data)
        if data_deleted and data_deleted.acknowledged:
            await ctx.send(
                f"I deleted {channel.mention}"
            )
        else:
            await ctx.send(
                f"I could not find channel"
            )
        
    @commands.Cog.listener()
    async def on_message(self, message):
        data_check = await self.bot.lvl_guild.find_by_custom({"guild_id": message.guild.id, "channel_id": message.channel.id})

        if data_check:
            data = await self.bot.lvling.find_by_custom(
            {"user_id": message.author.id, "guild_id": message.guild.id}
        )
            if data is None:
                data = {
                    "user_id": message.author.id,
                    "guild_id": message.guild.id,
                    "count": 0,
                }
            xp = data["count"]
            data["count"] += 5
            await self.bot.lvling.update_by_custom(
                {"user_id": message.author.id, "guild_id": message.guild.id}, data
            )
            lvl = 0 
            while True:
                if xp < ((50*(lvl**2))+(50*lvl)):
                    break
                lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                if xp == 0:
                    emlvup = discord.Embed(title="LEVEL UP!", description=f"Congratulations, {message.author.mention} you leveled up to **level {lvl}.**!",color=0xffffff)
                    msg = await message.channel.send(embed=emlvup)
                    for i in range(len(level)):
                        if lvl == levelnum[i]:
                            await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                            embed = discord.Embed(title="LEVEL UP!",description=f"Congratulations, {message.author.mention} you leveled up to **level {lvl}.**!\nyou have gotten role **{level[i]}**!!!",color=0xffffff)
#                           embed.set_thumbnail(url=message.author.avatar.url)
                            await msg.edit(embed=embed)
    
    @commands.command(aliases=['rank', 'ranking'])
    async def leaderboard(self, ctx): #only one ch use '==' , more use 'in'
        i = 1
        embed = discord.Embed(color=0x77dd77 , timestamp=datetime.now(timezone.utc))
        embed.set_footer(text = f'{ctx.guild.name}', icon_url=ctx.guild.icon.url)
        embed.set_author(name=f"{self.bot.user.name} Rankings", url=self.bot.user.avatar.url)
        lvling_filter = {"guild_id": ctx.guild.id}
        warns = await self.bot.lvling.find_many_by_custom(lvling_filter)
        
        warns = sorted(warns, key=lambda x: x["count"])
        for x in reversed(warns):
                try:
                    temp = ctx.guild.get_member(x["user_id"])
                    tempxp = x["count"]  
                    embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempxp} ", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
        
        await ctx.channel.send(embed=embed)
        
def setup(bot):

    bot.add_cog(xp(bot))