import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from ..checks import check
from ..fonction import fonction

class fake_message(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot 

    @app_commands.command(
        name="fake_message",
        description="créer un faux message de la part d'un personne"
    )
    @check.is_SonHaon()
    async def fake_message(self,interaction:discord.Interaction,user:discord.User,message:str):
        webhook:discord.Webhook = fonction.has_webhook(interaction.channel,user)
        await interaction.response.send_message("message envoyé :thumbsup:",ephemeral=True)
        await webhook.send(message,username=user.display_name,avatar_url=user.display_avatar.url)