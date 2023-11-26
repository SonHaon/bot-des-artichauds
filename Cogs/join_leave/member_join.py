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
from ..couleurs import couleur 
from ..fonction import log
from .fonction import image_bienvenue_fr,image_bienvenue_en

path=os.path.dirname(os.path.abspath(__file__))+"/info"

async def embed_fr(bot,member:discord.Member):
    embed = discord.Embed(
            title="Ho ! Un nouveau jardinier !",
            description=f"""Ho ! Un nouveau soldat !
🎉 Amis <@&948895100346437676>, nous accueillons un nouvel AdArtichaud : {member.display_name} 🎉!

Nous sommes un clan actif, voici les deux seules conditions demandées :
- La plus importante : Au moins 150 ressources (os et chairs) pour les coffres de clan chaque semaine. Tout le monde profite des récompenses, il est normal que tout le monde participe. Il n'est nullement obligatoire de faire les runs payants, chacun fait comme il veut. Faire le run gratuit chaque jour suffit amplement pour atteindre cet objectif.
- Ensuite, au moins 3000 points d'activité de clan chaque semaine. Là encore, pas la peine de forcer, en jouant normalement et en faisant les dons et aides aux éclosions, ça se fait tout seul.

Comme tu pourras le voir, nous avons beaucoup de canaux pour bien séparer tous les aspects du jeu.
Les informations principales sont souvent en messages épinglés.
Cependant, nous avons des experts du hors-sujet assez compétitifs, donc si tu ne trouves pas de réponse à une question, n'hésite pas à demander.

Tu peux :
- nous faire une petite presentation dans <#900048923534688286>
- lire le règlement et intégrer les rôles qui peuvent t’intéresser dans <#900068827595956234> 

Si besoin d’aide pour faire tes 3k points de clan, le détail ||de notre prisonnier politique Kaseiya 😏|| epinglé dans <#900384566802530314> pourra peut-être t’aider.

Bonne visite, si tu as des questions n’hésite pas.

Au plaisir de te voir participer a notre ferme armée ☺️""",
            color=couleur().bleu)
    embed.set_image(url= await image_bienvenue_fr(bot,member))
    return embed

async def embed_en(bot,member:discord.Member):
    embed = discord.Embed(
            title="Ho ! A new gardener !",
            description=f"""A new soldier!
🎉 Friends <@&948895100346437676>, we welcome a new AdArtichaud: {member.display_name} 🎉!

We're an active clan, so here are the only two requirements:
- The most important: At least 150 resources (bones and flesh) for clan chests every week. Everyone benefits from the rewards, so it's normal for everyone to participate. There's no obligation to do the paid runs - everyone does as they please. Doing the free run every day is more than enough to reach this goal.
- Next, at least 3,000 clan activity points every week. Here again, there's no need to force the issue: by playing normally and making donations and hatching aids, it'll take care of itself.

As you can see, we've got plenty of channels to keep all aspects of the game separate.
The main information is often in pinned messages.
However, we have some pretty competitive off-topic experts, so if you can't find an answer to a question, don't hesitate to ask.

You can:
- give us a little presentation in <#900048923534688286>
- read the rules and integrate the roles that might interest you in <#900068827595956234> 

If you need help making your 3k clan points, the detail ||of our political prisoner Kaseiya 😏|| pinned in <#900384566802530314> might be able to help you.

Enjoy your visit, if you have any questions don't hesitate.

Looking forward to seeing you at our farm ☺️

Translated with www.DeepL.com/Translator (free version)""",
            color=couleur().bleu)
    return embed.set_image(url= await image_bienvenue_en(bot,member))





class bouton_trad(discord.ui.View):
    def __init__(self,bot):
        self.bot = bot
        super().__init__(timeout=None)

    async def interaction_check(self, interaction: discord.Interaction, /) -> bool:
        if interaction.user == interaction.message.mentions[0]:
            return True
        role=self.bot.roles
        if role.chef in interaction.user.roles:
            return True
        return False
    
    @discord.ui.button(
        style=ButtonStyle.blurple,
        label="show english",
        row=0
    )
    async def EN(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = await embed_en(self.bot,interaction.message.mentions[0])
        await interaction.response.edit_message(embeds=[interaction.message.embeds[0],embed],view=None)
        await asyncio.sleep(2)
        os.remove(f"{path}/image_en.png")











class member_join(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_member_join")
    async def timeout(self,member:discord.Member):
        channel = member.guild.get_channel(900046546656182324)
        embed = await embed_fr(self.bot,member)
        if member.id == 382930544385851392:
            await channel.send(f"{member.mention} vient encore réparer <@889450194935099412> qui marche pas")
            return
        elif member.id == 931236217465471066:
            channel = member.guild.get_channel(1007578769722179657)
            embed.description=""
        await channel.send(member.mention+self.bot.roles.jardinier.mention,embed=embed,view=bouton_trad(self.bot))
        await asyncio.sleep(2)
        os.remove(f"{path}/image_fr.png")
        logger.info(f"'{member.display_name}' a rejoind le serveur")
        await log(self.bot,member,f"{member.mention} a rejoind le serveur des artichauds")