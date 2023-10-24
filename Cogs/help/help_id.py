import asyncio
from unicodedata import name 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from .embed_help import embeds_id
from .select_help import View_id

class help_id(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(
        name="help_id",
        description="explique comment trouver l'id d'un message",
    )
    @app_commands.choices(plateforme=[app_commands.Choice(name="pc",value="0"),app_commands.Choice(name="iphone",value="1"),app_commands.Choice(name="android",value="2")])
    @app_commands.describe(plateforme=_t("description",fr="plateforme que vous utilisez",en="platform you use"))
    async def help_id(self,interaction:discord.Interaction,plateforme:str):
        await interaction.response.send_message(embeds=[embeds_id[int(plateforme)][0]],view=View_id(int(plateforme)))