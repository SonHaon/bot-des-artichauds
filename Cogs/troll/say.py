import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..checks import check
from ..fonction import date_now

import logging 
logger = logging.getLogger('discord.artichauds') 

class say(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="say",description="permet de faire envoyer un message au bot")
    @check.is_chef()
    @app_commands.rename(content="message",file="fichier")
    @app_commands.describe(content="message à envoyer",file="fichier à envoyer",channel="channel où le message va être envoyé")
    async def say(self,interaction:discord.Interaction,content:str,channel:discord.TextChannel=None,file:discord.Attachment=None):
        await interaction.response.defer(ephemeral=True)
        if channel == None:
            channel:discord.TextChannel = interaction.channel
        await interaction.edit_original_response(content=f"le message `{content}` à bien été envoyé dans {channel.mention}")
        await channel.send(content=content,file=file)
        logger.info(f"'{interaction.user.display_name}' a fait envoyé '{content}' à {self.bot.user.display_name} dans le channel '{channel.name}'")
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai fait envoyé `{content}` à {self.bot.user.mention} dans le channel {interaction.channel.mention}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)