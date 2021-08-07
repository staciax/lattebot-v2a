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
from itertools import groupby
import json
import numpy as np

# Local
import utils
from user_config import * 
from utils.util import Pag

#xp_config
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
    @commands.cooldown(1, 15, commands.BucketType.guild)
    async def set_channel_exp(self, ctx , channel: discord.TextChannel = None):
        if channel is None:
            await ctx.send("You did not give me a channel, therefore I will use the current one!")
        channel = channel or ctx.channel
        data = await self.bot.lvl_guild.find_by_custom({"guild_id": ctx.guild.id, "channel_id": channel.id})
        embed = discord.Embed(title="Add Channel EXP")
        embed.add_field(name=f"Channel", value=f"{channel.mention}", inline=False)

        m = await ctx.send("Are these all valid?", embed=embed , delete_after=60)
        await m.add_reaction("✅")
        await m.add_reaction("🇽")

        try:
            reaction, member = await self.bot.wait_for(
                "reaction_add",
                timeout=60,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )
        except asyncio.TimeoutError:
            await ctx.send("Confirmation Failure. Please try again.")
            return

        if str(reaction.emoji) not in ["✅", "🇽"] or str(reaction.emoji) == "🇽":
            await ctx.send("add channel cancelling")
            return
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
    @commands.cooldown(1, 15, commands.BucketType.guild)
    async def delete_channel_exp(self, ctx , channel: discord.TextChannel=None):
        if channel is None:
            await ctx.send("You did not give me a channel, therefore I will use the current one!")
        channel = channel or ctx.channel
        data = {"guild_id": ctx.guild.id, "channel_id": channel.id}
        data_deleted = await self.bot.lvl_guild.delete_by_custom(data)
        
        if bool(data_deleted) == False:
            print("data false")
            return

        embed = discord.Embed(title="Delete Channel EXP")
        embed.add_field(name=f"Channel", value=f"{channel.mention}", inline=False)

        m = await ctx.send("Are these all valid?", embed=embed , delete_after=60)
        await m.add_reaction("✅")
        await m.add_reaction("🇽")

        try:
            reaction, member = await self.bot.wait_for(
                "reaction_add",
                timeout=60,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )
        except asyncio.TimeoutError:
            await ctx.send("Confirmation Failure. Please try again.")
            return

        if str(reaction.emoji) not in ["✅", "🇽"] or str(reaction.emoji) == "🇽":
            await ctx.send("Delete channel cancelling")
            return

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
        filter_lvl = await self.bot.reward_role.find_many_by_custom({"guild_id": message.guild.id})
        filting_lvl = sorted(filter_lvl, key=lambda x: x["role_id"])

        if bool(filting_lvl) == True:
            print("true filting_lvl")
        else:
            print("false filting_lvl")

        filted_lvl = []
        filted_role = []

        for x in filting_lvl:
            lvl_id = x["level_id"]
            role_id = x["role_id"]
            filted_lvl.append(lvl_id)
            filted_role.append(role_id)

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
            print(f'now level{lvl}')
            xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
            if xp == 0:
                if bool(filting_lvl) == True:
                    emlvup = discord.Embed(title="LEVEL UP!", description=f"Congratulations, {message.author.mention} you leveled up to **level {lvl}.**!",color=0xffffff)
                    msg = await message.channel.send(embed=emlvup)
                    for i in range(len(filted_role)):
                        if lvl == filted_lvl[i]:
                            print(filted_role[i])
                            await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=filted_role[i]))
                            embed = discord.Embed(title="LEVEL UP!",description=f"Congratulations, {message.author.mention} you leveled up to **level {lvl}.**!\nyou have gotten role **{level[i]}**!!!",color=0xffffff)
                            await msg.edit(embed=embed)
                else:
                    embed_basic = discord.Embed(title="LEVEL UP!", description=f"Congratulations, {message.author.mention} you leveled up to **level {lvl}.**!",color=0xffffff)
                    msg = await message.channel.send(embed=embed_basic)
                    for i in range(len(level)):
                        if lvl == levelnum[i]:
                            await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                            embed = discord.Embed(title="LEVEL UP!",description=f"Congratulations, {message.author.mention} you leveled up to **level {lvl}.**!\nyou have gotten role **{level[i]}**!!!",color=0xffffff)
                            await msg.edit(embed=embed)

    
    @commands.command(aliases=['rank', 'ranking'])
    @commands.cooldown(1, 10, commands.BucketType.guild)
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

    @commands.command(aliases=['lv', 'lvl' , 'xp' , 'exp'])
    @commands.cooldown(1, 15, commands.BucketType.guild)
    async def level(self, ctx, member: discord.Member = None): 
                if not member:  # if member is no mentioned
                    member = ctx.message.author
                member_id = member.id
