import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..checks import check

class spam(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="spam",description="spam quelqu'un")
    @check.is_chef()
    async def spam(self,interaction:discord.Interaction,user:discord.User,message:str,delai:int,nombre_fois:int,delete:bool):
        await interaction.response.send_message("spam lancé",ephemeral=True)
        if delete:
            delete = 0.001
            delai = 1
        else:
            delete = None
        for i in range(nombre_fois):
            await asyncio.sleep(delai)
            await interaction.channel.send(f"{user.mention} {message}",delete_after=delete)