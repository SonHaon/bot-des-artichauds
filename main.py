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
import watchdog
from watchdog.observers import Observer  #creating an instance of the watchdog.observers.Observer from watchdogs class.
from watchdog.events import LoggingEventHandler,FileSystemEventHandler  #implementing a subclass of watchdog.events.FileSystemEventHandler which is LoggingEventHandler in our case
from discord.utils import maybe_coroutine


from Cogs.checks import check
from Cogs.fonction import *
from Cogs.couleurs import couleur
from Cogs.components import bouton_sondage,ban_modal, boutons_auto_role
from roles import get_role
from users import get_user
from channels import get_channel

from Cogs_sommaire import *
load_dotenv(".env")
TOKEN = os.getenv("TOKEN")
guild = discord.Object(id=900046546656182322)
translator = deepl.Translator("b2f44de3-fa00-9598-36ba-effea8104e2b:fx") 

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

class MyTranslator(Translator):
    async def translate(
        self,
        string: locale_str,
        locale: Locale,
        context: TranslationContext
        ):
        #print(str(context.location).removeprefix("TranslationContextLocation."), string.extras)
        if locale is Locale.french:
            try:
                return string.extras["fr"]
            except:
                return None
        else:
            try:
                return string.extras["en"]
            except:
                return None
        return None 




class bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents = intents,command_prefix="%µ¨£%£µ%",help_command=None)
        
    async def setup_hook(self):
        # set le traducteur
        await self.tree.set_translator(MyTranslator())
        # commandes normal
        await self.add_cog(ping(bot=self))
        await self.add_cog(quote(bot=self),guild=guild)
        await self.add_cog(sondage(bot=self),guild=guild)
        await self.add_cog(channel_history(bot=self))
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
        await self.add_cog(set_auto_role(bot=self),guild=guild)
        # commandes de help
        await self.add_cog(help(bot=self),guild=guild)
        await self.add_cog(help_id(bot=self),guild=guild)
        # commandes de bot
        await self.add_cog(change_presence(bot=self),guild=guild)
        await self.add_cog(reboot(bot=self))
        await self.add_cog(raspberry_reboot(bot=self),guilds=[guild,discord.Object(id=916617095876337664)])
        # event
        await self.add_cog(timeout(bot=self),guild=guild)
        await self.add_cog(member_leave(bot=self),guild=guild)
        await self.add_cog(member_join(bot=self),guild=guild)
        await self.add_cog(on_message(bot=self),guild=guild)
        await self.add_cog(test_lien(bot=self))
        await self.add_cog(logs(bot=self))
        # commandes de traduction
        await self.add_cog(trad_fr(bot=self),guild=guild)
        await self.add_cog(trad_en(bot=self),guild=guild)
        await self.add_cog(trad_de(bot=self),guild=guild)
        await self.add_cog(trad_sp(bot=self),guild=guild)
        await self.add_cog(langue(bot=self),guild=guild)

        await self.tree.sync(guild=guild)
        await self.tree.sync()


    async def on_ready(self):
        await self.wait_until_ready()
        self.translate=MyTranslator.translate
        self.roles = get_role(guild=self.get_guild(900046546656182322))
        self.member = get_user(bot=self)
        self.channel = get_channel(bot=self)
        self.artichauds = self.get_guild(900046546656182322)
        self.add_view(view=boutons_auto_role(guild=self.artichauds),message_id=1093050764173267016)
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




#def logs_fonction():
#    asyncio.create_task(logs(SonHaon_Bot))
#    logger.info("permier truc marche")

#class EventHandler(FileSystemEventHandler):
#  def __init__(self,bot) -> None:
#      self.bot=bot
#      super().__init__()
#  def dispatch(self,event):
#    logger.info("test")
#    self.bot.loop.create_task(logs(SonHaon_Bot))

#def watchdog_truc(bot):
#    path = r"/Users/noah/Documents/serveur_discord/botarchauds.log"
#    event_handler = EventHandler(bot)
#    observer = Observer()
#    observer.schedule(event_handler, path, recursive=True)  #Scheduling monitoring of a path with the observer instance and event handler. There is 'recursive=True' because only with it enabled, watchdog.observers.Observer can monitor sub-directories
#    observer.start()
#    logger.info("après start")

# caractère invisible : (⁠)

SonHaon_Bot.run(TOKEN)