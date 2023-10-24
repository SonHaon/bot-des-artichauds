import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 


class de(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(
        name="dé",
        description="lance un dé"
    )
    @app_commands.rename(
        min="nombre_minimum",
        max="nombre_maximum"
    )
    @app_commands.describe(
        min="le plus petit nombre que peux donner le dé",
        max="le plus grand nombre que peux donner le dé",
    )
    async def de(self,interaction:discord.Interaction,min:int = 1,max:int = 6):
        await interaction.response.defer()
        await interaction.edit_original_response(content="je lance le dé...")
        num = random.randint(min,max)
        await asyncio.sleep(1)
        await interaction.edit_original_response(content=f"je lance le dé...\n**{num}** :game_die:!")

