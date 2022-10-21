import asyncio
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..checks import check
from ..fonction import recup_message_by_id,date_now
import logging 
logger = logging.getLogger('discord.artichauds') 

class bouton_sondage_ouinon(discord.ui.View):
    def __init__(self,bot):
        super().__init__(timeout=None)
        self.attend = False
        self.bot = bot

    @discord.ui.button(label="OUI",emoji="✅",style=ButtonStyle.green,row=0,custom_id="oui")
    async def oui(self,interaction:discord.Interaction,bouton:discord.ui.Button):
        await interaction.response.send_message("réponse en cours de traitement",ephemeral=True)
        if interaction.message.embeds[1].description:
            if str(interaction.user.id) in interaction.message.embeds[1].description:
                await interaction.edit_original_response(content="vous avez déjà voté")
                return
        while self.attend:
            await asyncio.sleep(0.5)
        self.attend=True
        embed_base = interaction.message.embeds[0]
        embed_votes = interaction.message.embeds[1]
        oui = embed_base.fields[0].value.split("**")
        oui[1] = str(int(oui[1])+1)
        embed_base.set_field_at(index=0,value="**".join(oui),name=embed_base.fields[0].name)
        if not embed_votes.description:
            embed_votes = discord.Embed(title=embed_votes.title,color=embed_votes.color,description=f"{interaction.user.mention} à répondu **__oui ✅__**")
        else:
            votes_list = embed_votes.description.split(",\n")
            votes_list.append(f"{interaction.user.mention} a répondu **__oui ✅__**")
            embed_votes = discord.Embed(title=embed_votes.title,color=embed_votes.color,description=",\n".join(votes_list))
        embed_votes.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
        await interaction.message.edit(embeds=[embed_base,embed_votes])
        await interaction.edit_original_response(content="votre réponse a été enregistré")
        self.attend = False
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai répondu **OUI** au sondage OUI/NON: \n{interaction.message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)

    @discord.ui.button(label="NON",emoji="❌",style=ButtonStyle.red,row=0,custom_id="non")
    async def non(self,interaction:discord.Interaction,bouton:discord.ui.Button):
        await interaction.response.send_message("réponse en cours de traitement",ephemeral=True)
        if interaction.message.embeds[1].description:
            if str(interaction.user.id) in interaction.message.embeds[1].description:
                await interaction.edit_original_response(content="vous avez déjà voté")
                return
        while self.attend:
            await asyncio.sleep(0.5)
        self.attend=True
        embed_base = interaction.message.embeds[0]
        embed_votes = interaction.message.embeds[1]
        non = embed_base.fields[1].value.split("**")
        non[1] = str(int(non[1])+1)
        embed_base.set_field_at(index=1,value="**".join(non),name=embed_base.fields[1].name)
        if not embed_votes.description:
            embed_votes = discord.Embed(title=embed_votes.title,color=embed_votes.color,description=f"{interaction.user.mention} à répondu **__non ❌__**")
        else:
            votes_list = embed_votes.description.split(",\n")
            votes_list.append(f"{interaction.user.mention} a répondu **__non ❌__**")
            embed_votes = discord.Embed(title=embed_votes.title,color=embed_votes.color,description=",\n".join(votes_list))
        embed_votes.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
        await interaction.message.edit(embeds=[embed_base,embed_votes])
        await interaction.edit_original_response(content="votre réponse a été enregistré")
        self.attend = False
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai répondu **NON** au sondage OUI/NON: \n{interaction.message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)

