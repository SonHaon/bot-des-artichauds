import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..fonction import log
from ..checks import check

import logging 
logger = logging.getLogger('discord.artichauds') 

class clear(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(
        name=_t(
            "clear",
            fr="supprimer",
            en="clear"
        ),
        description=_t(
            "description",
            fr="supprime un nombre donné de message",
            en="deletes a given number of messages"
        )
    )
    @check.is_chef()
    @app_commands.rename(
        nb=_t(
            "nombre_messages",
            fr="nombre_messages",
            en="message_number"
        )
    )
    @app_commands.describe(
        nb=_t(
            "description",
            fr="nombre de message à supprimer",
            en="number of messages to delete"
        )
    )
    async def clear(self,interaction:discord.Interaction,nb:int):
        await interaction.response.defer(ephemeral=True)
        await interaction.channel.purge(limit=nb)
        await interaction.edit_original_response(content=f"j'ai supprimé *{nb}* messages")
        logger.info(f"'{interaction.user.display_name}' a supprimé '{nb}' messages dans le channel '{interaction.channel.name}' grace à la commande '/clear'")
        await log(self.bot,interaction.user,f"j'ai supprimé **{nb}** dans {interaction.channel.mention} grace à la commande **/clear**")
