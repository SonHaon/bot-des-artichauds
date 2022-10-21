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

class timeout(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_member_update")
    async def timeout(self,member_before:discord.Member,member_after:discord.Member):
        if member_after.is_timed_out():
            if member_after.id == self.bot.member.Mixame.id:
                await member_after.timeout(None)
                logger.info(f"'Mixame' a été unmute")
                webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
                webhook = webhook[0]
                await webhook.send(f"{date_now()} j'ai unmute {member_after.mention}",username=self.bot.user.display_name,avatar_url=self.bot.user.display_avatar.url)