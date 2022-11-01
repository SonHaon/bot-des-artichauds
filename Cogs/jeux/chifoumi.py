import asyncio
import discord
from discord.ext import commands
from discord import app_commands,ButtonStyle
from discord.ui import *
import random

from ..couleurs import couleur
from ..fonction import log

import logging 
logger = logging.getLogger('discord.artichauds') 

class bouton_duo(discord.ui.View):
        def __init__(self,ctx:discord.Interaction,adversaire:discord.User, *, timeout=None):
            self.ctx = ctx
            self.adversaire = adversaire
            self.symbole_adversaire = None
            self.symbole_user = None
            super().__init__(timeout=timeout)

        @discord.ui.button(style=ButtonStyle.gray,emoji="🪨",row=1,label="")
        async def pierre_user(self,interaction:discord.Interaction,button:discord.ui.Button):
            if interaction.user == self.ctx.user:
                self.symbole_user = str(button.emoji)
                chil = self.children
                for child in chil:
                    if child.row==1:
                        child.disabled=True
                    if child.row ==0:
                        child.style=ButtonStyle.green
                        child.label=f"{child.label[:-13]} à joué"
                await interaction.message.edit(view=self)
                await interaction.response.send_message("votre reponse à été enregistré",ephemeral=True)
                while self.symbole_adversaire == None:
                    await asyncio.sleep(1)
                await asyncio.sleep(5)
                button.style=ButtonStyle.blurple
                for child in self.children:
                    if child.row==1:
                        self.remove_item(child)
                button.row=0
                self.add_item(button)
                await interaction.message.edit(view=self)
            else:
                await interaction.response.send_message("vous ne pouvez pas faire ca",ephemeral=True)

        @discord.ui.button(style=ButtonStyle.gray,emoji="🪨",row=3,label="")
        async def pierre_adversaire(self,interaction:discord.Interaction,button:discord.ui.Button):
            if interaction.user == self.adversaire:
                self.symbole_adversaire = str(button.emoji)
                chil = self.children
                for child in chil:
                    if child.row==3:
                        child.disabled=True
                    if child.row ==2:
                        child.style=ButtonStyle.green
                        child.label=f"{child.label[:-13]} à joué"
                await interaction.message.edit(view=self)
                await interaction.response.send_message("votre reponse à été enregistré",ephemeral=True)
                while self.symbole_user == None:
                    await asyncio.sleep(1)
                await asyncio.sleep(5)
                button.style=ButtonStyle.blurple
                for child in self.children:
                    if child.row==3:
                        self.remove_item(child)
                button.row=2
                self.add_item(button)
                await interaction.message.edit(view=self)
            else:
                await interaction.response.send_message("vous ne pouvez pas faire ca",ephemeral=True)

        @discord.ui.button(style=ButtonStyle.gray,emoji="📄",row=1,label="")
        async def feuille_user(self,interaction:discord.Interaction,button:discord.ui.Button):
            if interaction.user == self.ctx.user:
                self.symbole_user = str(button.emoji)
                chil = self.children
                for child in chil:
                    if child.row==1:
                        child.disabled=True
                    if child.row ==0:
                        child.style=ButtonStyle.green
                        child.label=f"{child.label[:-13]} à joué"
                await interaction.message.edit(view=self)
                await interaction.response.send_message("votre reponse à été enregistré",ephemeral=True)
                while self.symbole_adversaire == None:
                    await asyncio.sleep(1)
                await asyncio.sleep(5)
                button.style=ButtonStyle.blurple
                for child in self.children:
                    if child.row==1:
                        self.remove_item(child)
                button.row=0
                self.add_item(button)
                await interaction.message.edit(view=self)
            else:
                await interaction.response.send_message("vous ne pouvez pas faire ca",ephemeral=True)

        @discord.ui.button(style=ButtonStyle.gray,emoji="📄",row=3,label="")
        async def feuille_adversaire(self,interaction:discord.Interaction,button:discord.ui.Button):
            if interaction.user == self.adversaire:
                self.symbole_adversaire = str(button.emoji)
                chil = self.children
                for child in chil:
                    if child.row==3:
                        child.disabled=True
                    if child.row ==2:
                        child.style=ButtonStyle.green
                        child.label=f"{child.label[:-13]} à joué"
                await interaction.message.edit(view=self)
                await interaction.response.send_message("votre reponse à été enregistré",ephemeral=True)
                while self.symbole_user == None:
                    await asyncio.sleep(1)
                await asyncio.sleep(5)
                button.style=ButtonStyle.blurple
                for child in self.children:
                    if child.row==3:
                        self.remove_item(child)
                button.row=2
                self.add_item(button)
                await interaction.message.edit(view=self)
            else:
                await interaction.response.send_message("vous ne pouvez pas faire ca",ephemeral=True)

        @discord.ui.button(style=ButtonStyle.gray,emoji="✂️",row=1,label="")
        async def ciseaux_user(self,interaction:discord.Interaction,button:discord.ui.Button):
            if interaction.user == self.ctx.user:
                self.symbole_user = str(button.emoji)
                chil = self.children
                for child in chil:
                    if child.row==1:
                        child.disabled=True
                    if child.row ==0:
                        child.style=ButtonStyle.green
                        child.label=f"{child.label[:-13]} à joué"
                await interaction.message.edit(view=self)
                await interaction.response.send_message("votre reponse à été enregistré",ephemeral=True)
                while self.symbole_adversaire == None:
                    await asyncio.sleep(1)
                await asyncio.sleep(5)
                button.style=ButtonStyle.blurple
                for child in self.children:
                    if child.row==1:
                        self.remove_item(child)
                button.row=0
                self.add_item(button)
                await interaction.message.edit(view=self)
            else:
                await interaction.response.send_message("vous ne pouvez pas faire ca",ephemeral=True)

        @discord.ui.button(style=ButtonStyle.gray,emoji="✂️",row=3,label="")
        async def ciseaux_adversaire(self,interaction:discord.Interaction,button:discord.ui.Button):
            if interaction.user == self.adversaire:
                self.symbole_adversaire = str(button.emoji)
                chil = self.children
                for child in chil:
                    if child.row==3:
                        child.disabled=True
                    if child.row ==2:
                        child.style=ButtonStyle.green
                        child.label=f"{child.label[:-13]} à joué"
                await interaction.message.edit(view=self)
                await interaction.response.send_message("votre reponse à été enregistré",ephemeral=True)
                while self.symbole_user == None:
                    await asyncio.sleep(1)
                await asyncio.sleep(5)
                button.style=ButtonStyle.blurple
                for child in self.children:
                    if child.row==3:
                        self.remove_item(child)
                button.row=2
                self.add_item(button)
                await interaction.message.edit(view=self)
            else:
                await interaction.response.send_message("vous ne pouvez pas faire ca",ephemeral=True)
        
        async def on_timeout(self) -> None:
            for child in self.children:
                child.disabled=True
            await self.ctx.edit_original_response(content="*Le temps est écoulé :pensive:*",view=None)

