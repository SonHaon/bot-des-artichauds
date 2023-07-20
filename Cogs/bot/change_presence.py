import asyncio
import discord 
from discord.ext import  commands 
from discord.app_commands import locale_str as _t
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

import logging
logger = logging.getLogger('discord.artichauds')
from ..couleurs import couleur 
from ..fonction import log


statu=[discord.Status.online,discord.Status.offline,discord.Status.idle,discord.Status.dnd]
status1=["en ligne","invisible","absent","ne pas déranger"]

class change_presence(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(
        name=_t(
            "change_presence",
            fr="status",
            en="status"
        ),
        description=_t(
            "description",
            fr="change le status du bot",
            en="change bot status"
        )
    )
    @app_commands.choices(status=[
        app_commands.Choice(name=_t("choice",fr="en ligne",en="online"),value="0"),
        app_commands.Choice(name=_t("choice",fr="invisible",en="invisible"),value="1"),
        app_commands.Choice(name=_t("choice",fr="absent",en="absent"),value="2"),
        app_commands.Choice(name=_t("choice",fr="ne pas déranger",en="do not disturb"),value="3")]
    )
    async def change_presence(self,interaction:discord.Interaction,status:str):
        status=int(status)
        if status==1:
            await self.bot.change_presence(status=statu[status])
        else:
            await self.bot.change_presence(status=statu[status],activity=discord.Activity(type=discord.ActivityType.watching,name="/help"))
        await interaction.response.send_message(f"le statu du bot est maintenant *{status1[statu]}*",ephemeral=True)
        logger.info(f"'{interaction.user.display_name}' a changé le status de '{self.bot.user.display_name}' en {status1[statu]} depuis le channel '{interaction.channel.name}'")
        await log(self.bot,interaction.user,f"j'ai **changé le status** de {self.bot.user.mention} en __**{status1[statu]}**__ depuis {interaction.channel.mention}")