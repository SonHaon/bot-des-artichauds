import asyncio
from datetime import datetime
import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *
import random
import os
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw,ImageOps
import logging

from ..fonction import log
logger = logging.getLogger('discord.artichauds')

class ping(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name=app_commands.locale_str("ping"),description=app_commands.locale_str("verifie si le bot marche"))
    async def ping(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_response(content=f"le ping du bot est de {round(self.bot.latency*1000)}ms")
        logger.info(f"'{interaction.user.display_name}' à éxecuté la commande '/ping' dans le channel '{interaction.channel.name}'")
        await log(self.bot,interaction.user,f"j'ai fait **/ping** dans {interaction.channel.mention}")
