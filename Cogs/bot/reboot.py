import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 
import os

import logging
logger = logging.getLogger('discord.artichauds')

from ..couleurs import couleur 
from ..checks import check
from ..fonction import date_now

class reboot(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="reboot",description="redémarre le bot (et le raspberry)")
    @check.is_SonHaon()
    async def reboot(self,interaction:discord.Interaction):
        await interaction.response.send_message("le bot va redémarrer",ephemeral=True)
        logger.info(f"'{interaction.user.display_name}' a redémarrer '{self.bot.user.display_name}' depuis le channel '{interaction.channel.name}'")
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai **redémarrer** {self.bot.user.mention} depuis {interaction.channel.mention}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)
        os.system("sudo reboot")
        