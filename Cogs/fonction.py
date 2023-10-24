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