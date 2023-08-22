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

from ..fonction import log,trad
logger = logging.getLogger('discord.artichauds')

class ping(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name=_t(
            "ping",
            fr="ping",
            en="ping"
        ),
        description=_t(
            "description",
            fr="verifie si le bot marche",
            en="check if the bot works"
        )
    )
    async def ping(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.edit_original_response(content=await trad(
            self.bot,
                _t(f"the bot latency is {round(self.bot.latency*1000)}ms",
                fr=f"le ping du bot est de {round(self.bot.latency*1000)}ms",
                en=f"the bot latency is {round(self.bot.latency*1000)}ms"),
            interaction.locale))
        logger.info(f"'{interaction.user.display_name}' à éxecuté la commande '/ping' dans le channel '{interaction.channel.name}'")
        await log(self.bot,interaction.user,f"j'ai fait **/ping** dans {interaction.channel.mention}")
