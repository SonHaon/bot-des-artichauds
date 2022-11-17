import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
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
        await channel.send(f"{member.mention} (`{member.display_name}`) a quitté le serveur")
        logger.info(f"'{member.display_name}' a quitté le serveur")
        await log(self.bot,member,f"{member.mention} a quitté le serveur des artichauds")