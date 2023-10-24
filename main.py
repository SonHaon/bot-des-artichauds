import asyncio
from pathlib import Path
import discord
from discord.ext import commands
from discord import app_commands, Locale
from discord.ui import *
import random
import os
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw,ImageOps
import logging
import logging.handlers
import deepl
from discord.app_commands import Translator, locale_str, TranslationContext, TranslationContextLocation
import sys
import time
import logging
from discord.utils import maybe_coroutine


from Cogs.checks import check
from Cogs.fonction import fonction
from users import get_user

from Cogs_sommaire import *

load_dotenv("/Users/noah/Documents/serveur_discord/SonHaon-Bot/.env")
TOKEN = os.getenv("TOKEN")


guild = discord.Object(id=916617095876337664)


logger = logging.getLogger('discord.bot')
logger.setLevel(logging.INFO)
dt_fmt = '%d/%m/%Y %H:%M'
formatter = logging.Formatter('[{asctime}] {name}: {message}', dt_fmt, style='{')

logger_command = logging.getLogger("discord.command")
logger_command.setLevel(logging.INFO)





class bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents = intents,command_prefix="%µ¨£%£µ%",help_command=None)
        
    async def setup_hook(self):
        # commandes normal
        await self.add_cog(ping(bot=self))
        await self.add_cog(quote(bot=self),guild=guild)
        # commandes de jeu
        await self.add_cog(de(bot=self),guild=guild)
        await self.add_cog(chifoumi(bot=self),guild=guild)
        await self.add_cog(trouve_le_nombre(bot=self),guild=guild)
        # commandes de troll
        await self.add_cog(say(bot=self),guild=guild)
        await self.add_cog(add_reaction(bot=self),guild=guild)
        await self.add_cog(fake_message(bot=self),guild=guild)
        # commandes de modération
        await self.add_cog(clear(bot=self),guild=guild)
        # commandes de help
        await self.add_cog(help(bot=self),guild=guild)
        await self.add_cog(help_id(bot=self),guild=guild)
        # commandes de bot
        await self.add_cog(change_presence(bot=self),guild=guild)
        # event
        await self.add_cog(member_leave(bot=self),guild=guild)
        await self.add_cog(member_join(bot=self),guild=guild)
        await self.add_cog(on_message(bot=self),guild=guild)

        await self.tree.sync(guild=guild)
        await self.tree.sync()


    async def on_ready(self):
        await self.wait_until_ready()
        self.member = get_user(bot=self)
        self.fonction = fonction

        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="/help"))
        logger.info(f"{self.user.name} est allumé")

SonHaon_Bot = bot()

@SonHaon_Bot.tree.error
async def on_app_command_error(interaction:discord.Interaction,error):
    if isinstance(error,app_commands.BotMissingPermissions):
        try:
            await interaction.response.send_message(content="je n'ai pas les permissions de faire ça",ephemeral=True)
        except:
            await interaction.edit_original_response(content="je n'ai pas les permissions de faire ça")
    elif isinstance(error, app_commands.MissingPermissions or app_commands.MissingRole or app_commands.MissingAnyRole):
        try:
            await interaction.response.send_message(content="vous ne pouvez pas faire ça",ephemeral=True)
        except:
            await interaction.edit_original_response(content="vous ne pouvez pas faire ça")
    elif isinstance(error,app_commands.CheckFailure):
        try:
            await interaction.response.send_message(content="vous ne pouvez pas faire ça",ephemeral=True)
        except:
            await interaction.edit_original_response(content="vous ne pouvez pas faire ça")
    else:
        embed=discord.Embed(title="Une erreur inattendue est survenue",description=f"""```{error}```\ncopie-colle l’erreur et mentionne {SonHaon_Bot.member.SonHaon.mention} avec l’erreur""")
        try:
            await interaction.response.send_message(embed=embed,ephemeral=True)
        except:
            await interaction.edit_original_response(embed=embed)
        raise error

SonHaon_Bot.run(TOKEN)