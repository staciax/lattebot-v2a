import discord
from discord.ext import commands
from discord import Embed

def Utility(ctx):
  embed = Embed(title="Utility commands",description=f"Utility Commands\n\n`coming soon`",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Infomation(ctx):
  embed = Embed(title="Infomation Commands",description="Infomation Commands\n\n`userinfo , ui [targer] :` show userinfo infomation\n\n`serverinfo , sv :` show server infomation\n\n`avatar , av [targer] :` show user avatar profile",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Moderation(ctx):
  embed = Embed(title="Moderation Commands",description="Moderation Commands\n\n`clear [number] or all :` clear message\n\n`muterole :` create muterole\n\n`mute [target] :` mute member\n\n`unmute [target] :` unmute member\n\n`kick [target]:` kick member\n\n`ban [target]:` ban member\n\n`unban [target]:`unban member\n\n`lockdown :`disable text channel\n\n`changenick [member]:` change nickname member\n\n`slowmode [seconds]:` set slowmode in channel",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Giveaway(ctx):
  embed = Embed(title="Giveaway Commands",description="Giveaway Commands\n\n`giveaway , g :` The group command for managing giveaways\n\n`reroll :` reroll giveaway",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed
  
def Fun(ctx):
  embed = Embed(title="Fun Commands",description="Fun Commands\n\n`bm [message]:` Let the bot send the message\n\n`poll [message]:` poll in your server",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Meta(ctx):
  embed = Embed(title="Meta Commands",description="Meta Commands\n\n`ping :` check latency bot\n\n`stats :` show stats bot\n\n`invite :` invite the bot!!\n\n`feedback` : send message to bot developer\n\n`support :` Get the invite link for the support server!\n\n`vote :`  Get the voting link for the bot",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Reaction(ctx):
  embed = Embed(title="Reaction",description="Reaction Roles\n\nGive color role: <#840380566862823425>",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def Leveling(ctx):
  embed = Embed(title="Leveling",description="Leveling Commands\nways you can get experience\ntalk in <#861883647070437386> <#840398821544296480>\n\n`level , xp :` check my level\n\n`rank :` show ranking level all member",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed

def NSFW(ctx):
  embed = Embed(title="NSFW",description="NSFW Commands\n\n`coming soon..`",color=0xffffff)
  embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar.url)
  return embed
