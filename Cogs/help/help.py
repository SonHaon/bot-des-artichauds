import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
from discord.app_commands import locale_str as _t
import random

import logging 
logger = logging.getLogger('discord.artichauds') 

from Cogs.fonction import fonction

from .embed_help import embed_default,embed_default_admin
from .select_help import View_tout,View_tout_admin

class help(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot

    @app_commands.command(
        name="help",
        description="affiche le menu d'aide de toutes commandes"
    )
    async def help(self, interaction: discord.Interaction) -> None:
        if fonction.a_role(interaction.user,self.bot.roles.chef):
            await interaction.response.send_message(embed=embed_default_admin,view=View_tout_admin(default_catergory=None))
        else:
            await interaction.response.send_message(embed=embed_default,view=View_tout(default_catergory=None))