import discord
from discord import app_commands
from roles import get_role

class check:
    def is_SonHaon():
        def predicate(interaction: discord.Interaction) -> bool:
            return interaction.user.id == 707200529738235925
        return app_commands.check(predicate)

    def is_chef():
        def predicate(interaction:discord.Interaction) -> bool:
            role=get_role(interaction.guild)
            if role.chef in interaction.user.roles or interaction.user.id == 707200529738235925:
                return True
            else:
                return False
        return app_commands.check(predicate)