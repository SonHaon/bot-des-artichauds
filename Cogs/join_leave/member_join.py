import asyncio
from io import BytesIO 
import discord 
from discord.ext import  commands 
from discord.app_commands import locale_str as _t
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
from PIL import Image, ImageDraw,ImageFont
import os
import json

from .fonction import embed
path=os.path.dirname(os.path.abspath(__file__))+"/info"


class member_join(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_member_join")
    async def on_member_join(self,member:discord.Member):
        with open(f"{path}/info.json") as file:
            channel_id=json.load(file)["channel_arrivee"]
        channel = member.guild.get_channel(channel_id)
        embeds = await embed().create(self.bot,member,"arrivee")
        await channel.send(member.mention,embed=embeds)