class bouton_solo(discord.ui.View):
        def __init__(self,ctx:discord.Interaction, *, timeout=None):
            self.ctx = ctx
            self.symbole_adversaire = random.choice(["🪨","📄","✂️"])
            self.symbole_user = None
            super().__init__(timeout=timeout)

        @discord.ui.button(style=ButtonStyle.gray,emoji="🪨",row=1,label="")
        async def pierre_user(self,interaction:discord.Interaction,button:discord.ui.Button):
            if interaction.user == self.ctx.user:
                self.symbole_user = str(button.emoji)
                chil = self.children
                for child in chil:
                    if child.row==1:
                        child.disabled=True
                    if child.row ==0:
                        child.style=ButtonStyle.green
                        child.label=f"{child.label[:-13]} à joué"
                await interaction.response.edit_message(view=self)
                button.style=ButtonStyle.blurple
                for child in self.children:
                    if child.row==1:
                        self.remove_item(child)
                button.row=0
                self.add_item(button)
                await interaction.message.edit(view=self)
            else:
                await interaction.response.send_message("vous ne pouvez pas faire ca",ephemeral=True)

        @discord.ui.button(style=ButtonStyle.gray,emoji="📄",row=1,label="")
        async def feuille_user(self,interaction:discord.Interaction,button:discord.ui.Button):
            if interaction.user == self.ctx.user:
                self.symbole_user = str(button.emoji)
                chil = self.children
                for child in chil:
                    if child.row==1:
                        child.disabled=True
                    if child.row ==0:
                        child.style=ButtonStyle.green
                        child.label=f"{child.label[:-13]} à joué"
                await interaction.response.edit_message(view=self)
                button.style=ButtonStyle.blurple
                for child in self.children:
                    if child.row==1:
                        self.remove_item(child)
                button.row=0
                self.add_item(button)
                await interaction.message.edit(view=self)
            else:
                await interaction.response.send_message("vous ne pouvez pas faire ca",ephemeral=True)

        @discord.ui.button(style=ButtonStyle.gray,emoji="✂️",row=1,label="")
        async def ciseaux_user(self,interaction:discord.Interaction,button:discord.ui.Button):
            if interaction.user == self.ctx.user:
                self.symbole_user = str(button.emoji)
                chil = self.children
                for child in chil:
                    if child.row==1:
                        child.disabled=True
                    if child.row ==0:
                        child.style=ButtonStyle.green
                        child.label=f"{child.label[:-13]} à joué"
                await interaction.response.edit_message(view=self)
                button.style=ButtonStyle.blurple
                for child in self.children:
                    if child.row==1:
                        self.remove_item(child)
                button.row=0
                self.add_item(button)
                await interaction.message.edit(view=self)
            else:
                await interaction.response.send_message("vous ne pouvez pas faire ca",ephemeral=True)

        @discord.ui.button(label=f"Botarchauds : à joué",disabled=True,style=discord.ButtonStyle.green,row=2)
        async def bot(self,ctx,button):
            pass
        
        @discord.ui.button(emoji="<:transparent:937043219814965329>",disabled=True,style=discord.ButtonStyle.gray,row=2)
        async def button_bot(self,ctx,button):
            pass

        async def on_timeout(self) -> None:
            for child in self.children:
                child.disabled=True
            await self.ctx.edit_original_response(content="*Le temps est écoulé :pensive:*",view=None)

