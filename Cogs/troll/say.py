import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..checks import check
from ..fonction import log,recup_message_by_id

import logging 
logger = logging.getLogger('discord.artichauds') 

class say(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name=_t(
            "say",
            fr="say",
            en="say"
        ),
        description=_t(
            "description",
            fr="permet de faire envoyer un message au bot",
            en="send a message to the bot"
        )
    )
    @check.is_chef()
    @app_commands.rename(
        content=_t(
            "1",
            fr="message",
            en="message"
        ),
        file=_t(
            "2",
            fr="fichier",
            en="file"
        )
    )
    @app_commands.describe(
        content=_t(
            "description",
            fr="message à envoyer",
            en="message to send"
        ),
        file=_t(
            "description",
            fr="fichier à envoyer",
            en="file to send"
        ),
        channel=_t(
            "description",
            fr="channel où le message va être envoyé",
            en="channel where message will be sent"
        )
    )
    async def say(self,interaction:discord.Interaction,content:str,channel:discord.TextChannel=None,file:discord.Attachment=None,reply:str=None):
        await interaction.response.defer(ephemeral=True)
        if channel == None:
            channel:discord.TextChannel = interaction.channel
        if reply != None:
            message:discord.Message=recup_message_by_id(interaction,int(reply))
            if message!=None:
                if message.channel==channel:
                    message.reply(content=content,file=file)
                else:
                    await interaction.edit_original_response(content=f"le message n'est pas dans le channel choisi (ou actuel si aucun channel n'est choisi)")
            else:
                await interaction.edit_original_response(content=f"le message n'existe pas ou n'a pas pu être trouvé")

        await interaction.edit_original_response(content=f"le message `{content}` à bien été envoyé dans {channel.mention}")
        await channel.send(content=content,file=file)
        logger.info(f"'{interaction.user.display_name}' a fait envoyé '{content}' à {self.bot.user.display_name} dans le channel '{channel.name}'")
        await log(self.bot,interaction.user,f"j'ai fait envoyé `{content}` à {self.bot.user.mention} dans le channel {interaction.channel.mention}")