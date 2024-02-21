import asyncio 
import discord 
from discord.ext import  commands 
from discord.app_commands import locale_str as _t
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 
import logging
import deepl
logger = logging.getLogger('discord.artichauds') 
from ..couleurs import couleur 
from ..fonction import has_webhook

translator = deepl.Translator("b2f44de3-fa00-9598-36ba-effea8104e2b:fx") 

class on_message_edit(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_message_edit")
    async def on_message_edit(self, before_message,after_message:discord.Message):
        if after_message.content.startswith("EN "):
            content = translator.translate_text(after_message.content[3:],target_lang="EN-US")
            webhook = await has_webhook(after_message.channel,after_message.author)
            await after_message.delete()
            await webhook.send(content=f"*{after_message.content[3:]}*\n\n{content}")
            logger.info(f"{after_message.author.display_name} a traduit un message en anglais dans {after_message.channel.name}")
        if after_message.content.startswith("FR "):
            content = translator.translate_text(after_message.content[3:],target_lang="FR")
            webhook = await has_webhook(after_message.channel,after_message.author)
            await after_message.delete()
            await webhook.send(content=f"*{after_message.content[3:]}*\n\n{content}")
            logger.info(f"{after_message.author.display_name} a traduit un message en francais dans {after_message.channel.name}")
        if after_message.content.startswith("DE "):
            content = translator.translate_text(after_message.content[3:],target_lang="DE")
            webhook = await has_webhook(after_message.channel,after_message.author)
            await after_message.delete()
            await webhook.send(content=f"*{after_message.content[3:]}*\n\n{content}")
            logger.info(f"{after_message.author.display_name} a traduit un message en allemand dans {after_message.channel.name}")
        if after_message.content.startswith("SP ") or after_message.content.startswith("ES "):
            content = translator.translate_text(after_message.content[3:],target_lang="ES")
            webhook = await has_webhook(after_message.channel,after_message.author)
            await after_message.delete()
            await webhook.send(content=f"*{after_message.content[3:]}*\n\n{content}")
            logger.info(f"{after_message.author.display_name} a traduit un message en espagnol dans {after_message.channel.name}")