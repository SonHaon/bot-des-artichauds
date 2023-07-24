import asyncio 
import discord 
from discord.ext import  commands 
from discord.app_commands import locale_str as _t
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 
import logging
import deepl
from requests import get
logger = logging.getLogger('discord.artichauds') 
from ..couleurs import couleur 
from ..fonction import has_webhook,log

translator = deepl.Translator("b2f44de3-fa00-9598-36ba-effea8104e2b:fx") 

class test_lien(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_message")
    async def on_message(self, message:discord.Message):
        if message.guild.id != 916617095876337664:
            await log(self.bot,message.author,f"messag_trouvé")
        if message.channel is discord.DMChannel:
            await log(self.bot,message.author,f"est dm channel")
            reponse=get(message.content)
            if reponse.status_code == 404:
                await message.reply("erreur 404",mention_author=False)
            else:
                await message.reply("Ca marche !!!",mention_author=False)