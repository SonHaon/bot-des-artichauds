import discord
from discord import app_commands

class check:
    def is_SonHaon():
        def predicate(interaction: discord.Interaction) -> bool:
            return interaction.user.id == 707200529738235925
        return app_commands.check(predicate)

    def is_admin():
        def predicate(interaction:discord.Interaction) -> bool:
            if interaction.user.guild_permissions.administrator==True or interaction.user.id == 707200529738235925:
                return True
            else:
                return False
        return app_commands.check(predicate)