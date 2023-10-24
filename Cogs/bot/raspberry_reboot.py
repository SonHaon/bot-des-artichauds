import asyncio 
import discord 
from discord.ext import  commands 
from discord.app_commands import locale_str as _t
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 
import os

import logging
logger = logging.getLogger('discord.artichauds')

from ..couleurs import couleur 
from ..checks import check
from ..fonction import log

class bouton_validation(discord.ui.View):
    def __init__(self,bot):
        self.bot = bot
        super().__init__(timeout=None)

    @discord.ui.button(
        style=ButtonStyle.green,
        label="Redémarrer",
        emoji="✅",
        custom_id="reboot",
        row=0
    )
    async def reboot(self,interaction:discord.Interaction,button:discord.ui.Button):
        await self.bot.change_presence(status=discord.Status.offline)
        await interaction.response.edit_message(content="le raspberry va redémarrer",view=None)
        logger.info(f"'{interaction.user.display_name}' a redémarrer 'le raspberry' depuis le channel '{interaction.channel.name}'")
        await log(self.bot,interaction.user,f"j'ai **redémarrer** le raspberry depuis {interaction.channel.mention}")
        os.system("sudo reboot")

    @discord.ui.button(
        style=ButtonStyle.red,
        label="Annulé",
        emoji="❌",
        custom_id="annule",
        row=0
    )
    async def not_reboot(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.response.edit_message(content="Le raspberry n'a pas redémarré",view=None)




class raspberry_reboot(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(
        name=_t(
            "raspberry_reboot",
            fr="redémarrage_du_raspberry",
            en="raspberry_restart"
        ),
        description=_t(
            "description",
            fr="redémarre le raspberry, à ne faire qu'en cas d'urgence",
            en="restarts raspberry, only to be used in an emergency"
        )
    )
    @check.is_SonHaon()
    async def raspberry_reboot(self,interaction:discord.Interaction):
        await interaction.response.send_message("Voulez-vous vraiment faire ca ?",view=bouton_validation(self.bot),ephemeral=True)
        