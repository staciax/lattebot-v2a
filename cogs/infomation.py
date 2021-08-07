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
        emoji_total = len(ctx.guild.emojis)
        emoji_regular = len([emoji for emoji in ctx.guild.emojis if not emoji.animated])
        emoji_animated = len([emoji for emoji in ctx.guild.emojis if emoji.animated])

        embed = discord.Embed(title=f"Server info - {ctx.guild.name}",color=0xffffff)
        fields = [("Server name",ctx.guild.name, True),
				("Server Owner",f"{ctx.guild.owner.display_name}#{ctx.guild.owner.discriminator}", True),
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
                ("Activity",f"{emoji_s('member')} **Total:** {str(ctx.guild.member_count)}\n{emoji_s('online')} **Online:** {statuses[0]} \n{emoji_s('idle')} **Idle:** {statuses[1]} \n{emoji_s('dnd')} **Dnd:** {statuses[2]} \n{emoji_s('offline')} **Offline:** {statuses[3]}",True),
                ("Boosts",utils.check_boost(ctx),True),
                ("Emoji",f"**Total:** {emoji_total}\n**Regular:** {emoji_regular}\n**Animated:** {emoji_animated}",True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        embed.set_thumbnail(url=ctx.guild.icon.url)
    
        await ctx.send(embed=embed)

    @commands.command(aliases=['ui'] , pass_context=True)
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author  

        #member_status
        mobiles = utils.mobile_status(member)
        desktop = utils.desktop_status(member)
        Web = utils.web_status(member)

        #member_badge
        flags = member.public_flags.all()
        badges ="\u0020".join(utils.profile_converter(f.name) for f in flags)
        if member.bot: badges = f"{badges} {utils.profile_converter('bot')}"
        if member.premium_since: badges = f"{badges} {utils.profile_converter('guildboost')}"

        #member_info
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        member_activity = f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "** **"
        roles = [role for role in member.roles]
        if len(member.roles) > 1:
            role_string = ' '.join([r.mention for r in member.roles][1:])

        embed = discord.Embed(colour=0xffffff)  #timestamp=ctx.message.created_at, #title=f"User Info - {member}")        embed.set_author(name=f"User info - {member}", icon_url=member.avatar.url)
        fields = [("Nickname",f"{member.display_name}", True),
                ("Is bot?","Yes" if member.bot else "No", True),
                ("Activity",member_activity, True),
                ("Join position",f"{str(members.index(member)+1)}/{ctx.guild.member_count}", True),
                ("Joined",member.joined_at.strftime("%d-%m-%Y, %H:%M"), True),
                ("Registered",member.created_at.strftime("%d-%m-%Y, %H:%M"), True),
                ("Status",f"{desktop}\n{mobiles}\n{Web}", True),
                ("Badge :",f"{badges}** **", True),
                ("Top Role",member.top_role.mention, False),
                ("Roles ({})\n".format(len(member.roles)-1),role_string, False)]

        for name , value , inline in fields:
            embed.add_field(name=name , value=value , inline=inline)
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"ID: {member.id}" ) 
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        embed = discord.Embed(title = f"{member.name}'s avatar", color = 0xc4cfcf)
        embed.set_image(url =  member.avatar.url) # Shows the avatar
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Infomation(bot))
