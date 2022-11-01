import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 
import logging
logger = logging.getLogger('discord.artichauds') 
from ..couleurs import couleur 
from ..fonction import date_now

class member_leave(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_member_remove")
    async def member_leave(self,member:discord.Member):
        channel = member.guild.get_channel(1007259536991715468)
        await channel.send(f"{member.mention} a quitté le serveur")
        logger.info(f"'{member.display_name}' a quitté le serveur")
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} {member.mention} a quitté le serveur des artichauds",username=member.display_name,avatar_url=member.display_avatar.url)