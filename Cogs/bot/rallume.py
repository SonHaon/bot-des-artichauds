import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

import logging
logger = logging.getLogger('discord.artichauds')

from ..couleurs import couleur 
from ..checks import check
from ..fonction import date_now

class rallume(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="rallume",description="flm")
    @check.is_SonHaon()
    async def rallume(self,interaction:discord.Interaction):
        await interaction.response.send_message("c'est rallumé",ephemeral=True)
        await self.bot.remove_cog("rallume",guild=discord.Object(id=900046546656182322))
        logger.info(f"'{interaction.user.display_name}' a rallumé '{self.bot.user.display_name}' depuis le channel '{interaction.channel.name}'")
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai **rallumé** {self.bot.user.mention} depuis {interaction.channel.mention}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)
        await self.bot.setup_hook()
        await self.bot.tree.sync(guild=discord.Object(id=900046546656182322))