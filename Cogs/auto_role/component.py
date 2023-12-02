from typing import Optional, Union
import discord,math
from discord.emoji import Emoji
from discord.ext import commands
from discord import TextInput,TextStyle,ButtonStyle
from discord.partial_emoji import PartialEmoji
from discord.ui import *

from .fonction import infos,infos_save,message_auto_role




class boutons_auto_role(discord.ui.View):
    def __init__(self):
        info=infos()
        roles:list=info["roles"]
        super().__init__(timeout=None)
        ligne=0
        role_ligne=len(roles)
        if not role_ligne<=5:
            role_ligne=math.ceil(role_ligne/(math.ceil(role_ligne/5)))
        a=1
        for role in roles:
            if a>role_ligne:
                a=0
                ligne+=1
            else:
                a+=1
            self.add_item(bouton_role(role,ligne))


    @discord.ui.button(
        style=ButtonStyle.grey,
        label="Voir mes roles",
        custom_id="voir_role",
        row=2
    )
    async def view_role(self,interaction:discord.Interaction,button:discord.ui.Button):
        user=interaction.user
        virgule = ", "
        roles2=infos()["roles"]
        roles = []
        ids=[]
        for role in roles2:
            ids.append(role["id"])
        
        for role in user.roles:
            if role.id in ids:
                roles.append(role.mention)
        roles.reverse()
        if roles==[]:
            await interaction.response.send_message(f"vous n'avez aucun role",ephemeral=True)
        else:
            await interaction.response.send_message(f"vous avez les roles suivant : {virgule.join(roles)}",ephemeral=True)
        
        embed = interaction.message.embeds[0]
        embed.set_field_at(0,name=embed.fields[0].name,value=message_auto_role(interaction))
        await interaction.message.edit(embed=embed,view=boutons_auto_role())



class bouton_role(Button):
    def __init__(self,role,ligne):
        self.role=role
        super().__init__(
                style=ButtonStyle.blurple,
                label=role["name"],
                emoji=role["emoji"],
                custom_id=str(role["id"]),
                row=ligne,
            )
        
    async def callback(self,interaction:discord.Interaction):
        role=interaction.guild.get_role(self.role["id"])
        user=interaction.user
        if not role in user.roles:
            await user.add_roles(role,reason="À réagi avec l'auto-role")
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été ajouté",ephemeral=True)
        else:
            await user.remove_roles(role)
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été enlevé",ephemeral=True)
        message = interaction.message
        embed = message.embeds[0]
        embed.set_field_at(0,name=embed.fields[0].name,value=message_auto_role(interaction))
        await message.edit(embed=embed,view=boutons_auto_role())


class message_autorole_modal(Modal):
    def __init__(self,bot) -> None:
        self.bot:commands.bot.Bot=bot
        super().__init__(title="titre",timeout=None) #title of the modal up top
        self.add_item(TextInput(label="titre de l'embed",placeholder="texte qui s'affiche comme titre de l'embed",required=True,style=TextStyle.short)) 
        self.add_item(TextInput(label="texte de l'embed",placeholder="texte qui s'affiche dans l'embed",required=True,style=TextStyle.long)) 
        
    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title = self.children[0].value, description = self.children[1].value)
        embed.add_field(name="Roles : ",value=message_auto_role(interaction))
        embed.set_footer(text = f"{interaction.guild.name}", icon_url=interaction.guild.icon.url)
        await interaction.channel.send(embed=embed,view=boutons_auto_role())
        await interaction.response.send_message("l'auto role à bien été créer",ephemeral=True)
