import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 


from ..checks import check

class say(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name="say",
        description="permet de faire envoyer un message au bot"
    )
    @check.is_admin()
    @app_commands.rename(
        content="message",
        file="fichier"
    )
    @app_commands.describe(
        content="message à envoyer",
        file="fichier à envoyer",
        channel="channel où le message va être envoyé"
    )
    async def say(self,interaction:discord.Interaction,content:str,channel:discord.TextChannel=None,file:discord.Attachment=None):
        await interaction.response.defer(ephemeral=True)
        if channel == None:
            channel:discord.TextChannel = interaction.channel
        await interaction.edit_original_response(content=f"le message `{content}` à bien été envoyé dans {channel.mention}")
        await channel.send(content=content,file=file)