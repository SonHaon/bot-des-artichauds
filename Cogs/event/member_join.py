import asyncio
from io import BytesIO 
import discord 
from discord.ext import  commands 
from discord.app_commands import locale_str as _t
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
from PIL import Image, ImageDraw,ImageFont
import os
import random 
import logging
logger = logging.getLogger('discord.artichauds') 
from ..fonction import fonction

async def embed(bot,member:discord.Member):
    embed = discord.Embed(
            title="Ho ! Un nouveau jardinier !",
            description=f"""🎉 Amis <@&948895100346437676>, nous accueillons un nouvel Artichaud : {member.display_name} 🎉!

Nous sommes un clan actif, voici les deux seules conditions demandées :
La plus importante : Au moins 100 ressources (os et chairs) pour les coffres de clan chaque semaine. Tout le monde profite des récompenses, il est normal que tout le monde participe. Il n'est nullement obligatoire de faire les runs payants, chacun fait comme il veut. Faire le run gratuit chaque jour suffit amplement pour atteindre cet objectif.
Ensuite, au moins 3500 points d'activité de clan chaque semaine. Là encore, pas la peine de forcer, en jouant normalement et en faisant les dons et aides aux éclosions, ça se fait tout seul.

Comme tu pourras le voir, nous avons beaucoup de canaux pour bien séparer tous les aspects du jeu.
Les informations principales sont souvent en messages épinglés.
Cependant, nous avons des experts du hors-sujet assez compétitifs, donc si tu ne trouves pas de réponse à une question, n'hésite pas à demander.

Tu peux :
nous faire une petite présentation dans <#900048923534688286>
lire le règlement et intégrer les rôles qui peuvent t’intéresser <#900068827595956234> 

Si besoin d’aide pour faire tes 3,5k points de clan, le détail ||de notre prisonnier politique Kaseiya 😏|| épinglé dans <#900384566802530314> pourra peut-être t’aider.

Bonne visite, si tu as des questions n’hésite pas.

Au plaisir de te voir participer a notre ferme ☺️""",
            color=0x0000FF)
    embed.set_image(url= await fonction.image_bienvenue(bot,member,f"Bienvenue {member.name}"))
    return embed

class member_join(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_member_join")
    async def on_member_join(self,member:discord.Member):
        channel = member.guild.get_channel(934114546304553012)
        embeds = await embed(self.bot,member)
        await channel.send(member.mention,embed=embeds)
        await asyncio.sleep(2)
        os.remove("/home/sonhaon/bot-des-artichauds/image_fr.png")