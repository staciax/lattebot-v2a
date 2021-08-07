import discord , random , time , re , os
from discord.ext import commands
from datetime import datetime, timedelta, timezone

# Third party

# Local
import utils
from user_config import *

emoji_s = utils.emoji_converter

class Infomation(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    def our_custom_check():
        async def predicate(ctx):
            return ctx.guild is not None \
                and ctx.author.guild_permissions.manage_channels \
                and ctx.me.guild_permissions.manage_channels
        return commands.check(predicate) #@our_custom_check()

    def is_it_me(ctx):
        return ctx.author.id == 385049730222129152 #@commands.check(is_it_me)
    
    @commands.command(aliases=['sv'])
    async def serverinfo(self, ctx):

        #afk_channel_check and timeout
        sec = utils.afk_channel_timeout(ctx)

        #member_status and emoji_member_status
        statuses = utils.member_status(ctx)
        
        #emoji_count
        memberCount = str(ctx.guild.member_count)
        emojitotal = len(ctx.guild.emojis)
        emojiregular = len([emoji for emoji in ctx.guild.emojis if not emoji.animated])
        emojianimated = len([emoji for emoji in ctx.guild.emojis if emoji.animated])

        embed = discord.Embed(title=f"Server info - {ctx.guild.name}",color=0xffffff)
        fields = [("Server name",ctx.guild.name, True),
				("Server Owner",f"{ctx.guild.owner.display_name}#{ctx.guild.owner.discriminator}\n{ctx.guild.owner.mention}", True),
                ("Server Region",str(ctx.guild.region).title(), True),
                ("Server Member",len([member for member in ctx.guild.members if not member.bot]), True),
                ("Server Bots",len([Member for Member in ctx.guild.members if Member.bot]), True),
                ("Server Roles",len(ctx.guild.roles), True),
                ("Text Channels",len(ctx.guild.text_channels), True),
                ("Voice Channels",len(ctx.guild.voice_channels), True),
                ("Stage Chennels",len(ctx.guild.stage_channels), True),
                ("Category size",len(ctx.guild.categories), True),
                ("AFK Chennels",ctx.guild.afk_channel, True),
                ("AFK Timer",sec,True),
                ("Rules Channel",utils.rules_channel(ctx),True),
                ("System Channel",utils.system_channel(ctx),True),
                ("Verification Level",utils.system_channel(ctx),True),
                ("Activity",f"{emoji_s('member')} **Total:** {memberCount}\n{emoji_s('online')} **Online:** {statuses[0]} \n{emoji_s('idle')} **Idle:** {statuses[1]} \n{emoji_s('dnd')} **Dnd:** {statuses[2]} \n{emoji_s('offline')} **Offline:** {statuses[3]}",True),
                ("Boosts",utils.check_boost(ctx),True),
                ("Emoji",f"**Total:** {emojitotal}\n**Regular:** {emojiregular}\n**Animated:** {emojianimated}",True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        embed.set_thumbnail(url=ctx.guild.icon.url)
    
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Infomation(bot))
