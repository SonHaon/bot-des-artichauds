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
        if (message.channel.id == 1012624628751007756) and not(message.author.bot):
            url=f"https://bit.ly/{message.content}"
            reponse=get(url)
            if reponse.status_code == 404:
                await message.reply(f"{url}  erreur 404",mention_author=False)
            else:
                await message.reply(f"{url}  Ca marche !!!",mention_author=False)
        if message.channel.id == 1133079615678709892 and not(message.author.bot) and not(message.content.startswith("!")):
            webhook=has_webhook(message.channel,message.author)
            url=f"https://bit.ly/{message.content}"
            reponse=get(url)
            if reponse.status_code == 404:
                await webhook.send(content=f"{url}  erreur 404",)
                await message.delete()
            else:
                await webhook.send(content=f"{url}  Ca marche !!!",mention_author=False)
                await message.delete()