import asyncio
from platform import platform
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 


from .embed_help import *

class Select_jeux(discord.ui.Select):
    def __init__(self,default=0):
        options=[
            discord.SelectOption(label="commandes",description="affiche le message de help général pour les commandes de jeux",value="0"),
            discord.SelectOption(label="chifoumi",description="affiche le message de help pour le /chifoumi",value="1"),
            discord.SelectOption(label="trouve_le_nombre",description="affiche le message de help pour le /trouve_le_nombre",value="2"),
            discord.SelectOption(label="dé",description="affiche le message de help pour le /dé",value="3")
            ]
        options[default].default=True
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        view:discord.ui.View=self.view
        view.remove_item(self)
        for option in self.options:
            option.default=False
        self.options[int(self.values[0])].default=True
        view.add_item(self)
        value=int(self.values[0])
        await interaction.response.edit_message(embed=embeds_jeux[value],view=view)


class Select_autre(discord.ui.Select):
    def __init__(self,default=0):
        options=[
            discord.SelectOption(label="commandes",description="affiche le message de help général pour les commandes autres",value="0"),
            discord.SelectOption(label="ping",description="affiche le message de help pour le /ping",value="1"),
            discord.SelectOption(label="quote",description="affiche le message de help pour le /quote",value="2")
            ]
        options[default].default=True
        super().__init__(placeholder="Select an option",min_values=1,max_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        view:discord.ui.View=self.view
        view.remove_item(self)
        for option in self.options:
            option.default=False
        self.options[int(self.values[0])].default=True
        view.add_item(self)
        value=int(self.values[0])
        await interaction.response.edit_message(embed=embeds_normal[value],view=view)
        





class Select_categorie(discord.ui.Select):
    def __init__(self, default=0) -> None:
        options=[
            discord.SelectOption(label="jeux",description="affiche le message de help général pour les commandes de jeux",value="0"),
            discord.SelectOption(label="autres",description="affiche le message de help général pour les autres commandes",value="1")
            ]
        if not default==None:
            options[default].default=True
        super().__init__(placeholder="choisi une catégorie",max_values=1,min_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        list_select=[Select_jeux(default=0),Select_autre(default=0)]
        view = View_tout(default_catergory=int(self.values[0]),item=list_select[int(self.values[0])])
        value = int(self.values[0])
        await interaction.response.edit_message(embed=embeds_help[value][0],view=view)

class View_tout(discord.ui.View):
    def __init__(self,default_catergory=0,item=False, *, timeout= 180):
        super().__init__(timeout=timeout)
        self.add_item(Select_categorie(default=default_catergory))
        if item:
            self.add_item(item)




class Select_troll(discord.ui.Select):
    def __init__(self,default=0):
        options=[
            discord.SelectOption(label="commandes",description="affiche le message de help général pour les commandes de troll",value="0"),
            discord.SelectOption(label="say",description="affiche le message de help pour le /say",value="1"),
            discord.SelectOption(label="add_reaction",description="affiche le message de help pour le /add_reaction",value="2")
            ]
        options[default].default=True
        super().__init__(placeholder="Select an option",min_values=1,max_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        view:discord.ui.View=self.view
        view.remove_item(self)
        for option in self.options:
            option.default=False
        self.options[int(self.values[0])].default=True
        view.add_item(self)
        value=int(self.values[0])
        await interaction.response.edit_message(embed=embeds_troll[value],view=view)

class Select_modération(discord.ui.Select):
    def __init__(self,default=0):
        options=[
            discord.SelectOption(label="commandes",description="affiche le message de help général pour les commandes de modération",value="0"),
            discord.SelectOption(label="clear",description="affiche le message de help pour le /clear",value="1")
            ]
        options[default].default=True
        super().__init__(placeholder="Select an option",min_values=1,max_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        view:discord.ui.View=self.view
        view.remove_item(self)
        for option in self.options:
            option.default=False
        self.options[int(self.values[0])].default=True
        view.add_item(self)
        value=int(self.values[0])
        await interaction.response.edit_message(embed=embeds_moderation[value],view=view)
        



class Select_categorie_admin(discord.ui.Select):
    def __init__(self, default=0) -> None:
        options=[
            discord.SelectOption(label="jeux",description="affiche le message de help général pour les commandes de jeux",value="0"),
            discord.SelectOption(label="autres",description="affiche le message de help général pour les autres commandes",value="1"),
            discord.SelectOption(label="modération",description="affiche le message de help général pour les commandes de modération",value="2"),
            discord.SelectOption(label="troll",description="affiche le message de help général pour les commandes de troll",value="3")
            ]
        if not default==None:
            options[default].default=True
        super().__init__(placeholder="choisi une catégorie",max_values=1,min_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        list_select=[Select_jeux(default=0),Select_autre(default=0),Select_modération(default=0),Select_troll(default=0)]
        view = View_tout_admin(default_catergory=int(self.values[0]),item=list_select[int(self.values[0])])
        value = int(self.values[0])
        await interaction.response.edit_message(embed=embeds_help_admin[value][0],view=view)

class View_tout_admin(discord.ui.View):
    def __init__(self,default_catergory=0,item=False, *, timeout= 180):
        super().__init__(timeout=timeout)
        self.add_item(Select_categorie_admin(default=default_catergory))
        if item:
            self.add_item(item)


class select_image(discord.ui.Select):
    def __init__(self,plateforme) -> None:
        self.plateforme =plateforme
        options = [
            discord.SelectOption(label="image 1",description="affiche l'image 1",value="1"),
            discord.SelectOption(label="image 2",description="affiche l'image 2",value="2"),
            discord.SelectOption(label="image 3",description="affiche l'image 3",value="3"),
            discord.SelectOption(label="image 4",description="affiche l'image 4",value="4")
            ]
        super().__init__(placeholder="choisit les images à afficher", min_values=0, max_values=4, options=options)

    async def callback(self,interaction:discord.Interaction):
        view:discord.ui.View=self.view
        embeds=[embeds_id[self.plateforme][0]]
        for value in self.values:
            value=int(value)
            embeds.append(embeds_id[self.plateforme][value])
        view.clear_items()
        for option in self.options:
            option.default=False
        for value in self.values:
            value=int(value)
            self.options[value-1].default=True
        view.add_item(self)
        await interaction.response.edit_message(embeds=embeds,view=view)

class View_id(discord.ui.View):
    def __init__(self,plateforme, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(select_image(plateforme=plateforme))