from datetime import datetime
import discord
from PIL import Image,ImageDraw,ImageFont
import numpy as np
from io import BytesIO

class fonction:
    async def recup_message_by_id(self,ctx:discord.Interaction, id:int) -> discord.Message:
        for channel in ctx.guild.text_channels:
            channel:discord.TextChannel
            async for message in channel.history():
                if message.id == id:
                    return message

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

    def a_role(self,user,role_search):
        roles = user.roles
        for role in roles:
            if role.name == role_search.name:
                return True
        return False


    async def create_webhook(self,channel:discord.TextChannel,user:discord.Member):
        avatar=await user.display_avatar.read()
        webhook = await channel.create_webhook(name=user.display_name,avatar=avatar)
        return webhook

    async def has_webhook(self,channel:discord.TextChannel,user:discord.Member):
        webhooks = await channel.webhooks()
        if len(webhooks) == 0:
            webhook = await self.create_webhook(channel,user)
            return webhook
        else:
            avatar=await user.display_avatar.read()
            await webhooks[0].edit(name=user.display_name,avatar=avatar)
            return webhooks[0]

    def date_now(self):
        return f"<t:{round(datetime.now().timestamp())}:f> **||**"

    async def image_bienvenue(self,bot,member:discord.Member,message:str):
        user_pp_url = member.display_avatar.replace(size=256)
        user_pp_url = BytesIO(await user_pp_url.read())
        user_pp = Image.open(user_pp_url)
        user_pp = self.circular_crowp(user_pp)
        img = Image.open("/Users/noah/Documents/serveur_discord/bot-des-artichauds/joinimg.png")
        draw = ImageDraw.Draw(img)
        font= ImageFont.truetype("/Users/noah/Documents/serveur_discord/bot-des-artichauds/Quicksand_Bold.otf",50)
        draw.multiline_text((650,150),message, (255,255,255), anchor="mm",font=font,align="center")
        img.paste(user_pp, box=(22,22),mask=user_pp)
        img.save("/Users/noah/Documents/serveur_discord/bot-des-artichauds/image_fr.png")
        channel_image=bot.get_channel(1009137943077724240)
        message = await channel_image.send(file=discord.File("/Users/noah/Documents/serveur_discord/bot-des-artichauds/image_fr.png"))
        return message.attachments[0].url
        