#        if ctx.channel.id in bot_channel:   
                data_user = await self.bot.lvling.find_by_custom(
                    {"user_id": member.id, "guild_id": ctx.guild.id}
                )
                if data_user is None:
                    embed = discord.Embed(description="You haven't sent any messages, **no xp**!!",color=0xffffff)
                    await ctx.channel.send(embed=embed)
                else:
                    xp = data_user["count"]
                    lvl = 0
                    rank = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    final_xp = (200*((1/2)*lvl))

                    lvling_filter = {"guild_id": ctx.guild.id}
                    warns = await self.bot.lvling.find_many_by_custom(lvling_filter)        
                    warns = sorted(warns, key=lambda x: x["count"])
                    for x in reversed(warns):
                        rank += 1
                        if data_user["user_id"] == x["user_id"]:
                            break

                    embedlv = discord.Embed(title=f"{member.name}'s level stats | {ctx.guild.name}",color=0x77dd77)
                    embedlv.set_image(url="attachment://latte-level.png")

                    await ctx.channel.send(file=utils.level_images(member, final_xp, lvl, rank, xp), embed=embedlv)
    
    @commands.command(name="basic-role")
    @commands.cooldown(1, 15, commands.BucketType.guild)
    async def basic_xp_role(self, ctx):
        embed = discord.Embed(description="", color=PTYELLOW)
        embed.title = "✧ LATTE XP ROLE!"
        lvlbar = "・┈・┈・┈・Level!・┈・┈・┈・⠀⠀"
        lvlbar2 = discord.utils.get(ctx.author.guild.roles, name=lvlbar)
        if not lvlbar2:
            await ctx.guild.create_role(name=lvlbar , colour=0x18191c)
            embed.description += f"{lvlbar.mention}\n"
            embed.description += f"{lvlbar2.mention}\n"
        
            for x, y in zip(reversed(level), reversed(colorlvl)):
                checkrole = discord.utils.get(ctx.author.guild.roles, name=level)
                if not checkrole:
                    await ctx.guild.create_role(name=x , colour=y)
                else:
                    return
        elif lvlbar2:
            for i in reversed(range(len(level))):
                roles = discord.utils.get(ctx.author.guild.roles, name=level[i])
                if roles:
                    embed.description += f"{roles.mention}\n"

            await ctx.channel.send(embed=embed)
        
    @commands.command(name="rewardxp")
    @commands.cooldown(1, 15, commands.BucketType.guild)
    async def reward_role_level(self, ctx, role: discord.Role, level: int = None):
        print(f"{role.id} {level}\n\n")
        level_finding = {"guild_id": ctx.guild.id, "role_id": role.name}
        level_finded = await self.bot.reward_role.find_by_custom(level_finding)

        if level_finded is None:
            level_data = {"guild_id": ctx.guild.id, "role_id": role.name, "level_id": level}
            await self.bot.reward_role.update_by_custom(level_data , level_data)
            await ctx.send("role create")
        else:
            print("found data")
      
def setup(bot):
    bot.add_cog(xp(bot))