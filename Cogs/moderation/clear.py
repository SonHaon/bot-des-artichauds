import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from ..checks import check

import logging 
logger = logging.getLogger('discord.artichauds') 

class clear(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(
        name="clear",
        description="supprime un nombre donné de message"
    )
    @check.is_admin()
    @app_commands.rename(
        nb="nombre_messages"
    )
    @app_commands.describe(
        nb="nombre de message à supprimer"
    )
    async def clear(self,interaction:discord.Interaction,nb:int):
        await interaction.response.defer(ephemeral=True)
        await interaction.channel.purge(limit=nb)
        await interaction.edit_original_response(content=f"j'ai supprimé *{nb}* messages")
