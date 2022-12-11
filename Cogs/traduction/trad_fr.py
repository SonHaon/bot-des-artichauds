import asyncio
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 
import deepl

from ..couleurs import couleur 
from ..checks import check


translator = deepl.Translator("b2f44de3-fa00-9598-36ba-effea8104e2b:fx") 

class trad_fr(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot
        self.ctx_menu = app_commands.ContextMenu(
            name="traduire en français",
            callback=self.trad_fr
        )
        self.bot.tree.add_command(self.ctx_menu)

    @app_commands.guilds(900046546656182322)
    async def trad_fr(self,interaction:discord.Interaction,message:discord.Message) -> None:
        content = translator.translate_text(message.content,target_lang="FR")
        await interaction.response.send_message(content=f"{message.content}\n\n{content}",ephemeral=True)