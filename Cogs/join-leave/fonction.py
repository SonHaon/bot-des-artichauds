from PIL import Image,ImageDraw,ImageFont
import numpy as np
import discord
from discord.ext import commands
from io import BytesIO
from os import path,remove
import asyncio
import json


class image:
    async def __init__(self,bot,member,etat) -> None:
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
        path=path.dirname(path.abspath(__file__)) #chemin d'accès du dossier

        user_pp_url = member.display_avatar.replace(size=256)
        user_pp_url = BytesIO(await user_pp_url.read())
        user_pp = Image.open(user_pp_url)
        user_pp = self.circular_crowp(user_pp) # récupère la pp en tant qu'image et recoupé en rond

        img = Image.open(f"{path}/joinimg.png")
        draw = ImageDraw.Draw(img)

        with open("info.json") as file:
            message=json.load(file)[f"message_{etat}"]
        font= ImageFont.truetype(f"{path}/Quicksand_Bold.otf",50)
        draw.multiline_text((650,150),message, (255,255,255), anchor="mm",font=font,align="center") #rajoute le texte d'image

        img.paste(user_pp, box=(22,22),mask=user_pp) #rajoute la pp sur le fond

        img.save(f"{path}/image.png") #save l'image

        channel_image=bot.get_channel(1009137943077724240)
        message = await channel_image.send(file=discord.File(f"{path}/image.png")) # l'envoie dans un channel pour obtenir l'url

        await asyncio.sleep(1)
        remove(f"{path}/image.png") #supprime l'image

        return message.attachments[0].url
        
class embed:
    async def __init__(self,bot,member,etat) -> None:
        return await embed(bot,member,etat)

    async def embed(bot,member:discord.Member,etat):
        with open(f"message_{etat}.txt") as file:
            description=file.read()

        with open("info.json") as file:
            titre=json.load(file)[f"titre_{etat}"]

        embed = discord.Embed(
                title=titre,
                description=description,
                color=0x0000FF)
        embed.set_image(url= await image(bot,member,etat))
        return embed