import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from ..couleurs import couleur
from ..checks import check
from ..fonction import recup_message_by_id,log

import logging 
logger = logging.getLogger('discord.artichauds') 

class add_reaction(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name=_t(
            "add_réaction",
            fr="ajouter_réaction",
            en="add_reaction"
        ),
        description=_t(
            "description",
            fr="fait ajouter un emoji au bot",
            en="make the bot add an emoji"
        )
    )
    @check.is_chef()
    @app_commands.rename(
        id=_t(
            "name",
            fr="id_message",
            en="message_id"
        )
    )
    @app_commands.describe(
        emoji=_t(
            "description",
            fr="l'émoji à ajouter",
            en="emoji to add"
        ),
        id=_t(
            "description",
            fr="l'id du message auquel la réaction sera ajouter",
            en="id of the message to which the reaction will be added"
        )
    )
    async def add_emoji(self,interaction:discord.Interaction,emoji:str,id:str):
        await interaction.response.defer(ephemeral=True)
        message:discord.Message= await recup_message_by_id(interaction,int(id))
        if message==None:
            await interaction.edit_original_response(content="Le message n'existe pas ou l'id est incorrect")
            logger.info(f"'{interaction.user.display_name}' a voulu faire 'ajouter une reaction' de la part de {self.bot.user.name} dans le channel '{interaction.channel.name}' mais ça n'a pas fonctionné")
            await log(self.bot,interaction.user,f"j'ai voulu faire **ajouter une reaction** de la part de {self.bot.user.mention} dans le channel {interaction.channel.mention} mais ça n'a pas fonctionné")
            return
        await message.add_reaction(emoji)
        await interaction.edit_original_response(content=f"l'émoji {emoji} à bien été ajouté au message :\n{message.jump_url}")
        logger.info(f"'{interaction.user.display_name}' a ajouté une réaction de la part de {self.bot.user.display_name} depuis le channel '{interaction.channel.name}' sur le message {message.jump_url}")
        await log(self.bot,interaction.user,f"j'ai **ajouté la reaction {emoji}** de la part de {self.bot.user.mention} depuis le channel {interaction.channel.mention} sur le message {message.jump_url}")