import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from ..fonction import fonction

class quote(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name="quote",
        description="cite un message grace a son id"
    )
    @app_commands.rename(
        message_id="message_id"
    )
    @app_commands.describe(
        message_id="identifiant du message a récupérer"
    )
    async def quote(self,interaction:discord.Interaction,message_id:str):
        await interaction.response.defer()
        message:discord.Message = await fonction.recup_message_by_id(interaction, int(message_id))
        if message==None:
            await interaction.edit_original_response(content="Le message n'existe pas ou l'id est incorrect")
            return
        embed = discord.Embed(description= message.content, color=0x2f3136)
        embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
        await interaction.edit_original_response(embed=embed)