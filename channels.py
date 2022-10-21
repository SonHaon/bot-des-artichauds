import discord
from discord.ext import commands

class get_channel:
    def __init__(self,bot:commands.Bot) -> None:
        self.logs:discord.TextChannel = bot.get_channel(1015569619739746374)
        self.general:discord.TextChannel = bot.get_channel(900046546656182324)