async def solo(interaction:discord.Interaction,adversaire:discord.User,bot:commands.Bot):
    view=bouton_solo(ctx=interaction,timeout=120)
    view.add_item(item=discord.ui.Button(label=f"{interaction.user.display_name} : tu dois jouer",disabled=True,style=discord.ButtonStyle.red,row=0))
    await interaction.response.send_message(view=view)
    
    while view.symbole_user==None:
        await asyncio.sleep(1)
    
    await asyncio.sleep(0.5)
    view.add_item(item=discord.ui.Button(label=f"Chi",style=ButtonStyle.blurple,row=4))
    await interaction.edit_original_response(view=view)
    view.remove_item(view.children[-1])
    view.add_item(item=discord.ui.Button(label=f"Fou",style=ButtonStyle.blurple,row=4))
    await asyncio.sleep(1)
    await interaction.edit_original_response(view=view)
    view.remove_item(view.children[-1])
    view.add_item(item=discord.ui.Button(label=f"Mi",style=ButtonStyle.blurple,row=4))
    await asyncio.sleep(1)
    await interaction.edit_original_response(view=view)
    view.remove_item(view.children[-1])
    await asyncio.sleep(1)
    
    
    if (view.symbole_user == "✂️" and view.symbole_adversaire == "📄") or (view.symbole_user == "📄" and view.symbole_adversaire == "🪨") or (view.symbole_user == "🪨" and view.symbole_adversaire == "✂️"):
        view.add_item(item=discord.ui.Button(label=f"Bravo {interaction.user.display_name} tu as battu {adversaire.display_name} au chifoumi 👏",row=4,style=ButtonStyle.green,emoji="👏",disabled=True))
        logger.info(f"'{interaction.user.display_name}' a gagné sa partie de 'chifoumi' contre '{adversaire.display_name}' dans le channel '{interaction.channel.name}'")
        await log(bot,interaction.user,f"j'ai gagné ma partie de **chifoumi** contre {adversaire.mention} dans {interaction.channel.mention}")
    elif view.symbole_user == view.symbole_adversaire:
        view.add_item(item=discord.ui.Button(label=f"{interaction.user.display_name}, tu as fait égalité contre {adversaire.display_name}",row=4,style=ButtonStyle.grey,disabled=True))
        logger.info(f"'{interaction.user.display_name}' a fait égalité à sa partie de 'chifoumi' contre '{adversaire.display_name}' dans le channel '{interaction.channel.name}'")
        await log(bot,interaction.user,f"j'ai fait égalité à ma partie de **chifoumi** contre {adversaire.mention} dans {interaction.channel.mention}")
    else:
        view.add_item(item=discord.ui.Button(label=f"{interaction.user.display_name} tu as perdu contre {adversaire.display_name} au chifoumi 😔",row=4,style=ButtonStyle.red,emoji="😔",disabled=True))
        logger.info(f"'{interaction.user.display_name}' a perdu sa partie de 'chifoumi' contre '{adversaire.display_name}' dans le channel '{interaction.channel.name}'")
        await log(bot,interaction.user,f"j'ai perdu ma partie de **chifoumi** contre {adversaire.mention} dans {interaction.channel.mention}")
    view.timeout=None
    view.remove_item(view.children[-4])
    view.add_item(discord.ui.Button(disabled=True,style=discord.ButtonStyle.blurple,emoji=view.symbole_adversaire,row=2))
    await interaction.edit_original_response(view=view)

