from datetime import datetime
import discord
from PIL import Image,ImageDraw
import numpy as np
from io import BytesIO
from roles import get_role
import aiohttp
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
    > **{len(get_role(ctx.guild).infini.members)}** jardiniers possède le role {get_role(ctx.guild).infini.mention}
    > **{len(get_role(ctx.guild).alors.members)}** jardiniers possède le role {get_role(ctx.guild).alors.mention}"""

async def a_sync(url):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(url) as r:
            if r.status in range(200, 299):
                img = BytesIO(await r.read())
                b = img.getvalue()
                return b

async def create_webhook(channel:discord.TextChannel,user:discord.Member):
    avatar=await a_sync(user.display_avatar.url)
    webhook = await channel.create_webhook(name=user.display_name,avatar=avatar)
    return webhook

async def has_webhook(channel:discord.TextChannel,user:discord.Member):
    webhooks = await channel.webhooks()
    if len(webhooks) == 0:
        webhook = await create_webhook(channel,user)
        return webhook
    else:
        avatar=await a_sync(user.display_avatar.url)
        await webhooks[0].edit(name=user.display_name,avatar=avatar)
        return webhooks[0]

def date_now():
    date = datetime.now()
    return f"[<t:{date.timestamp}:f>] **|**"

