import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..checks import check
from ..fonction import date_now
from .rallume import rallume

import logging
logger = logging.getLogger('discord.artichauds')
guild = discord.Object(id=900046546656182322)

class eteindre(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="éteindre",description="flm")
    @check.is_SonHaon()
    async def eteindre(self,interaction:discord.Interaction):
        await interaction.response.send_message("le bot est éteind",ephemeral=True)
        await self.bot.remove_cog("ping",guild=guild)
        await self.bot.remove_cog("quote",guild=guild)
        # commandes de jeu
        await self.bot.remove_cog("de",guild=guild)
        await self.bot.remove_cog("chifoumi",guild=guild)
        await self.bot.remove_cog("trouve_le_nombre",guild=guild)
        # commandes de troll
        await self.bot.remove_cog("say",guild=guild)
        await self.bot.remove_cog("add_reaction",guild=guild)
        # commandes de modération
        await self.bot.remove_cog("clear",guild=guild)
        await self.bot.remove_cog("set_auto_role",guild=guild)
        # commandes de help
        await self.bot.remove_cog("help",guild=guild)
        await self.bot.remove_cog("help_admin",guild=guild)
        await self.bot.remove_cog("help_id",guild=guild)
        # commande de bot
        await self.bot.remove_cog("eteindre",guild=guild)
        await self.bot.add_cog(rallume(self.bot),guild=guild)
        await self.bot.tree.sync(guild=guild)
        print("|------|\n|eteind|\n|------|")
        logger.info(f"'{interaction.user.display_name}' a éteint '{self.bot.user.display_name}' depuis le channel '{interaction.channel.name}'")
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai **éteint** {self.bot.user.mention} depuis {interaction.channel.mention}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)