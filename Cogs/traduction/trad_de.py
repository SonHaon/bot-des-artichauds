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

class trad_de(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot
        self.ctx_menu = app_commands.ContextMenu(
            name="ins Deutsche übersetzen",
            callback=self.trad_de
        )
        self.bot.tree.add_command(self.ctx_menu)

    @app_commands.guilds(900046546656182322)
    async def trad_de(self,interaction:discord.Interaction,message:discord.Message) -> None:
        content = translator.translate_text(message.content,target_lang="DE")
        await interaction.response.send_message(content=content,ephemeral=True)