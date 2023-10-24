import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import json
import os

from .fonction import embed
path=os.path.dirname(os.path.abspath(__file__))

class member_leave(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_member_remove")
    async def member_leave(self,member:discord.Member):
        with open(f"{path}/info.json") as file:
            channel_id=json.load(file)["channel_depart"]
        channel = member.guild.get_channel(channel_id)
        embeds = await embed().create(self.bot,member,"depart")
        await channel.send(member.mention,embed=embeds)