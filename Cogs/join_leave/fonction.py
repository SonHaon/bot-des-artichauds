from PIL import Image,ImageDraw,ImageFont
import numpy as np
import discord
from discord.ext import commands
from io import BytesIO
import os
import asyncio
import json

path=os.path.dirname(os.path.abspath(__file__))+"/info"

class image():
    async def create(self,bot,member,etat):
        return await self.image_bienvenue(bot,member,etat)

    def circular_crowp(self,img):
        img=img.convert("RGB")
        npImage=np.array(img)
        h,w=img.size
        alpha = Image.new('L', img.size,0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0,0,h,w],0,360,fill=255)
        npAlpha=np.array(alpha)
        npImage=np.dstack((npImage,npAlpha))
        return Image.fromarray(npImage)

    async def image_bienvenue(self,bot:commands.Bot,member:discord.Member,etat:str):
        user_pp_url = member.display_avatar.replace(size=256)
        user_pp_url = BytesIO(await user_pp_url.read())
        user_pp = Image.open(user_pp_url)
        user_pp = self.circular_crowp(user_pp) # récupère la pp en tant qu'image et recoupé en rond

        img = Image.open(f"{path}/joinimg.png")
        draw = ImageDraw.Draw(img)

        with open(f"{path}/info.json") as file:
            message:str=json.load(file)[f"message_{etat}"]
        font= ImageFont.truetype(f"{path}/Quicksand_Bold.otf",50)
        draw.multiline_text((650,150),message.format(nom=member.name), (255,255,255), anchor="mm",font=font,align="center") #rajoute le texte d'image

        img.paste(user_pp, box=(22,22),mask=user_pp) #rajoute la pp sur le fond

        img.save(f"{path}/image.png") #save l'image

        channel_image=bot.get_channel(1009137943077724240)
        message = await channel_image.send(file=discord.File(f"{path}/image.png")) # l'envoie dans un channel pour obtenir l'url

        await asyncio.sleep(1)
        os.remove(f"{path}/image.png") #supprime l'image

        return message.attachments[0].url
        
class embed():
    async def create(self,bot,member,etat):
        return await self.embed(bot,member,etat)

    async def embed(self,bot,member:discord.Member,etat):
        with open(f"{path}/message_{etat}.txt") as file:
            description=file.read()

        with open(f"{path}/info.json") as file:
            titre=json.load(file)[f"titre_{etat}"]

        embed = discord.Embed(
                title=titre,
                description=description,
                color=0x0000FF)
        embed.set_image(url= await image().create(bot,member,etat))
        return embed