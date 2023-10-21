import asyncio
from datetime import datetime
import discord
from discord.ext import commands,tasks
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

class logs(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 
        self.logs.start()

    @tasks.loop(seconds=15)
    async def logs(self):
        channel = self.bot.get_channel(1015569619739746374)
        await channel.send('test')