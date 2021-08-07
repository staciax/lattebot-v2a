import discord
from utils import emoji_converter

""" Server info converter"""
emoji_s = emoji_converter
m_online = emoji_s('online')
m_offline = emoji_s('offline')
m_idle = emoji_s('idle')
m_dnd = emoji_s('dnd')
m_invisible = emoji_s('invisible')

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

""" member infomation converter"""

def mobile_status(member):
    mobile = str(member.mobile_status)
    if mobile == 'offline':
        mb = f"{m_offline} Mobile"
    elif mobile == 'dnd':
        mb = f"{m_dnd} Mobile"
    elif mobile == 'idle':
        mb = f"{m_idle} Mobile"
    elif mobile == 'online':
        mb = f"{m_online} Mobile"  
    else:
        mb = f"{m_invisible} Mobile"    
    return mb

def desktop_status(member):
    desktop = str(member.desktop_status)
    if desktop == 'offline':
        dt = f"{m_offline} Desktop"
    elif desktop == 'dnd':
        dt = f"{m_dnd} Desktop"
    elif desktop == 'idle':
        dt = f"{m_idle} Desktop"
    elif desktop == 'online':
        dt = f"{m_online} Desktop"       
    else:
        dt = f"{m_invisible} Desktop"
    return dt

def web_status(member):
    Web = str(member.web_status)
    if Web == 'offline':
        wb = f"{m_offline} Web"
    elif Web == 'dnd':
        wb =  f"{m_dnd} Web"
    elif Web == 'idle':
        wb = f"{m_idle} Web"
    elif Web == 'online':
        wb = f"{m_online} Web"
    else:
        wb = f"{m_invisible} Web"
    return wb
