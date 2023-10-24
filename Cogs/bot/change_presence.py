import asyncio
import discord 
from discord.ext import  commands 
from discord.app_commands import locale_str as _t
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 



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
        app_commands.Choice(name=_t("1",fr="en ligne",en="online"),value="0"),
        app_commands.Choice(name=_t("2",fr="invisible",en="invisible"),value="1"),
        app_commands.Choice(name=_t("3",fr="absent",en="absent"),value="2"),
        app_commands.Choice(name=_t("4",fr="ne pas déranger",en="do not disturb"),value="3")]
    )
    async def change_presence(self,interaction:discord.Interaction,status:str):
        status=int(status)
        if status==1:
            await self.bot.change_presence(status=statu[status])
        else:
            await self.bot.change_presence(status=statu[status],activity=discord.Activity(type=discord.ActivityType.watching,name="/help"))
        await interaction.response.send_message(f"le statu du bot est maintenant *{status1[statu]}*",ephemeral=True)