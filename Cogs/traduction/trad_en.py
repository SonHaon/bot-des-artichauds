import asyncio
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 
import deepl

from ..couleurs import couleur 
from ..checks import check


translator = deepl.Translator("b2f44de3-fa00-9598-36ba-effea8104e2b:fx") 

class trad_en(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot
        self.ctx_menu = app_commands.ContextMenu(
            name="translate to english",
            callback=self.trad_en
        )
        self.bot.tree.add_command(self.ctx_menu)

    @app_commands.guilds(900046546656182322)
    async def trad_en(self,interaction:discord.Interaction,message:discord.Message) -> None:
        content = translator.translate_text(message.content,target_lang="EN-US")
        await interaction.response.send_message(content=content,ephemeral=True)