import discord
import os , random , traceback , platform , asyncio
from discord.ext import commands
from datetime import datetime, timedelta, timezone
import time
from time import perf_counter
from dateutil.relativedelta import relativedelta

from user_config import *
import utils

class Data(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.launch_time = datetime.utcnow()
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx, statusType: str, *, statusText):

        if statusType.lower() == "playing":  # Setting `Playing ` status
            await self.bot.change_presence(activity=discord.Game(name=statusText))
        if statusType.lower() == "streaming":  # Setting `Streaming ` status
            await self.bot.change_presence(activity=discord.Streaming(name=statusText, url=""))
        if statusType.lower() == "listening":  # Setting `Listening ` status
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=statusText))
        if statusType.lower() == "watching":  # Setting `Watching ` status
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=statusText))

        embed = discord.Embed(
            description=f"{utils.emoji_converter('check')} **Status Changed!**\n\n`{statusText}`", color=0xffffff)
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title=f"**invite bot**",description=f"**✧ LATTE Bot**\n♡ ꒷ now is online **{len(self.bot.guilds)}** servers︰𓂃 ꒱\n\n⸝⸝﹒{INVITELINK} ꒱",color=0xFFFFFF,timestamp=datetime.now(timezone.utc))
        embed.set_thumbnail(url=self.bot.user.avatar.url)
#       embed.set_image(url='https://i.imgur.com/rzGqQwn.png')
#         embed.set_footer(text = f'Req by {ctx.author}', icon_url = ctx.author.avatar.url)
        
        await ctx.send(embed=embed)   
    
    @commands.command(description="bot latency")
    async def ping(self, ctx):
        #bot
        bot_latency = round(self.bot.latency * 1000)
        #typings
        typings = time.monotonic()
        await ctx.trigger_typing()
        typinge = time.monotonic()
        typingms = round((typinge - typings) * 1000)
        #database
        dbstart = time.monotonic()
        self.bot.db
        dbend = time.monotonic()
        db_time = round((dbend - dbstart) * 1000)

        embed = discord.Embed(description="", color=0xc4cfcf)
        embed.add_field(name=f"{utils.emoji_converter('latteicon')} Latency",
                        value=f"```nim\n{bot_latency} ms```", inline=True)
        embed.add_field(name=f"{utils.emoji_converter('typing')} Typing",
                        value=f"```nim\n{typingms} ms```", inline=True)
        embed.add_field(name=f"{utils.emoji_converter('mongodb')} Database",
                        value=f"```nim\n{db_time} ms```", inline=True)

        await ctx.send(embed=embed)
    
    @commands.command(name="stats")
    @commands.is_owner()
    async def stats(self, ctx):

        BotVersion = BOTVERSION
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))
        totalcogs = len(self.bot.cogs)
        totalcommands = len(self.bot.commands)

        delta_uptime = relativedelta(datetime.utcnow(), self.bot.launch_time)
        days, hours, minutes, seconds = delta_uptime.days, delta_uptime.hours, delta_uptime.minutes, delta_uptime.seconds
        data_time = utils.data_time(seconds, minutes, hours, days)

        embed = discord.Embed(description='\uFEFF', colour=0xffffff, timestamp=datetime.now(timezone.utc)) #title=f'{self.bot.user.name} Stats',
        
        fields = [("Bot version:",f"```{BotVersion}```", True),
                    ("Python version:",f"```{pythonVersion}```", True),
                    ("Discord.py version:",f"```{dpyVersion}```", True),
                    ("Total servers:",f"```{serverCount}```", True),
                    ("Total users:",f"```{memberCount}```", True),
                    ("Uptime:",f"```{data_time}s```", True),
                    ("Total Cogs:",f"```{totalcogs}```", True),
					("Total Commands:",f"```{totalcommands}```", True),
                    ("Bot developers:","```ꜱᴛᴀᴄɪᴀ.#0001 (385049730222129152)```", False)]
            
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        
        lastup = datetime(2021, 8, 3)
        dt = lastup.strftime("%d %B %Y") #%A,
        embed.set_footer(text=f"Recently Updated • {dt}")
#        embed.set_footer(text=f"Req by {ctx.author}" , icon_url = ctx.author.avatar.url) # (text=f"Req by {ctx.author} | {self.bot.user.name}"
        embed.set_author(name=f"{self.bot.user.name} Stats", icon_url=self.bot.user.avatar.url)
#        embed.set_image(url=ctx.guild.banner.url)
#        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.send(embed=embed)
    
    @commands.command(name='uptime')
    @commands.is_owner()
    async def uptime(self, ctx: commands.Context):
        """Gets the uptime of the bot"""
        
        delta_uptime = relativedelta(datetime.utcnow(), self.bot.launch_time)
        days, hours, minutes, seconds = delta_uptime.days, delta_uptime.hours, delta_uptime.minutes, delta_uptime.seconds

        uptimes = {x[0]: x[1] for x in [('days', days), ('hours', hours),
                                        ('minutes', minutes), ('seconds', seconds)] if x[1]}

        last = "".join(value for index, value in enumerate(uptimes.keys()) if index == len(uptimes)-1)
        uptime_string = "".join(
            f"{v} {k}" if k != last else f" and {v} {k}" if len(uptimes) != 1 else f"{v} {k}"
            for k, v in uptimes.items()
        )
        
        await ctx.channel.send(f'I started {uptime_string} ago.')
    
    @commands.command(aliases=['botdis', 'lattelg'])
    @commands.is_owner()
    async def logout2(self, ctx):
        embed = discord.Embed(description="`Latte bot is disconnect`",color=0xffffff,timestamp=datetime.now(timezone.utc))
        embed.set_footer(text=f"Logout by {ctx.author}" , icon_url = ctx.author.avatar_url)
        embed.set_author(name=f"{self.bot.user.name} Logout", icon_url=self.bot.user.avatar.url)
        embed.set_thumbnail(url=self.bot.user.avatar.url)

        await ctx.send(embed=embed) 
        await self.bot.logout()
    
    @commands.command(name="bm")
    async def bm(self, ctx, *, message=None):
        embed = discord.Embed(description=f"{utils.emoji_converter('xmark')} Please specify what message bot send the message | `prefix` `bm [message]`",color=0xffffff)
        if message == None:
            message = await ctx.send(embed=embed)
        else:
            await ctx.send(f'{message}')
            await ctx.message.delete()
    
    @commands.command(aliases=['report','bug','fb'])
    async def feedback2(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        embedwait = discord.Embed(title="FEED BACK",description=f"Please write a feedback.\n\n`note: within 1 minute`",color=0xffffff)
        embedfail = discord.Embed(title="FEED BACK",description=f"{utils.emoji_converter('xmark')} You took to long, please try again.",color=0xffffff)
        await ctx.send(embed=embedwait)
        try:
            msg1 = await self.bot.wait_for('message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send(embed=embedfail)

        reportembed = discord.Embed(title="FEED BACK",
                                 description=f"{msg1.content}",
                                 color=0xffffff)
        reportembed.set_thumbnail(url=ctx.author.avatar.url)

        embedsc = discord.Embed(title="FEED BACK",description=f"{ctx.author.mention} Thank you for feedback {utils.emoji_converter('whiteheart')} !",color=0xffffff)

        await self.log_channel.send(embed=reportembed)
        await ctx.send(embed=embedsc)


def setup(bot):
    bot.add_cog(Data(bot))
