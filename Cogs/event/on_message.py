import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 
import logging
import deepl
logger = logging.getLogger('discord.artichauds') 
from ..couleurs import couleur 
from ..fonction import has_webhook

translator = deepl.Translator("b2f44de3-fa00-9598-36ba-effea8104e2b:fx") 

class on_message(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_message")
    async def on_message(self, message:discord.Message):
        if message.content.startswith("EN "):
            content = translator.translate_text(message.content[3:],target_lang="EN-US")
            webhook = await has_webhook(message.channel,message.author)
            await message.delete()
            await webhook.send(content=f"*{message.content[3:]}*\n\n{content}")
            logger.info(f"{message.author.display_name} a traduit un message en anglais dans {message.channel.name}")
        if message.content.startswith("FR "):
            content = translator.translate_text(message.content[3:],target_lang="FR")
            webhook = await has_webhook(message.channel,message.author)
            await message.delete()
            await webhook.send(content=f"*{message.content[3:]}*\n\n{content}")
            logger.info(f"{message.author.display_name} a traduit un message en francais dans {message.channel.name}")
