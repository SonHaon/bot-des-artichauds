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
        ),
        reply_id=_t(
            "3",
            fr="réponse_id",
            en="reply_id"
        ),
        reply_mention=_t(
            "4",
            fr="mention_réponse",
            en="reply_mention"
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
        ),
        reply_id=_t(
            "description",
            fr="l'id du message auquel le bot doit répondre",
            en="the id of the message to which the bot should reply"
        ),
        reply_mention=_t(
            "description",
            fr="si le message mentionne la personne à laquelle on répond (ne fait rien si le bot ne répond pas à un message)",
            en="if the message mentions the person you're replying to (does nothing if the bot doesn't reply to a message)"
        )
    )
    async def say(self,interaction:discord.Interaction,content:str,channel:discord.TextChannel=None,file:discord.Attachment=None,reply_id:str=None,reply_mention:bool=False):
        await interaction.response.defer(ephemeral=True)
        if channel == None:
            channel:discord.TextChannel = interaction.channel
        if reply_id != None:
            message:discord.Message=await recup_message_by_id(interaction,int(reply_id))
            if message!=None:
                logger.info("message found")
                if message.channel==channel:
                    logger.info("channel check true")
                    await message.reply(content=content,file=file,mention_author=reply_mention)
                    await interaction.edit_original_response(content=f"le message `{content}` à bien été envoyé dans {channel.mention} en réponse au [message]({message.jump_url})")
                    return
                else:
                    await interaction.edit_original_response(content=f"le message n'est pas dans le channel choisi (ou actuel si aucun channel n'est choisi)")
            else:
                await interaction.edit_original_response(content=f"le message n'existe pas ou n'a pas pu être trouvé")

        await interaction.edit_original_response(content=f"le message `{content}` à bien été envoyé dans {channel.mention}")
        await channel.send(content=content,file=file)
        logger.info(f"'{interaction.user.display_name}' a fait envoyé '{content}' à {self.bot.user.display_name} dans le channel '{channel.name}'")
        await log(self.bot,interaction.user,f"j'ai fait envoyé `{content}` à {self.bot.user.mention} dans le channel {interaction.channel.mention}")