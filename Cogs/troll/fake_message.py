import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..fonction import log
from ..checks import check

class fake_message(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot 

    @app_commands.command(name="fake_message",description="créer un faux message de la part d'un personne")
    @check.is_SonHaon()
    async def fake_message(self,interaction:discord.Interaction,user:discord.User,message:str):
        webhook:discord.Webhook = await interaction.channel.create_webhook(name=user.display_name)
        await interaction.response.send_message("message envoyé :thumbsup:",ephemeral=True)
        await webhook.send(message,username=user.display_name,avatar_url=user.display_avatar.url)
        await webhook.delete()

        await log(self.bot,interaction.user,f"j'ai fait envoyé `{message}` de la part de {user.mention} dans {interaction.channel.mention}")