import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..fonction import log

import logging 
logger = logging.getLogger('discord.artichauds') 

class de(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(
        name=_t(
            "dé",
            fr="dé",
            en="dice"
        ),
        description=_t(
            "description",
            fr="lance un dé",
            en="roll a dice"
        )
    )
    @app_commands.rename(
        min=_t(
            "min",
            fr="nombre_minimum",
            en="minimum_number"
        ),
        max=_t(
            "max",
            fr="nombre_maximum",
            en="maximum_number"
        )
    )
    @app_commands.describe(
        min=_t(
            "description",
            fr="le plus petit nombre que peux donner le dé",
            en="the smallest number the die can give"
        ),
        max=_t(
            "description",
            fr="le plus grand nombre que peux donner le dé",
            en="the highest number the die can give"
        )
    )
    async def de(self,interaction:discord.Interaction,min:int = 1,max:int = 6):
        await interaction.response.defer()
        await interaction.edit_original_response(content="je lance le dé...")
        num = random.randint(min,max)
        await asyncio.sleep(1)
        await interaction.edit_original_response(content=f"je lance le dé...\n**{num}** :game_die:!")
        logger.info(f"'{interaction.user.display_name}' a lancé un 'dé' dans le channel '{interaction.channel.name}', le résultat est '{num}'")
        await log(self.bot,interaction.user,f"j'ai fait **/dé** dans {interaction.channel.mention}, le résultat est **__{num}__**")