async def duo(interaction:discord.Interaction,adversaire:discord.User,bot:commands.Bot):
    view=bouton_duo(ctx=interaction,adversaire=adversaire,timeout=120)
    view.add_item(item=discord.ui.Button(label=f"{interaction.user.display_name} : tu dois jouer",disabled=True,style=discord.ButtonStyle.red,row=0))
    view.add_item(item=discord.ui.Button(label=f"{adversaire.display_name} : tu dois jouer",disabled=True,style=discord.ButtonStyle.red,row=2))
    await interaction.response.send_message(f"{adversaire.mention}, {interaction.user.mention} veut faire un chifoumi contre toi",view=view)
    while view.symbole_adversaire==None or view.symbole_user==None:
        await asyncio.sleep(1)
    
    await asyncio.sleep(1.5)
    view.add_item(item=discord.ui.Button(label=f"Chi",style=ButtonStyle.blurple,row=4))
    await interaction.edit_original_response(view=view)
    view.remove_item(view.children[-1])
    view.add_item(item=discord.ui.Button(label=f"Fou",style=ButtonStyle.blurple,row=4))
    await asyncio.sleep(1)
    await interaction.edit_original_response(view=view)
    view.remove_item(view.children[-1])
    view.add_item(item=discord.ui.Button(label=f"Mi",style=ButtonStyle.blurple,row=4))
    await asyncio.sleep(1)
    await interaction.edit_original_response(view=view)
    view.remove_item(view.children[-1])
    await asyncio.sleep(1)
    
    
    if (view.symbole_user == "✂️" and view.symbole_adversaire == "📄") or (view.symbole_user == "📄" and view.symbole_adversaire == "🪨") or (view.symbole_user == "🪨" and view.symbole_adversaire == "✂️"):
        view.add_item(item=discord.ui.Button(label=f"Bravo {interaction.user.display_name} tu as battu {adversaire.display_name} au chifoumi 👏",row=4,style=ButtonStyle.green,emoji="👏",disabled=True))
        logger.info(f"'{interaction.user.display_name}' a gagné sa partie de 'chifoumi' contre '{adversaire.display_name}' dans le channel '{interaction.channel.name}'")
        await log(bot,interaction.user,f"j'ai gagné ma partie de **chifoumi** contre {adversaire.mention} dans {interaction.channel.mention}")
    elif view.symbole_user == view.symbole_adversaire:
        view.add_item(item=discord.ui.Button(label=f"Vous avez fait égalité",row=4,style=ButtonStyle.grey,disabled=True))
        logger.info(f"'{interaction.user.display_name}' a fait égalité à sa partie de 'chifoumi' contre '{adversaire.display_name}' dans le channel '{interaction.channel.name}'")
        await log(bot,interaction.user,f"j'ai fait égalité à sa partie de **chifoumi** contre {adversaire.mention} dans {interaction.channel.mention}")    
    else:
        view.add_item(item=discord.ui.Button(label=f"Bravo {adversaire.display_name} tu as battu {interaction.user.display_name} au chifoumi 👏",row=4,style=ButtonStyle.green,emoji="👏",disabled=True))
        logger.info(f"'{interaction.user.display_name}' a perdu sa partie de 'chifoumi' contre '{adversaire.display_name}' dans le channel '{interaction.channel.name}'")
        await log(bot,interaction.user,f"j'ai perdu ma partie de **chifoumi** contre {adversaire.mention} dans {interaction.channel.mention}")
    view.timeout=None
    await interaction.edit_original_response(view=view)


class chifoumi(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="chifoumi",description="permet de faire un chifoumi avec la personne de son choix, par default le bot")
    @app_commands.rename(user="advesaire")
    @app_commands.describe(user="personne contre qui vous voulez jouer")
    async def chifoumi(self,interaction:discord.Interaction,user:discord.User=None):
        if user == None or user==self.bot.user:
            await solo(interaction=interaction,adversaire=self.bot.user,bot=self.bot)
        else:
            await duo(interaction=interaction,adversaire=user,bot=self.bot)
