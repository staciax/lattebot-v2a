import discord #, random, sr_api, asyncdagpi, aiogtts
#import os, io, typing, datetime

def profile_converter(name):
  
  names_to_emojis = {
    "staff" : "<:staff:864052110450884609>",
    "partner" : "<:discordpartner:864052529729896458>",
    "hypesquad" : "<:hypesquad:864052223377670155>",
    "bug_hunter" : "<:bughunter:864052207237726218>",
    "hypesquad_bravery" : "<:bravery:864052291544154132>",
    "hypesquad_brilliance" : "<:brillance:864052307087589377>",
    "hypesquad_balance" : "<:balance:864052284707176449>",
    "early_supporter" : "<:supporter:864052229246156811> ",
    "system" : "<:system_badge:864053001237037067>",
    "bug_hunter_level_2" : "<:bug_hunter_level_2:864052216946753556>",
    "verified_bot" : "<:verified_bot1:864170916601790484><:verified_bot2:864170916329816106>",
    "verified_bot_developer" : "<:verified_bot_developer:864053432468897812>",
    "early_verified_bot_developer" : "<:early_verified_bot_developer:864053963169726484>",
    "discord_certified_moderator" : "<:certified_moderator:864054307367682059>",
    "bot" : "<:bots1:864196319702286336><:bots2:864196319630065664>",
    "guildboost" : "<a:boost:864076334497923072><:nitro:864052236103581716>",
    "nitro" : "<:nitro:864052236103581716>",   
  }
  
  return names_to_emojis.get(name)

def emoji_converter(name):
  
  names_to_emojis = {
    "xmark" : "<:xmark:864416758705553418>",
    "check" : "<:check:864461829836505098>",
    "1st" : "<a:blackjump:867350049319026698>",
    "2nd" : "<a:nezukojump:867350058164551681>",
    "3rd" : "<a:brownjump:867350221665861642>",
    "4th" : "<:check:864461829836505098>",
    "blackcrown" : "<a:blackcrown:867335151407333386>",
    "nekocrown" : "<:nekocatroyal:867362857614966784>",
    "moderation" : "<:moderation:867680516987420722>",
    "lutoaraka" : "<:lutoarakablush:867683214298054696>",
    "shidapout" : "<:shidapout:867683219733348363>",
    "ShinoSmirk" : "<:ShinoSmirk:867686091501994004>",
    "hanaji" : "<:hanaji:867688774914015253>",
    "sayuwoah" : "<:sayuwoah:867683372896878602>",
    "ClevelandDeal" : "<:ClevelandDeal:867693328560947200>",
    "Aoba" : "<:Aoba:867693003693883433>",
    "wowanime" : "<:wowanime:867701428998635522>", 
    "winkai" : "<:winkai:867701465983615006>", 
    "Ani1" : "<:Ani1:867705949933666324>",
    "chocolawow" : "<:chocolawow:867704973865254922>",
    "tohka" : "<:tohka:867707490379628564>",
    "whiteheart" : "<a:white_heart1:867855190472523806>",
    "mongodb" : "<:mongo:870397578242568202>", 
    "latteicon" : "<:latteicon:870419352632045568>", 
    "typing" : "<a:typing:870418148602552422>",  
 
  }
  
  return names_to_emojis.get(name)







