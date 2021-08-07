import discord
from discord.ext import commands

def afk_channel_timeout(ctx):
    second = ctx.guild.afk_timeout
    if second == 3600:
        sec = "1 Hour"
    elif second == 1800:
        sec = "30 Minutes"
    elif second == 900:
        sec = "15 Minutes"
    elif second == 300:
        sec = "5 Minutes"
    elif second == 60:
        sec = "1 Minute"
    
    if ctx.guild.afk_channel == None:
        sec = "None"
    return sec

def member_status(ctx):
    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
				len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
				len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
				len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]    
    return statuses

def rules_channel(ctx):
    rulesch = ctx.guild.rules_channel
    if rulesch == None:
        rs += ("none")
    else:
        rs = ctx.guild.rules_channel.mention   
    return rs

def system_channel(ctx):
    systemch = ctx.guild.system_channel
    if systemch == None:
        sy += ("none")
    else:
        sy = ctx.guild.system_channel.mention
    return sy

def check_boost(ctx):
  if ctx.guild.premium_tier != 0:
    boosts = f'**Level:** {ctx.guild.premium_tier}\n**Boosts:** {ctx.guild.premium_subscription_count}'
    last_boost = max(ctx.guild.members, key=lambda m: m.premium_since or ctx.guild.created_at)
    if last_boost.premium_since is not None:
      boosts = f'{boosts}\n**Last Boost:**\n{last_boost}'
  return boosts