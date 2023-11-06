from datetime import datetime
import discord
from PIL import Image,ImageDraw,ImageFont
import numpy as np
from io import BytesIO
import aiohttp
from roles import get_role
from channels import get_channel
import os

from ..fonction import circular_crowp

path=os.path.dirname(os.path.abspath(__file__))+"/info"


async def image_bienvenue_fr(bot,member:discord.Member):
    user_pp_url = member.display_avatar.replace(size=256)
    user_pp_url = BytesIO(await user_pp_url.read())
    user_pp = Image.open(user_pp_url)
    user_pp = circular_crowp(user_pp)
    img = Image.open(f"{path}/joinimg.png")
    draw = ImageDraw.Draw(img)
    font= ImageFont.truetype(f"{path}/Quicksand_Bold.otf",50)
    draw.multiline_text((650,150),f"Bienvenue {member.display_name}\n\ndans le jardin des\n\n{member.guild}", (255,255,255), anchor="mm",font=font,align="center")
    img.paste(user_pp, box=(22,22),mask=user_pp)
    img.save(f"{path}/image_fr.png")
    channel_image=bot.get_channel(1009137943077724240)
    message = await channel_image.send(file=discord.File(f"{path}/image_fr.png"))
    return message.attachments[0].url
    


async def image_bienvenue_en(bot,member:discord.Member):
    user_pp_url = member.display_avatar.replace(size=256)
    user_pp_url = BytesIO(await user_pp_url.read())
    user_pp = Image.open(user_pp_url)
    user_pp = circular_crowp(user_pp)
    img = Image.open(f"{path}/joinimg.png")
    draw = ImageDraw.Draw(img)
    font= ImageFont.truetype(f"{path}/Quicksand_Bold.otf",50)
    draw.multiline_text((650,150),f"Welcome {member.display_name}\n\nin the garden of\n\n elite artichokes", (255,255,255), anchor="mm",font=font,align="center")
    img.paste(user_pp, box=(22,22),mask=user_pp)
    img.save(f"{path}/image_en.png")
    channel_image=bot.get_channel(1009137943077724240)
    message = await channel_image.send(file=discord.File(f"{path}/image_en.png"))
    return message.attachments[0].url