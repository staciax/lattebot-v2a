# Standard 
import discord , asyncio , re 
from discord.ext import commands
from datetime import datetime, timedelta, timezone

# Third party
#from discord_components import *

# Local
import utils

emojis = utils.emoji_converter

class Help(commands.Cog, name="Help command"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        #DiscordComponents(self.bot)
        print(f"{self.__class__.__name__} cog has been loaded\n-----")

    @commands.command(
        name="help", aliases=["h", "commands"], description="The help command!"
    )
    async def help(self, ctx):

        embedhelp = discord.Embed(title="✧ LATTE Help", description="Prefix of this bot `lt `\nUse `selection` below for more info on an command. \n",color=0xffffff)
        embedhelp.add_field(name='** **', value=f"•{emojis('shidapout')} **Utility**\n•{emojis('winkai')} **Giveaway**\n•{emojis('chocolawow')} **Reaction Roles**")
        embedhelp.add_field(name='** **', value=f"•{emojis('ShinoSmirk')} **Infomation**\n•{emojis('wowanime')} **Fun**\n•{emojis('ClevelandDeal')} **Leveling**")
        embedhelp.add_field(name='** **', value=f"•{emojis('lutoaraka')} **Moderation**\n•{emojis('Ani1')} **Meta**\n•{emojis('tohka')} **NSFW**")

#        embedhelp.add_field(name='** **', value=f"**Support**\n {INVITELINK} | {SUPPORT_SERVER} | {GITHUB_DEV}", inline=False)
        lastup = datetime(2020, 8, 3)
        dt = lastup.strftime("%d %B %Y") #%A,
        embedhelp.set_footer(text=f"Recently Updated • {dt}")
        embedhelp.set_image(url="https://i.imgur.com/3jz8m3V.png")
      
        msg = await ctx.send(embed=embedhelp,
        components=
        [Select(placeholder="Select a catogory",
                            options=[
                                SelectOption(
                                    label="Utility",
                                    value="test1.2",
                                    description="Utility Commands",
                                    emoji=self.bot.get_emoji(867683219733348363)
                                ),
                                SelectOption(
                                    label="Infomation",
                                    value="test2.2",
                                    description="Infomation commands",
                                    emoji=self.bot.get_emoji(867686091501994004)
                                ),
                                SelectOption(
                                    label="Moderation",
                                    value="test3.2",
                                    description="Moderation commands",
                                    emoji=self.bot.get_emoji(867683214298054696)
                                ),
                                SelectOption(
                                    label="Giveaway",
                                    value="test4.2",
                                    description="Giveaway commands",
                                    emoji=self.bot.get_emoji(867701465983615006)
                                ),
                                SelectOption(
                                    label="Fun",
                                    value="test5.2",
                                    description="Fun commands",
                                    emoji=self.bot.get_emoji(867701428998635522) #""
                                ),
                                SelectOption(
                                    label="Meta",
                                    value="test6.2",
                                    description="Game commands",
                                    emoji=self.bot.get_emoji(867705949933666324)
                                ),
                                SelectOption(
                                    label="Reaction",
                                    value="test7.2",
                                    description="Reaction roles",
                                    emoji=self.bot.get_emoji(867704973865254922)
                                ),
                                SelectOption(
                                    label="Leveling",
                                    value="test8.2",
                                    description="Leveling",
                                    emoji=self.bot.get_emoji(867693328560947200)
                                ),
                                SelectOption(
                                    label="NSFW",
                                    value="test9.2",
                                    description="NSFW",
                                    emoji=self.bot.get_emoji(867707490379628564)
                                ),
                                SelectOption(
                                    label="Help",
                                    value="test10.2",
                                    description="back to main page",
                                    emoji=self.bot.get_emoji(864921120226279504)
                                ),
                            ])]
                            )

        while True:
            try:
                event = await self.bot.wait_for("select_option", check=None)
                label = event.component[0].label

                if label == "Utility":
                    await event.respond(
                        type=7,
                        embed=utils.Utility(ctx)
                    )

                elif label == "Infomation":
                    await event.respond(
                        type=7,
                        embed=utils.Infomation(ctx)
                    )
          
                elif label == "Moderation":
                    await event.respond(                        
                        type=7,
                        embed=utils.Moderation(ctx)
                    )
                
                elif label == "Giveaway":
                    await event.respond(                        
                        type=7,
                        embed=utils.Giveaway(ctx)
                    )
                
                elif label == "Fun":
                    await event.respond(                        
                        type=7,
                        embed=utils.Fun(ctx)
                    )

                elif label == "Meta":
                    await event.respond(                        
                        type=7,
                        embed=utils.Meta(ctx)
                    )

                elif label == "Reaction":
                    await event.respond(                        
                        type=7,
                        embed=utils.Reaction(ctx)
                    )
                
                elif label == "Leveling":
                    await event.respond(                        
                        type=7,
                        embed=utils.Leveling(ctx)
                    )
                elif label == "NSFW":
                    await event.respond(                        
                        type=7,
                        embed=utils.NSFW(ctx)
                    )

                elif label == "Help":
                    await event.respond(                        
                        type=7,
                        embed=embedhelp
                    )

            except discord.NotFound:
                print("error.") 


def setup(bot):
    bot.add_cog(Help(bot))
