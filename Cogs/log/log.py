import asyncio
from datetime import datetime
import discord
from discord.ext import commands,tasks
from discord import app_commands
from discord.app_commands import locale_str as _t
from discord.ui import *
import random
import os
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw,ImageOps
import logging
import json

from ..fonction import log,trad
logger = logging.getLogger('discord.artichauds')

path=os.path.dirname(os.path.abspath(__file__))






class logs(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 
        self.logs.start()

    @tasks.loop(seconds=15)
    async def logs(self):
        await self.bot.wait_until_ready()
        channel=self.bot.get_channel(1165260732292661268)

        with open("../botarchauds.log","r") as file:
            lignes=file.readlines()
        lignes.reverse()

        with open(f"{path}/info.json","r") as file:
            dico=json.load(file)
            last_log=dico["last_log"]

        dico["last_log"]=lignes[0]
        

        with open(f"{path}/info.json","w") as file:
            file.write(json.dumps(dico))

        if last_log==lignes[0]:
            return

        envoi=[]
        for ligne in lignes:
            if ligne != last_log:
                envoi.append(ligne)
            else:
                break

        envoi.reverse()
        content="".join(envoi)
        message=await channel.fetch_message(channel.last_message_id)

        if len(message.content)+len(content)>1999 or message.author.id!=self.bot.user.id:
            await channel.send(f'```{content}```')
        else:
            await message.edit(content=f"{message.content[:-3]}{content}```")
        