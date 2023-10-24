import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 
import logging
logger = logging.getLogger('discord.artichauds') 
from ..couleurs import couleur 
from ..fonction import log

class member_leave(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_member_remove")
    async def member_leave(self,member:discord.Member):
        channel = member.guild.get_channel(1007259536991715468)
        if member.id == 931236217465471066:
            channel = member.guild.get_channel(1007578769722179657)
        await channel.send(f"{member.mention} (`{member.display_name}`) a quitté le serveur")
        logger.info(f"'{member.display_name}' a quitté le serveur")
        await log(self.bot,member,f"{member.mention} a quitté le serveur des artichauds")