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
from ..fonction import log

class minecraft_commands(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="minecraft_commands",description="execute une commande dans la console minecraft")
    @check.is_SonHaon()
    async def minecraft_commands(self,interaction:discord.Interaction,commande:str):
        await interaction.response.defer()
        await interaction.edit_original_response(f"la commande `{commande}` à bien été éxecuté\n{os.popen(f'echo "{commande}" > /run/minecraft.stdin').read()}",ephemeral=True)
        logger.info(f"'{interaction.user.display_name}' a éxecuté la commande '{commande}' sur le serveur minecraft depuis le channel '{interaction.channel.name}'")
        
        