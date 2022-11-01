import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..fonction import message_auto_role,log
from ..components import boutons_auto_role

import logging 
logger = logging.getLogger('discord.artichauds') 

class set_auto_role(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @app_commands.command(name="set_auto_role",description="créer le message pour l'auto role")
    async def set_auto_role(self,interaction:discord.Interaction):
        embed = discord.Embed(title = "A vos rôles", description = "cliquez sur le bouton pour ajouter un role\nrecliquez sur le bouton pour retirer le role")
        embed.add_field(name="Role : ",value=message_auto_role(interaction))
        embed.set_footer(text = f"{interaction.guild.name}", icon_url=interaction.guild.icon.url)
        await interaction.channel.send(embed=embed,view=boutons_auto_role(interaction.guild))
        await interaction.response.send_message("l'auto role à bien été créer",ephemeral=True)
        logger.info(f"'{interaction.user.display_name}' a créé un auto-role temporaire dans le channel '{interaction.channel.name}' avec la commande '/set_auto_role'")
        await log(self.bot,interaction.user,f"j'ai créé un auto-role temporaire dans {interaction.channel.mention} avec la commande **/set_auto_role**")