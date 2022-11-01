import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..fonction import log

import logging 
logger = logging.getLogger('discord.artichauds') 

class clear(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="clear",description="supprime un nombre donné de message")
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.rename(nb="nombre_de_messages")
    @app_commands.describe(nb="nombre de message à supprimé")
    async def clear(self,interaction:discord.Interaction,nb:int):
        await interaction.response.defer(ephemeral=True)
        await interaction.channel.purge(limit=nb)
        await interaction.edit_original_response(content=f"j'ai supprimé *{nb}* messages")
        logger.info(f"'{interaction.user.display_name}' a supprimé '{nb}' messages dans le channel '{interaction.channel.name}' grace à la commande '/clear'")
        await log(self.bot,interaction.user,f"j'ai supprimé **{nb}** dans {interaction.channel.mention} grace à la commande **/clear**")
