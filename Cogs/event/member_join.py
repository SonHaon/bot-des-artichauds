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
from ..fonction import circular_crowp,log

class bouton_trad(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(
        style=ButtonStyle.blurple,
        label="english",
        custom_id="EN",
        row=0
    )
    async def EN(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.description = f"""🎉 We welcome a new <@&948895100346437676> {interaction.message.mentions[0].name} 🎉!

You can give us a little presentation in <#900048923534688286> 
Read the rules and integrate the roles that may interest you <#900068827595956234> 
If you need help to make your ~~10k~~ 5k clan points, the detail ||of the wonderful kaseiya 😏|| pinned in <#900384566802530314> might be able to help you.

Enjoy your visit, if you have any questions don't hesitate.

Looking forward to see you participate in our farm ☺️"""
        self.children[1].disabled = False
        self.children[0].disabled = True
        await interaction.response.edit_message(embed=embed,view=self)

    @discord.ui.button(
        style=ButtonStyle.blurple,
        label="français",
        custom_id="FR",
        row=0
    )
    async def FR(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.description = f"""🎉  Nous accueillons un nouveau <@&948895100346437676>  {interaction.message.mentions[0].name}  🎉!

Tu peu nous faire une petite presentation dans <#900048923534688286> 
Lire le règlement et intégrer les roles qui peuvent t’intéresser <#900068827595956234> 
Si besoin d’aide pour faire tes ~~10k~~ 5k points de clan, le détail ||du merveilleux kaseiya 😏|| epinglé dans <#900384566802530314> pourra peu être t’aider.

Bonne visite, si tu as des questions n’hésite pas.

Au plaisir de te voir participer a notre ferme ☺️"""
        self.children[1].disabled = True
        self.children[0].disabled = False
        await interaction.response.edit_message(embed=embed,view=self)









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
        user_pp_url = member.display_avatar.replace(size=256)
        user_pp_url = BytesIO(await user_pp_url.read())
        user_pp = Image.open(user_pp_url)
        user_pp = circular_crowp(user_pp)
        img = Image.open("bot-des-artichauds/joinimg.png")
        draw = ImageDraw.Draw(img)
        font=ImageFont.truetype("bot-des-artichauds/Quicksand_Bold.otf",50)
        draw.multiline_text((650,150),f"Bienvenue {member.display_name}\n\ndans le jardin des\n\n{member.guild}", (255,255,255), anchor="mm",font=font,align="center")
        img.paste(user_pp, box=(22,22),mask=user_pp)
        img.save("bot-des-artichauds/image test.png")
        embed = discord.Embed(
            title="Ho ! Un nouveau jardinier !",
            description=f"""🎉  Nous accueillons un nouveau <@&948895100346437676>  {member.name}  🎉!

Tu peu nous faire une petite presentation dans <#900048923534688286> 
Lire le règlement et intégrer les roles qui peuvent t’intéresser <#900068827595956234> 
Si besoin d’aide pour faire tes ~~10k~~ 5k points de clan, le détail ||du merveilleux kaseiya 😏|| epinglé dans <#900384566802530314> pourra peu être t’aider.

Bonne visite, si tu as des questions n’hésite pas.

Au plaisir de te voir participer a notre ferme ☺️""",
            color=couleur().bleu)
        channel_image=self.bot.get_channel(1009137943077724240)
        message = await channel_image.send(file=discord.File("bot-des-artichauds/image test.png"))
        image_url = message.attachments[0].url
        embed.set_image(url=image_url)
        await channel.send(member.mention,embed=embed,view=bouton_trad())
        await asyncio.sleep(2)
        os.remove("bot-des-artichauds/image test.png")
        logger.info(f"'{member.display_name}' a rejoind le serveur")
        await log(self.bot,member,f"{member.mention} a rejoind le serveur des artichauds")