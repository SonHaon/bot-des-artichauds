from datetime import datetime
import discord
from PIL import Image,ImageDraw,ImageFont
import numpy as np
from io import BytesIO
import aiohttp
from roles import get_role
from channels import get_channel
async def recup_message_by_id(ctx:discord.Interaction, id:int) -> discord.Message:
    for channel in ctx.guild.text_channels:
        channel:discord.TextChannel
        async for message in channel.history():
            if message.id == id:
                return message

def circular_crowp(img):
    img=img.convert("RGB")
    npImage=np.array(img)
    h,w=img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    return Image.fromarray(npImage)

def a_role(user,role_search):
    roles = user.roles
    for role in roles:
        if role.name == role_search.name:
            return True
    return False

def message_auto_role(ctx:discord.Interaction):
    return f"""> **{len(get_role(ctx.guild).duo.members)}** jardiniers possède le role {get_role(ctx.guild).duo.mention}
    > **{len(get_role(ctx.guild).duel.members)}** jardiniers possède le role {get_role(ctx.guild).duel.mention}
    > **{len(get_role(ctx.guild).ios.members)}** jardiniers possède le role {get_role(ctx.guild).ios.mention}
    > **{len(get_role(ctx.guild).android.members)}** jardiniers possède le role {get_role(ctx.guild).android.mention}
    > **{len(get_role(ctx.guild).alors.members)}** jardiniers possède le role {get_role(ctx.guild).alors.mention}"""

# async def a_sync(url):
#     async with aiohttp.ClientSession() as ses:
#         async with ses.get(url) as r:
#             if r.status in range(200, 299):
#                 img = BytesIO(await r.read())
#                 b = img.getvalue()
#                 return b

async def create_webhook(channel:discord.TextChannel,user:discord.Member):
    avatar=await user.display_avatar.read()
    webhook = await channel.create_webhook(name=user.display_name,avatar=avatar)
    return webhook

async def has_webhook(channel:discord.TextChannel,user:discord.Member):
    webhooks = await channel.webhooks()
    if len(webhooks) == 0:
        webhook = await create_webhook(channel,user)
        return webhook
    else:
        avatar=await user.display_avatar.read()
        await webhooks[0].edit(name=user.display_name,avatar=avatar)
        return webhooks[0]

def date_now():
    return f"<t:{round(datetime.now().timestamp())}:f> **||**"

async def log(bot,user:discord.User,message:str):
    webhook = await bot.channel.logs.webhooks()
    webhook = webhook[0]
    await webhook.send(f"{date_now()} {message}",username=user.display_name,avatar_url=user.display_avatar.url)


async def image_bienvenue_fr(bot,member:discord.Member):
    user_pp_url = member.display_avatar.replace(size=256)
    user_pp_url = BytesIO(await user_pp_url.read())
    user_pp = Image.open(user_pp_url)
    user_pp = circular_crowp(user_pp)
    img = Image.open("/home/sonhaon/bot-des-artichauds/joinimg.png")
    draw = ImageDraw.Draw(img)
    font= ImageFont.truetype("/home/sonhaon/bot-des-artichauds/Quicksand_Bold.otf",50)
    draw.multiline_text((650,150),f"Bienvenue {member.display_name}\n\ndans le jardin des\n\n{member.guild}", (255,255,255), anchor="mm",font=font,align="center")
    img.paste(user_pp, box=(22,22),mask=user_pp)
    img.save("/home/sonhaon/bot-des-artichauds/image_fr.png")
    channel_image=bot.get_channel(1009137943077724240)
    message = await channel_image.send(file=discord.File("/home/sonhaon/bot-des-artichauds/image_fr.png"))
    return message.attachments[0].url
    


async def image_bienvenue_en(bot,member:discord.Member):
    user_pp_url = member.display_avatar.replace(size=256)
    user_pp_url = BytesIO(await user_pp_url.read())
    user_pp = Image.open(user_pp_url)
    user_pp = circular_crowp(user_pp)
    img = Image.open("/home/sonhaon/bot-des-artichauds/joinimg.png")
    draw = ImageDraw.Draw(img)
    font= ImageFont.truetype("/home/sonhaon/bot-des-artichauds/Quicksand_Bold.otf",50)
    draw.multiline_text((650,150),f"Welcome {member.display_name}\n\nin the garden of\n\n elite artichokes", (255,255,255), anchor="mm",font=font,align="center")
    img.paste(user_pp, box=(22,22),mask=user_pp)
    img.save("/home/sonhaon/bot-des-artichauds/image_en.png")
    channel_image=bot.get_channel(1009137943077724240)
    message = await channel_image.send(file=discord.File("/home/sonhaon/bot-des-artichauds/image_en.png"))
    return message.attachments[0].url