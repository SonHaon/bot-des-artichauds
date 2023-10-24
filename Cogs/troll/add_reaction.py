import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from ..checks import check
from ..fonction import fonction

class add_reaction(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name="add_réaction",
        description="fait ajouter un emoji au bot"
    )
    @check.is_admin()
    @app_commands.rename(
        id="message_id"
    )
    @app_commands.describe(
        emoji="l'émoji à ajouter",
        id="l'id du message auquel la réaction sera ajouter"
    )
    async def add_emoji(self,interaction:discord.Interaction,emoji:str,id:str):
        await interaction.response.defer(ephemeral=True)
        message:discord.Message = await fonction.recup_message_by_id(interaction,int(id))
        if message==None:
            await interaction.edit_original_response(content="Le message n'existe pas ou l'id est incorrect")
            return
        await message.add_reaction(emoji)
        await interaction.edit_original_response(content=f"l'émoji {emoji} à bien été ajouté au message :\n{message.jump_url}")