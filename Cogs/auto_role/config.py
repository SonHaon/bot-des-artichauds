import asyncio
from datetime import datetime,timedelta
from typing import Any, Coroutine, List, Optional
import discord
from discord.ext import commands
from discord import ChannelType, app_commands,ButtonStyle,TextStyle,Interaction
from discord.app_commands import locale_str as _t
from discord.interactions import Interaction
from discord.ui import *
from discord.ui.item import Item
import os
import json

from .component import message_autorole_modal
from .fonction import infos,infos_save



class auto_role(commands.GroupCog,name="auto-role"):
    def __init__(self,bot) -> None:
        self.bot=bot
        super().__init__()
    
    roles_group=app_commands.Group(name="roles",description="modifie les roles de l'auto-role")
    

    @roles_group.command(
        name="ajouter",
        description="ajoute un role à l'auto-role"
    )
    async def add(self,interaction:discord.Interaction,role:discord.Role,nom:str,emoji:str):
        info=infos()
        roles=info["roles"]
        for arole in roles:
            if role.id == arole["id"]:
                await interaction.response.send_message("ce role est fait déjà parti de l'auto-role",ephemeral=True)
                return
        roles.append({"id":role.id,"name":nom,"emoji":emoji})
        info["roles"]=roles
        infos_save(info)
        await interaction.response.send_message(f"Le role <@&{role.id}> a été ajouté à l'auto-role, cliquer sur un des boutons pour le faire apparaitre",ephemeral=True)


    async def remove_autocomplete(self,interaction:Interaction,current:str):
        info=infos()
        roles=info["roles"]
        roles2=[]
        for role in roles:
            role2=interaction.guild.get_role(role["id"])
            if current.lower() in role2.name.lower():
                roles2.append(app_commands.Choice(name=role2.name,value=str(role["id"])))
        return roles2
    @roles_group.command(
        name="retirer",
        description="retire un role à l'auto-role"
    )
    @app_commands.autocomplete(role_id=remove_autocomplete)
    @app_commands.rename(role_id="role")
    async def remove(self,interaction:discord.Interaction,role_id:str):
        info=infos()
        roles:list=info["roles"]
        for arole in roles:
            try:
                if int(role_id) == arole["id"]:
                    roles.remove(arole)
                    info["roles"]=roles
                    infos_save(info)
                    await interaction.response.send_message(f"Le role <@&{arole['id']}> été retiré à l'auto-role, cliqueé sur un des boutons pour le faire disparaitre",ephemeral=True)
                    return
            except:
                break

        await interaction.response.send_message("ce role ne fait pas parti de l'auto-role",ephemeral=True)
        return


    async def edit_autocomplete(self,interaction:Interaction,current:str):
        info=infos()
        roles=info["roles"]
        roles2=[]
        for role in roles:
            role2=interaction.guild.get_role(role["id"])
            if current.lower() in role2.name.lower():
                roles2.append(app_commands.Choice(name=role2.name,value=str(role["id"])))
        return roles2
    @roles_group.command(
        name="modifier",
        description="modifie un role de l'auto-role"
    )
    @app_commands.autocomplete(role_id=edit_autocomplete)
    @app_commands.rename(role_id="role")
    async def edit(self,interaction:discord.Interaction,role_id:str,nom:str=None,emoji:str=None):
        info=infos()
        roles:list=info["roles"]
        for arole in roles:
            try:
                if int(role_id) == arole["id"]:
                    if nom!=None: arole["name"]=nom
                    if emoji !=None: arole["emoji"]=emoji
                    info["roles"]=roles
                    infos_save(info)
                    await interaction.response.send_message(f"Le role <@&{arole['id']}>a été modifié, cliquer sur un des boutons pour faire apparaitre les modifications",ephemeral=True)
                    return
            except:
                break

        await interaction.response.send_message("ce role ne fait pas parti de l'auto-role",ephemeral=True)
        return


    @app_commands.command(
        name="create",
        description="créer un message pour l'auto-role"
    )
    async def create(self,interaction:discord.Interaction):
        await interaction.response.send_modal(message_autorole_modal(self.bot))
