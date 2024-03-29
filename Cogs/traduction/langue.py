import asyncio
from datetime import datetime
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import locale_str as _t
from discord.ui import *
import random
import os
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw,ImageOps
import logging

from ..fonction import log
logger = logging.getLogger('discord.artichauds')

class langue(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name=_t(
            "langue",
            fr="langue",
            en="language"
        ),
        description=_t(
            "description",
            fr="affiche toutes les langues disponible",
            en="shows all available languages"
        )
    )
    async def langue(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_response(content=f"Les langues disponible sont:\nFrancais / French (FR)\nAnglais / English (EN)\nEspagnol / Español (SP)\nAllemand / Deutsch (DE)")
