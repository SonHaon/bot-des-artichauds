import asyncio
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

import logging
logger = logging.getLogger('discord.artichauds')
from ..couleurs import couleur 
from ..fonction import create_webhook,date_now


status=[discord.Status.online,discord.Status.offline,discord.Status.idle,discord.Status.dnd]
status1=["en ligne","invisible","absent","ne pas déranger"]

class change_presence(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="status",description="change le status du bot")
    @app_commands.choices(statu=[
        app_commands.Choice(name="en ligne",value="0"),
        app_commands.Choice(name="invisible",value="1"),
        app_commands.Choice(name="absent",value="2"),
        app_commands.Choice(name="ne pas déranger",value="3")]
    )
    async def change_presence(self,interaction:discord.Interaction,statu:str):
        statu=int(statu)
        if statu==1:
            await self.bot.change_presence(status=status[statu])
        else:
            await self.bot.change_presence(status=status[statu],activity=discord.Activity(type=discord.ActivityType.watching,name="/help"))
        await interaction.response.send_message(f"le statu du bot est maintenant *{status1[statu]}*",ephemeral=True)
        logger.info(f"'{interaction.user.display_name}' a changé le status de '{self.bot.user.display_name}' en {status1[statu]} depuis le channel '{interaction.channel.name}'")
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai **changé le status** de {self.bot.user.mention} en __**{status1[statu]}**__ depuis {interaction.channel.mention}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)