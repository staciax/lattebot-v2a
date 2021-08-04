import random
import datetime

import discord
from discord.ext import commands
from datetime import datetime, timezone


# In cogs we make our own class
# for d.py which subclasses commands.Cog


class Events(commands.Cog):

    current_streamers = list()

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="♢・test-bot")
        if channel:
            embed=discord.Embed(
            description=f"ʚ˚̩̥̩ɞ ◟‧Welcome‧ *to* **{member.guild}!** <a:ab__purplestar:854958903656710144>\n　。\nෆ ₊˚don’t forget to check out . . .\n\n♡ ꒷ get latte roles~︰𓂃 ꒱\n⸝⸝﹒<#861774918290636800> \n⸝⸝﹒<#840380566862823425>\n\n⸝⸝﹒||{member.mention}|| ꒱ {utils.emoji_converter('3rd')}", #⊹₊˚**‧Welcome‧**˚₊⊹ 
            timestamp=datetime.now(timezone.utc),
            color=0xc4cfcf
    
            )
            embed.set_author(name=f"{member}", icon_url=member.avatar.url), 
            embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text=f"You're our {member.guild.member_count} members ෆ"),

            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="♢・test-bot")
        if channel:
            embed = discord.Embed(
                    description=f"**Leave Server\n`{member}`**",
                    color=0xdbd7d2)
            embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text="—・see ya good bye")
            embed.timestamp = datetime.now(timezone.utc)

            await channel.send(embed = embed)
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        channel = discord.utils.get(before.guild.text_channels, name="member-log")
        if channel:
            if before.display_name != after.display_name:
                embed = discord.Embed(title="Nickname change",
                                    colour=0xFFDF00, #colour=after.colour,
						            timestamp=datetime.now(timezone.utc))

                fields = [("`Before`", before.display_name, False),
					    ("`After`", after.display_name, False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    embed.set_thumbnail(url=after.avatar.url)
                    embed.set_footer(text="", icon_url=after.avatar.url)

                await channel.send(embed=embed)
        

            elif before.roles != after.roles:
                embed = discord.Embed(title="Role updates",
                                    colour=0xb19cd9, #colour=after.colour,
						            timestamp=datetime.now(timezone.utc))

                fields = [(" `Before`", ", ".join([r.mention for r in before.roles]), False),
					    ("`After`", ", ".join([r.mention for r in after.roles]), False)]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)
                    embed.set_footer(text=f"{after.display_name}", icon_url=after.avatar.url)

                await channel.send(embed=embed)
        else:
            pass
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        channel = discord.utils.get(before.guild.text_channels, name="message-log")
        if channel:
            if not after.author.bot:
                if before.content != after.content:
                    embed = discord.Embed(title="Message edit",
                                colour=0xFF8C00, #after.author.colour,
                                timestamp=datetime.now(timezone.utc))
                
                    fields = [("`Before`", before.content , False),
						    ("`After`", after.content, False)]
                
                    for name, value, inline in fields:
                        embed.add_field(name=name, value=value, inline=inline)
                        embed.set_footer(text=f"{after.author.display_name}", icon_url=after.author.avatar.url)
                
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = discord.utils.get(message.guild.text_channels, name="message-log")
        if channel:
            if not message.author.bot:
                em = discord.Embed(color=0xDC143C,title = f"Message Deleted:")
                em.set_footer(text=self.bot.user.name,icon_url=self.bot.user.avatar.url )
                em.set_author(name=message.author.display_name,icon_url=message.author.avatar.url)

                if message.attachments is not None:
                    if len(message.attachments) > 1:
                        im = [x.proxy_url for x in message.attachments]
                        em.add_field(name='\uFEFF',value = f"This Message Contained {len(message.attachments)} Message Attachments, Please See Below")
                        await channel.send(' '.join(im))
                    elif message.attachments:
                        image = message.attachments[0].proxy_url
                        em.description = f"**Deleted in:** {message.channel.mention}"
                        em.set_image(url=image)
                    else:
                        em.description = f"**Deleted in:** {message.channel.mention} \n**Content:** {message.clean_content}"

                await channel.send(embed=em)
            else:
                pass
        else:
            delem = discord.Embed(color=0xDC143C,title = f"Message Deleted:")
            delem.set_footer(text=self.bot.user.name,icon_url=self.bot.user.avatar.url )
            delem.set_author(name=message.author.display_name,icon_url=message.author.avatar.url)
            delem.description = f"**Deleted in:** {message.channel} \n**Content:** {message.clean_content}"

            await channel.send(embed=delem)

    @commands.Cog.listener()
    async def on_voice_state_update(self , member, before, after):
        channel = discord.utils.get(member.guild.text_channels, name="message-log")
        if channel:
            embed = discord.Embed(description="",timestamp=datetime.now(timezone.utc))
            if member.bot:
                return
        
            if not before.channel:
                embed.description += f"**JOIN CHANNEL** : `{after.channel.name}`"
                embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                embed.color=0xffffff
                await channel.send(embed=embed)
#               print(f'{member.name} Join {after.channel.name}') 
        
            if before.channel and not after.channel:
                embed.description += f"**LEFT CHANNEL** : `{before.channel.name}`"
                embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                embed.color=0xffffff
#            print(f"{member.name} left channel {before.channel.name}")
                await channel.send(embed=embed)
        
            if before.channel and after.channel:
                if before.channel.id != after.channel.id:
                    embed.description += f"**SWITCHED CHANNELS** : `{before.channel.name}` to `{after.channel.name}`"
                    embed.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                    embed.color=0xffffff
                    await channel.send(embed=embed)
#                print("user switched voice channels")
                else:
#                print("something else happend!")
                    if member.voice.self_stream:
                        embedstm = discord.Embed(description=f"**STREAMING in** : `{before.channel.name}`",timestamp=datetime.now(timezone.utc))
                        embedstm.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                        embedstm.colour=0xffffff
                        self.current_streamers.append(member.id)
                        await channel.send(embed=embedstm)

                    elif member.voice.mute:
                        embedmute = discord.Embed(description=f"**SERVER MUTED** in `{after.channel.name}`")
                        embedmute.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                        embedmute.colour=0xffffff
                        await channel.send(embed=embedmute)

                    elif member.voice.deaf:
                        embeddeaf = discord.Embed(description=f"**SERVER DEAFEN** in `{after.channel.name}`")
                        embeddeaf.set_footer(text=f"{member.name}#{member.discriminator}" , icon_url=member.avatar.url)
                        embeddeaf.colour=0xffffff
                        await channel.send(embed=embeddeaf)

#                   elif member.voice.requested_to_speak_at:
#                       print("testing req speak")

                    else:
#                    print("we are here")
                        if member.voice.deaf:
                            print("unmuted")
                        for streamer in self.current_streamers:
                            if member.id == streamer:
                                if not member.voice.self_stream:
                                    print("user stopped streaming")
                                    self.current_streamers.remove(member.id)
                                break        
        else:
            return
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Ignore these errors
        ignored = (commands.CommandNotFound, commands.UserInputError)
        if isinstance(error, ignored):
            return

        if isinstance(error, commands.CommandOnCooldown):
            # If the command is currently on cooldown trip this
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            if int(h) == 0 and int(m) == 0:
                await ctx.send(f" You must wait {int(s)} seconds to use this command!")
            elif int(h) == 0 and int(m) != 0:
                await ctx.send(
                    f" You must wait {int(m)} minutes and {int(s)} seconds to use this command!"
                )
            else:
                await ctx.send(
                    f" You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!"
                )
        elif isinstance(error, commands.CheckFailure):
            # If the command has failed a check, trip this
            await ctx.send("Hey! You lack permission to use this command.")
        # Implement further custom checks for errors here...
        raise error


def setup(bot):
    bot.add_cog(Events(bot))