class bouton_sondage_ouinon_anonyme(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.attend = False
        self.vote = []

    @discord.ui.button(label="OUI",emoji="✅",style=ButtonStyle.green,row=0,custom_id="oui_anonyme")
    async def oui(self,interaction:discord.Interaction,bouton:discord.ui.Button):
        await interaction.response.send_message("réponse en cours de traitement",ephemeral=True)
        if interaction.user.id in self.vote:
            await interaction.edit_original_response(content="vous avez déjà voté")
            return
        while self.attend:
            await asyncio.sleep(0.5)
        self.attend=True
        embed_base = interaction.message.embeds[0]
        oui = embed_base.fields[0].value.split("**")
        oui[1] = str(int(oui[1])+1)
        embed_base.set_field_at(index=0,value="**".join(oui),name=embed_base.fields[0].name)
        embed_base.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
        self.vote.append(interaction.user.id)
        await interaction.message.edit(embeds=[embed_base])
        await interaction.edit_original_response(content="votre réponse a été enregistré")
        self.attend = False
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai répondu **OUI** au sondage OUI/NON: \n{interaction.message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)

    @discord.ui.button(label="NON",emoji="❌",style=ButtonStyle.red,row=0,custom_id="non_anonyme")
    async def non(self,interaction:discord.Interaction,bouton:discord.ui.Button):
        await interaction.response.send_message("réponse en cours de traitement",ephemeral=True)
        if interaction.user.id in self.vote:
            await interaction.edit_original_response(content="vous avez déjà voté")
            return
        while self.attend:
            await asyncio.sleep(0.5)
        self.attend=True
        embed_base = interaction.message.embeds[0]
        non = embed_base.fields[1].value.split("**")
        non[1] = str(int(non[1])+1)
        embed_base.set_field_at(index=1,value="**".join(non),name=embed_base.fields[1].name)
        embed_base.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
        self.vote.append(interaction.user.id)
        await interaction.message.edit(embeds=[embed_base])
        await interaction.edit_original_response(content="votre réponse a été enregistré")
        self.attend = False
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai répondu **NON** au sondage OUI/NON: \n{interaction.message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)


class bouton_sondage_perso(discord.ui.View):
    def __init__(self,label1,label2,emoji1,emoji2):
        self.attend = False
        self.label1 = label1
        self.label2 = label2
        self.emoji1 = emoji1
        self.emoji2 = emoji2
        super().__init__(timeout=None)

    @discord.ui.button(label="oui",emoji="✅",style=ButtonStyle.blurple,row=0)
    async def oui(self,interaction:discord.Interaction,bouton:discord.ui.Button):
        await interaction.response.send_message("réponse en cours de traitement",ephemeral=True)
        if interaction.message.embeds[1].description:
            if str(interaction.user.id) in interaction.message.embeds[1].description:
                await interaction.edit_original_response(content="vous avez déjà voté")
                return
        while self.attend:
            await asyncio.sleep(0.5)
        self.attend=True
        embed_base = interaction.message.embeds[0]
        embed_votes = interaction.message.embeds[1]
        oui = embed_base.fields[0].value.split("**")
        oui[1] = str(int(oui[1])+1)
        embed_base.set_field_at(index=0,value="**".join(oui),name=embed_base.fields[0].name)
        if not embed_votes.description:
            embed_votes = discord.Embed(title=embed_votes.title,color=embed_votes.color,description=f"{interaction.user.mention} à répondu **__{self.label1} {self.emoji1}__**")
        else:
            votes_list = embed_votes.description.split(",\n")
            votes_list.append(f"{interaction.user.mention} a répondu **__{self.label1} {self.emoji1}__**")
            embed_votes = discord.Embed(title=embed_votes.title,color=embed_votes.color,description=",\n".join(votes_list))
        embed_votes.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
        await interaction.message.edit(embeds=[embed_base,embed_votes])
        await interaction.edit_original_response(content="votre réponse a été enregistré")
        self.attend = False
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai répondu **{bouton.label}** au sondage {self.label1}/{self.label2}: \n{interaction.message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)

    @discord.ui.button(label="non",emoji="❌",style=ButtonStyle.blurple,row=0)
    async def non(self,interaction:discord.Interaction,bouton:discord.ui.Button):
        await interaction.response.send_message("réponse en cours de traitement",ephemeral=True)
        if interaction.message.embeds[1].description:
            if str(interaction.user.id) in interaction.message.embeds[1].description:
                await interaction.edit_original_response(content="vous avez déjà voté")
                return
        while self.attend:
            await asyncio.sleep(0.5)
        self.attend=True
        embed_base = interaction.message.embeds[0]
        embed_votes = interaction.message.embeds[1]
        non = embed_base.fields[1].value.split("**")
        non[1] = str(int(non[1])+1)
        embed_base.set_field_at(index=1,value="**".join(non),name=embed_base.fields[1].name)
        if not embed_votes.description:
            embed_votes = discord.Embed(title=embed_votes.title,color=embed_votes.color,description=f"{interaction.user.mention} à répondu **__{self.label2} {self.emoji2}__**")
        else:
            votes_list = embed_votes.description.split(",\n")
            votes_list.append(f"{interaction.user.mention} a répondu **__{self.label2} {self.emoji2}__**")
            embed_votes = discord.Embed(title=embed_votes.title,color=embed_votes.color,description=",\n".join(votes_list))
        embed_votes.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
        await interaction.message.edit(embeds=[embed_base,embed_votes])
        await interaction.edit_original_response(content="votre réponse a été enregistré")
        self.attend = False
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai répondu **{bouton.label}** au sondage {self.label1}/{self.label2}: \n{interaction.message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)


class bouton_sondage_perso_anonyme(discord.ui.View):
    def __init__(self,label1,label2,emoji1,emoji2):
        self.attend = False
        self.label1 = label1
        self.label2 = label2
        self.emoji1 = emoji1
        self.emoji2 = emoji2
        self.vote = []
        super().__init__(timeout=None)

    @discord.ui.button(label="oui",emoji="✅",style=ButtonStyle.blurple,row=0,custom_id="rep1_anonyme")
    async def oui(self,interaction:discord.Interaction,bouton:discord.ui.Button):
        await interaction.response.send_message("réponse en cours de traitement",ephemeral=True)
        if interaction.user.id in self.vote:
            await interaction.edit_original_response(content="vous avez déjà voté")
            return
        while self.attend:
            await asyncio.sleep(0.5)
        self.attend=True
        embed_base = interaction.message.embeds[0]
        oui = embed_base.fields[0].value.split("**")
        oui[1] = str(int(oui[1])+1)
        embed_base.set_field_at(index=0,value="**".join(oui),name=embed_base.fields[0].name)
        embed_base.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
        self.vote.append(interaction.user.id)
        await interaction.message.edit(embeds=[embed_base])
        await interaction.edit_original_response(content="votre réponse a été enregistré")
        self.attend = False
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai répondu **{bouton.label}** au sondage {self.label1}/{self.label2}: \n{interaction.message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)

    @discord.ui.button(label="non",emoji="❌",style=ButtonStyle.blurple,row=0,custom_id="rep2_anonyme")
    async def non(self,interaction:discord.Interaction,bouton:discord.ui.Button):
        await interaction.response.send_message("réponse en cours de traitement",ephemeral=True)
        if interaction.user.id in self.vote:
            await interaction.edit_original_response(content="vous avez déjà voté")
            return
        while self.attend:
            await asyncio.sleep(0.5)
        self.attend=True
        embed_base = interaction.message.embeds[0]
        non = embed_base.fields[1].value.split("**")
        non[1] = str(int(non[1])+1)
        embed_base.set_field_at(index=1,value="**".join(non),name=embed_base.fields[1].name)
        embed_base.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
        self.vote.append(interaction.user.id)
        await interaction.message.edit(embeds=[embed_base])
        await interaction.edit_original_response(content="votre réponse a été enregistré")
        self.attend = False
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai répondu **{bouton.label}** au sondage {self.label1}/{self.label2}: \n{interaction.message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)



class sondage(commands.GroupCog, name="sondage"): 
    def __init__(self,bot:commands.Bot) -> None: 
        self.bot = bot 
        super().__init__()

    @app_commands.command(name="oui_non",description="lance un sondage oui/non")
    @check.is_chef()
    @app_commands.choices(
        anonyme=[app_commands.Choice(name="Oui",value="True"),app_commands.Choice(name="Non",value="False")]
    )
    @app_commands.rename(title="titre")
    @app_commands.describe(title="titre du sondage",question="question du sondage")
    async def sondage_ouinon(self,interaction:discord.Interaction,title:str,question:str,anonyme:str):
        if anonyme == "False":
            embed_base = discord.Embed(title=title,description=question,color=couleur.bleu)
            embed_base.add_field(name="__**OUI**__",value=f"**{0}** jardiniers ont voté __oui__",inline=True)
            embed_base.add_field(name="__**NON**__",value=f"**{0}** jardiniers ont voté __non__",inline=True)
            embed_votes = discord.Embed(title="Votes",description=None,color=couleur.bleu)
            embed_votes.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
            await interaction.response.send_message("le sondage est lancé",ephemeral=True)
            message = await interaction.channel.send(embeds=[embed_base,embed_votes],view=bouton_sondage_ouinon())
            logger.info(f"'{interaction.user.display_name}' a lancé un sondage oui/non dans '{interaction.channel.name}'")
            webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
            webhook = webhook[0]
            await webhook.send(f"{date_now()} j'ai lancé un sondage oui/non dans {interaction.channel.mention} : {message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)
        else:
            embed_base = discord.Embed(title=title,description=question,color=couleur.bleu)
            embed_base.add_field(name="__**OUI**__",value=f"**{0}** jardiniers ont voté __oui__",inline=True)
            embed_base.add_field(name="__**NON**__",value=f"**{0}** jardiniers ont voté __non__",inline=True)
            embed_base.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
            await interaction.response.send_message("le sondage est lancé",ephemeral=True)
            message = await interaction.channel.send(embeds=[embed_base],view=bouton_sondage_ouinon_anonyme())
            logger.info(f"'{interaction.user.display_name}' a lancé un sondage anonyme oui/non dans '{interaction.channel.name}'")
            webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
            webhook = webhook[0]
            await webhook.send(f"{date_now()} j'ai lancé un sondage anonyme oui/non dans {interaction.channel.mention} : {message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)


    @app_commands.command(name="fin",description="met fin à un sondage")
    @check.is_chef()
    @app_commands.rename(id="id_du_sondage")
    @app_commands.describe(id="id du message contenant le sondage")
    async def fin(self,interaction:discord.Interaction,id:str):
        await interaction.response.defer(ephemeral=True)
        sondage:discord.Message = await interaction.channel.fetch_message(id)
        
        if not("_anonyme" in sondage.components[0].children[0].custom_id):
            if sondage.components[0].children[0].label == "OUI":
                oui = int(sondage.embeds[0].fields[0].value.split("**")[1])
                non = int(sondage.embeds[0].fields[1].value.split("**")[1])
                total_rep = oui + non
                if total_rep==0:
                    oui_100 = 0
                    non_100 = 0
                else:
                    oui_100 = round(oui/total_rep*100)
                    non_100 = round(non/total_rep*100)
                description = [f"**{oui_100}%** des jardiniers ont répondus __oui__",f"**{non_100}%** des jardiniers ont répondu __non__"]
                if oui > non:
                    color = couleur.full_vert
                    description.append(f"**La majorité des jardiniers ont répondu __oui__**")
                elif oui < non:
                    color=couleur.full_rouge
                    description.append(f"**La majorité des jardiniers ont répondu __non__**")
                else:
                    color = couleur.gris
                    description.append(f"**autant des jardiniers ont répondu __oui__ que __non__**")
                
                embed_résultat = discord.Embed(title="Résultat",color=color,description=",\n".join(description))
            else:
                reponse1 = sondage.components[0].children[0].label
                reponse2 = sondage.components[0].children[1].label
                rep1 = int(sondage.embeds[0].fields[0].value.split("**")[1])
                rep2 = int(sondage.embeds[0].fields[1].value.split("**")[1])
                total_rep = rep1 + rep2
                if total_rep==0:
                    rep1_100 = 0
                    rep2_100 = 0
                else:
                    rep1_100 = round(rep1/total_rep*100)
                    rep2_100 = round(rep2/total_rep*100)
                description = [f"**{rep1_100}%** des jardiniers ont répondus __{reponse1.upper()}__",f"**{rep2_100}%** des jardiniers ont répondu __{reponse2.upper()}__"]
                if rep1 > rep2:
                    description.append(f"\n**La majorité des jardiniers ont répondu __{reponse1.upper()}__**")
                elif rep1 < rep2:
                    description.append(f"\n**La majorité des jardiniers ont répondu __{reponse2.upper()}__**")
                else:
                    description.append(f"\n**Autant des jardiniers ont répondu __{reponse1.upper()}__ que __{reponse2}__**")
                
                embed_résultat = discord.Embed(title="Résultat",color=couleur.bleu,description=",\n".join(description))

            view = discord.ui.View(timeout=None)
            for button in sondage.components:
                bouton = button.children[0]
                view.add_item(discord.ui.Button(style=bouton.style,label=bouton.label,emoji=bouton.emoji,row=0,disabled=True))
                bouton = button.children[1]
                view.add_item(discord.ui.Button(style=bouton.style,label=bouton.label,emoji=bouton.emoji,row=0,disabled=True))
            sondage.embeds[0].description = f"{sondage.embeds[0].description}\n\n**Le sondage est terminé**"
            view.stop()
            embed_résultat.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
            embed_votes= discord.Embed(title=sondage.embeds[1].title,color=sondage.embeds[1].color,description=sondage.embeds[1].description)
            await sondage.edit(view=view,embeds=[sondage.embeds[0],embed_votes,embed_résultat])
            await interaction.edit_original_response(content="Le sondage est terminé")

        else:
            if sondage.components[0].children[0].label == "OUI":
                oui = int(sondage.embeds[0].fields[0].value.split("**")[1])
                non = int(sondage.embeds[0].fields[1].value.split("**")[1])
                total_rep = oui + non
                if total_rep==0:
                    oui_100 = 0
                    non_100 = 0
                else:
                    oui_100 = round(oui/total_rep*100)
                    non_100 = round(non/total_rep*100)
                description = [f"**{oui_100}%** des jardiniers ont répondus __oui__",f"**{non_100}%** des jardiniers ont répondu __non__"]
                if oui > non:
                    color = couleur.full_vert
                    description.append(f"**La majorité des jardiniers ont répondu __oui__**")
                elif oui < non:
                    color=couleur.full_rouge
                    description.append(f"**La majorité des jardiniers ont répondu __non__**")
                else:
                    color = couleur.gris
                    description.append(f"**autant des jardiniers ont répondu __oui__ que __non__**")
                
                embed_résultat = discord.Embed(title="Résultat",color=color,description=",\n".join(description))
            else:
                reponse1 = sondage.components[0].children[0].label
                reponse2 = sondage.components[0].children[1].label
                rep1 = int(sondage.embeds[0].fields[0].value.split("**")[1])
                rep2 = int(sondage.embeds[0].fields[1].value.split("**")[1])
                total_rep = rep1 + rep2
                if total_rep==0:
                    rep1_100 = 0
                    rep2_100 = 0
                else:
                    rep1_100 = round(rep1/total_rep*100)
                    rep2_100 = round(rep2/total_rep*100)
                description = [f"**{rep1_100}%** des jardiniers ont répondus __{reponse1.upper()}__",f"**{rep2_100}%** des jardiniers ont répondu __{reponse2.upper()}__"]
                if rep1 > rep2:
                    description.append(f"\n**La majorité des jardiniers ont répondu __{reponse1.upper()}__**")
                elif rep1 < rep2:
                    description.append(f"\n**La majorité des jardiniers ont répondu __{reponse2.upper()}__**")
                else:
                    description.append(f"\n**Autant des jardiniers ont répondu __{reponse1.upper()}__ que __{reponse2}__**")
                
                embed_résultat = discord.Embed(title="Résultat",color=couleur.bleu,description=",\n".join(description))

            view = discord.ui.View(timeout=None)
            for button in sondage.components:
                bouton = button.children[0]
                view.add_item(discord.ui.Button(style=bouton.style,label=bouton.label,emoji=bouton.emoji,row=0,disabled=True))
                bouton = button.children[1]
                view.add_item(discord.ui.Button(style=bouton.style,label=bouton.label,emoji=bouton.emoji,row=0,disabled=True))
            view.stop()
            embed_résultat.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
            embed_base= discord.Embed(title=sondage.embeds[0].title,color=sondage.embeds[0].color,description=f"{sondage.embeds[0].description}\n\n**Le sondage est terminé**")
            embed_base.add_field(name=sondage.embeds[0].fields[0],inline=True)
            embed_base.add_field(name=sondage.embeds[0].fields[1],inline=True)
            await sondage.edit(view=view,embeds=[embed_base,embed_résultat])
            await interaction.edit_original_response(content="Le sondage est terminé")
        
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        await webhook.send(f"{date_now()} j'ai lancé un sondage anonyme oui/non dans {interaction.channel.mention} : {sondage.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)



    @app_commands.command(name="personnalisé",description="créer un sondage avec deux choix personalisable")
    @check.is_chef()
    @app_commands.choices(
        anonyme=[app_commands.Choice(name="Oui",value="True"),app_commands.Choice(name="Non",value="False")]
    )
    @app_commands.rename(
        anonyme="anonyme",
        choix1="réponse_1",
        emoji1="emoji_1",
        choix2="réponse_2",
        emoji2="emoji_2"
    )
    @app_commands.describe(
        titre="titre du sondage",
        question="question du sondage",
        anonyme="est-ce que le sondage sera anonyme",
        choix1="première proposition",
        emoji1="émoji pour la première proposition",
        choix2="deuxième proposition",
        emoji2="émoji pour la deuxième proposition"
    )
    async def sondage_perso(self,interaction:discord.Interaction,titre:str,question:str,anonyme:str,choix1:str,choix2:str,emoji1:str="",emoji2:str=""):
        if anonyme == "False":
            embed_base = discord.Embed(title=titre,description=question,color=couleur.bleu)
            embed_base.add_field(name=f"__**{choix1} {emoji1}**__",value=f"**{0}** jardiniers ont voté __{choix1} {emoji1}__",inline=True)
            embed_base.add_field(name=f"__**{choix2} {emoji2}**__",value=f"**{0}** jardiniers ont voté __{choix2} {emoji2}__",inline=True)
            embed_votes = discord.Embed(title="Votes",description=None,color=couleur.bleu)
            embed_votes.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
            view = bouton_sondage_perso(label1=choix1,label2=choix2,emoji1=emoji1,emoji2=emoji2)
            view.children[0].label = choix1
            view.children[1].label = choix2
            if emoji1 == "":
                view.children[0].emoji = None
            else:
                view.children[0].emoji = emoji1
            if emoji2 == "":
                view.children[1].emoji = None
            else:
                view.children[1].emoji = emoji2
            await interaction.response.send_message("le sondage est lancé",ephemeral=True)
            message = await interaction.channel.send(embeds=[embed_base,embed_votes],view=view)
            logger.info(f"'{interaction.user.display_name}' a lancé un sondage '{choix1}/{choix2}' dans '{interaction.channel.name}'")
            webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
            webhook = webhook[0]
            await webhook.send(f"{date_now()} j'ai lancé un sondage {choix1}/{choix2} dans {interaction.channel.mention} : {message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)
        else:
            embed_base = discord.Embed(title=titre,description=f"{question}\n\nCe sondage est anonyme.",color=couleur.bleu)
            embed_base.add_field(name=f"__**{choix1} {emoji1}**__",value=f"**{0}** jardiniers ont voté __{choix1} {emoji1}__",inline=True)
            embed_base.add_field(name=f"__**{choix2} {emoji2}**__",value=f"**{0}** jardiniers ont voté __{choix2} {emoji2}__",inline=True)
            embed_base.set_footer(icon_url=interaction.guild.icon.url,text=interaction.guild.name)
            view = bouton_sondage_perso_anonyme(label1=choix1,label2=choix2,emoji1=emoji1,emoji2=emoji2)
            view.children[0].label = choix1
            view.children[1].label = choix2
            if emoji1 == "":
                view.children[0].emoji = None
            else:
                view.children[0].emoji = emoji1
            if emoji2 == "":
                view.children[1].emoji = None
            else:
                view.children[1].emoji = emoji2
            await interaction.response.send_message("le sondage est lancé",ephemeral=True)
            await interaction.channel.send(embeds=[embed_base],view=view)
            logger.info(f"'{interaction.user.display_name}' a lancé un sondage anonyme '{choix1}/{choix2}' dans '{interaction.channel.name}'")
            webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
            webhook = webhook[0]
            await webhook.send(f"{date_now()} j'ai lancé un sondage anonyme {choix1}/{choix2} dans {interaction.channel.mention} : {message.jump_url}",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)