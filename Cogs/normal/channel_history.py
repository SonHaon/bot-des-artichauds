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

class channel_history(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name=_t(
            "channel_history",
            fr="historique_channel",
            en="channel_history"
        ),
        description=_t(
            "description",
            fr="envoie un fichier avec l'entièreté de ce qui a été dit",
            en="sends a file with everything that's been said"
        )
    )
    async def channel_history(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=False)
        try:
            file= open("channel_history.txt",'w+')
            async for message in interaction.channel.history():
                file.writelines(f"{message}\n")
            file.close()
            await interaction.edit_original_response(content="voila :)",attachments=[discord.File("/home/sonhaon/bot-des-artichauds/channel_history.txt")])
        except:
            await interaction.edit_original_response(content="ca marche pas")

