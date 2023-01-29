import asyncio
from pathlib import Path
import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import *
import random
import os
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw,ImageOps
import logging
import logging.handlers

from Cogs.checks import check
from Cogs.fonction import *
from Cogs.couleurs import couleur
from Cogs.components import bouton_sondage,ban_modal, boutons_auto_role
from roles import get_role
from users import get_user
from channels import get_channel

from Cogs_sommaire import *
load_dotenv(os.path.join(os.path.dirname(os.path.realpath("main.py")), 'token/.env'))
TOKEN = os.getenv("token_botarchauds")
guild = discord.Object(id=900046546656182322)


handler = logging.handlers.RotatingFileHandler(
    filename='artichauds.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
logger = logging.getLogger('discord.artichauds')
logger.setLevel(logging.INFO)
dt_fmt = '%d/%m/%Y %H:%M'
formatter = logging.Formatter('[{asctime}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)


class bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents = intents,command_prefix="%µ¨£%£µ%",help_command=None)
        
    async def setup_hook(self):
        # commandes normal
        await self.add_cog(ping(bot=self),guild=guild)
        await self.add_cog(quote(bot=self),guild=guild)
        await self.add_cog(sondage(bot=self),guild=guild)
        # commandes de jeu
        await self.add_cog(de(bot=self),guild=guild)
        await self.add_cog(chifoumi(bot=self),guild=guild)
        await self.add_cog(trouve_le_nombre(bot=self),guild=guild)
        # commandes de troll
        await self.add_cog(say(bot=self),guild=guild)
        await self.add_cog(add_reaction(bot=self),guild=guild)
        await self.add_cog(spam(bot=self),guild=guild)
        await self.add_cog(fake_message(bot=self),guild=guild)
        # commandes de modération
        await self.add_cog(clear(bot=self),guild=guild)
        await self.add_cog(set_auto_role(bot=self),guild=guild)
        # commandes de help
        await self.add_cog(help(bot=self),guild=guild)
        await self.add_cog(help_id(bot=self),guild=guild)
        # commandes de bot
        await self.add_cog(change_presence(bot=self),guild=guild)
        await self.add_cog(reboot(bot=self),guilds=[guild,discord.Object(id=916617095876337664)])
        await self.add_cog(raspberry_reboot(bot=self),guilds=[guild,discord.Object(id=916617095876337664)])
        # event
        await self.add_cog(timeout(bot=self),guild=guild)
        await self.add_cog(member_leave(bot=self),guild=guild)
        await self.add_cog(member_join(bot=self),guild=guild)
        await self.add_cog(on_message(bot=self),guild=guild)
        # commandes de traduction
        await self.add_cog(trad_fr(bot=self),guild=guild)
        await self.add_cog(trad_en(bot=self),guild=guild)
        await self.add_cog(trad_de(bot=self),guild=guild)
        # commandes de minecraft
        await self.add_cog(minecraft_commands(bot=self),guild=discord.Object(id=916617095876337664))

        await self.tree.sync(guild=guild)
        await self.tree.sync(guild=discord.Object(id=916617095876337664))


    async def on_ready(self):
        await self.wait_until_ready()
        self.roles = get_role(guild=self.get_guild(900046546656182322))
        self.member = get_user(bot=self)
        self.channel = get_channel(bot=self)
        self.artichauds = self.get_guild(900046546656182322)
        self.add_view(view=boutons_auto_role(guild=self.artichauds),message_id=1012375814983131178)
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="/help"))
        logger.info(f"{self.user.name} est allumé")
        await log(self,self.user,"j'ai démarrer")

SonHaon_Bot = bot()
tree = SonHaon_Bot.tree

@tree.error
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



# caractère invisible : (⁠)

SonHaon_Bot.run(TOKEN)