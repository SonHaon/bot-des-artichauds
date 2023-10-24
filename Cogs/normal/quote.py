import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.app_commands import locale_str as _t
from discord.ui import * 
import random 

from ..couleurs import couleur
from ..fonction import recup_message_by_id,log

import logging 
logger = logging.getLogger('discord.artichauds') 

async def recup_message_by_id(ctx:discord.Interaction, id:int) -> discord.Message:

    for channel in ctx.guild.text_channels:
        channel:discord.TextChannel
        async for message in channel.history():
            if message.id == id:
                return message

class quote(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name=_t(
            "quote",
            fr="citer",
            en="quote"
        ),
        description=_t(
            "description",
            fr="cite un message grace a son id",
            en="quote a message using its id"
        )
    )
    @app_commands.rename(
        message_id=_t(
            "id_du_message",
            fr="id_message",
            en="message_id"
        )
    )
    @app_commands.describe(
        message_id=_t(
            "description",
            fr="identifiant du message a récupérer",
            en="message identifier to get"
        )
    )
    async def quote(self,interaction:discord.Interaction,message_id:str):
        await interaction.response.defer()
        message:discord.Message = await recup_message_by_id(interaction, int(message_id))
        if message==None:
            await interaction.edit_original_response(content="Le message n'existe pas ou l'id est incorrect")
            logger.info(f"'{interaction.user.display_name}' a voulu créer une 'citation' dans le channel '{interaction.channel.name}' mais ça n'a pas fonctionné")
            await log(self.bot,interaction.user,f"j'ai voulu créer une **citation** dans {interaction.channel.mention} mais ça n'a pas fonctionné")
            return
        embed = discord.Embed(description= message.content, color= couleur.gris)
        embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
        await interaction.edit_original_response(embed=embed)
        logger.info(f"'{interaction.user.display_name}' a créé une 'citation' du message de '{message.author.display_name}' dans le channel '{interaction.channel.name}' {message.jump_url}")
        await log(self.bot,interaction.user,f"j'ai créé une **citation** du message de '{message.author.mention}' dans {interaction.channel.mention}")