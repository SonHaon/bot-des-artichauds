import asyncio
from io import BytesIO 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
from PIL import Image, ImageDraw,ImageFont
import os
import random 
import logging
logger = logging.getLogger('discord.artichauds') 
from ..couleurs import couleur 
from ..fonction import circular_crowp,log,image_bienvenue_fr,image_bienvenue_en

async def embed_fr(bot,member:discord.Member):
    embed = discord.Embed(
            title="Ho ! Un nouveau jardinier !",
            description=f"""🎉  Nous accueillons un nouveau <@&948895100346437676>  {member.name}  🎉!

Tu peu nous faire une petite presentation dans <#900048923534688286> 
Lire le règlement et intégrer les roles qui peuvent t’intéresser <#900068827595956234> 
Si besoin d’aide pour faire tes ~~10k~~ 5k points de clan, le détail ||du merveilleux kaseiya 😏|| epinglé dans <#900384566802530314> pourra peu être t’aider.

Bonne visite, si tu as des questions n’hésite pas.

Au plaisir de te voir participer a notre ferme ☺️""",
            color=couleur().bleu)
    embed.set_image(url= await image_bienvenue_fr(bot,member))
    return embed

async def embed_en(bot,member:discord.Member):
    embed = discord.Embed(
            title="Ho ! A new gardener !",
            description=f"""🎉 We welcome a new <@&948895100346437676> {member.name} 🎉!

You can give us a little presentation in <#900048923534688286> 
Read the rules and integrate the roles that may interest you <#900068827595956234> 
If you need help to make your ~~10k~~ 5k clan points, the detail ||of the wonderful kaseiya 😏|| pinned in <#900384566802530314> might be able to help you.

Enjoy your visit, if you have any questions don't hesitate.

Looking forward to see you participate in our farm ☺️""",
            color=couleur().bleu)
    return embed.set_image(url= await image_bienvenue_en(bot,member))





class bouton_trad(discord.ui.View):
    def __init__(self,bot):
        self.bot = bot
        super().__init__(timeout=None)

    def interaction_check(self, interaction: discord.Interaction, /) -> bool:
        if interaction.user == interaction.message.mentions[0]:
            return True
        role=self.bot.role
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
        os.remove("bot-des-artichauds/image_en.png")











class member_join(commands.Cog): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 

    @commands.Cog.listener(name="on_member_join")
    async def timeout(self,member:discord.Member):
        channel = member.guild.get_channel(900046546656182324)
        if member.id == 382930544385851392:
            await channel.send(f"{member.mention} vient encore réparer <@889450194935099412> qui marche pas")
            return
        elif member.id == 931236217465471066:
            channel = member.guild.get_channel(1007578769722179657)
        image_url = await image_bienvenue_fr(self.bot,member)
        embed = await embed_fr(self.bot,member)
        await channel.send(member.mention,embed=embed,view=bouton_trad(self.bot))
        await asyncio.sleep(2)
        os.remove("bot-des-artichauds/image_fr.png")
        logger.info(f"'{member.display_name}' a rejoind le serveur")
        await log(self.bot,member,f"{member.mention} a rejoind le serveur des artichauds")