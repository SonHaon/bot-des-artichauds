import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 
import os

import logging
logger = logging.getLogger('discord.artichauds')

from ..couleurs import couleur 
from ..checks import check
from ..fonction import log

class reboot(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(
        name=_t(
            "reboot",
            fr="redémmarage",
            en="restart"
        ),
        description=_t(
            "description",
            fr="redémarre le bot et le mets a jour",
            en="restart the bot and update it"
        ),
    )
    @check.is_SonHaon()
    async def reboot(self,interaction:discord.Interaction):
        await self.bot.change_presence(status=discord.Status.offline)
        await interaction.response.send_message("le bot va redémarrer",ephemeral=True)
        logger.info(f"'{interaction.user.display_name}' a redémarrer '{self.bot.user.display_name}' depuis le channel '{interaction.channel.name}'")
        await log(self.bot,interaction.user,f"j'ai **redémarrer** {self.bot.user.mention} depuis {interaction.channel.mention}")
        os.system("launchctl load ~/Library/LaunchAgents/restart-botarchauds.plist")
        