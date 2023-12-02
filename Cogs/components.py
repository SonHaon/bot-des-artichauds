import discord
from discord.ui import view,Button,Select,Modal
from discord import app_commands,ButtonStyle

from roles import get_role
from Cogs.fonction import *

class bouton_sondage(discord.ui.View):
    def __init__(self,label1,emoji1,style1,label2,emoji2,style2):
        self.label1 = label1
        self.emoji1 = emoji1
        self.style1 = style1
        self.label2 = label2
        self.emoji2 = emoji2
        self.style2 = style2
        super().__init__(timeout=None)
    
class ban_modal(Modal):
    def __init__(self,user:discord.Member) -> None:
        self.user = user
        super().__init__(title=f"bannissement de {user.display_name}",timeout=None) #title of the modal up top
        self.add_item(discord.ui.TextInput(label="raison", placeholder="raison pour laquelle vous voulez bannir cette personne",required=False)) 
        
    async def on_submit(self, interaction: discord.Interaction):
        
        embed = discord.Embed(title="Bannissement", color=discord.Color.red())
        embed.set_author(icon_url=interaction.user.display_avatar.url,name=interaction.user.display_name)
        embed.add_field(name="membre banni :",value=self.user.mention,inline=True)
        embed.add_field(name="raison : ", value=f"test : {self.children[0].value}", inline=True)
        embed.set_footer(text=interaction.guild.name,icon_url=interaction.guild.icon.url)
        try:
            await self.user.ban(reason=self.children[0].value)
        except:
            await interaction.response.send_message("je n'ai pas les permissions requise pour bannir cette utilisateur",ephemeral=True)
        else:
            await interaction.response.send_message(embed=embed)
        



class ancien_boutons_auto_role(discord.ui.View):
    def __init__(self,guild:discord.Guild):
        self.roles = get_role(guild)
        super().__init__(timeout=None)
    
    @discord.ui.button(
        style=ButtonStyle.blurple,
        label="event",
        emoji="🎭",
        custom_id="event",
        row=0
    )
    async def event(self,interaction:discord.Interaction,button:discord.ui.Button):
        role=self.roles.event
        user=interaction.user
        if not a_role(user,role):
            await user.add_roles(role,reason="À réagi avec l'auto-role")
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été ajouté",ephemeral=True)
        else:
            await user.remove_roles(role)
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été enlevé",ephemeral=True)
        message = await interaction.channel.fetch_message(interaction.message.id)
        embed = message.embeds[0]
        embed.set_field_at(0,name=embed.fields[0].name,value=message_auto_role(interaction))
        await message.edit(embed=embed,view=self)

    @discord.ui.button(
        style=ButtonStyle.blurple,
        label="duo",
        emoji="🏹",
        custom_id="duo",
        row=0
    )
    async def duo(self,interaction:discord.Interaction,button:discord.ui.Button):
        role=self.roles.duo
        user=interaction.user
        if not a_role(user,role):
            await user.add_roles(role,reason="À réagi avec l'auto-role")
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été ajouté",ephemeral=True)
        else:
            await user.remove_roles(role)
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été enlevé",ephemeral=True)
        message = await interaction.channel.fetch_message(interaction.message.id)
        embed = message.embeds[0]
        embed.set_field_at(0,name=embed.fields[0].name,value=message_auto_role(interaction))
        await message.edit(embed=embed,view=self)

    @discord.ui.button(
        style=ButtonStyle.blurple,
        label="duel",
        emoji="⚔️",
        custom_id="duel",
        row=0
    )
    async def duel(self,interaction:discord.Interaction,button:discord.ui.Button):
        role=self.roles.duel
        user=interaction.user
        if not a_role(user,role):
            await user.add_roles(role,reason="À réagi avec l'auto-role")
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été ajouté",ephemeral=True)
        else:
            await user.remove_roles(role)
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été enlevé",ephemeral=True)
        message = await interaction.channel.fetch_message(interaction.message.id)
        embed = message.embeds[0]
        embed.set_field_at(0,name=embed.fields[0].name,value=message_auto_role(interaction))
        await message.edit(embed=embed,view=self)

    @discord.ui.button(
        style=ButtonStyle.blurple,
        label="ios",
        emoji="📱",
        custom_id="ios",
        row=1
    )
    async def ios(self,interaction:discord.Interaction,button:discord.ui.Button):
        role=self.roles.ios
        user=interaction.user
        if not a_role(user,role):
            await user.add_roles(role,reason="À réagi avec l'auto-role")
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été ajouté",ephemeral=True)
        else:
            await user.remove_roles(role)
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été enlevé",ephemeral=True)
        message = await interaction.channel.fetch_message(interaction.message.id)
        embed = message.embeds[0]
        embed.set_field_at(0,name=embed.fields[0].name,value=message_auto_role(interaction))
        await message.edit(embed=embed,view=self)

    @discord.ui.button(
        style=ButtonStyle.blurple,
        label="android",
        emoji="🤖",
        custom_id="android",
        row=1
    )
    async def android(self,interaction:discord.Interaction,button:discord.ui.Button):
        role=self.roles.android
        user=interaction.user
        if not a_role(user,role):
            await user.add_roles(role,reason="À réagi avec l'auto-role")
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été ajouté",ephemeral=True)
        else:
            await user.remove_roles(role)
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été enlevé",ephemeral=True)
        message = await interaction.channel.fetch_message(interaction.message.id)
        embed = message.embeds[0]
        embed.set_field_at(0,name=embed.fields[0].name,value=message_auto_role(interaction))
        await message.edit(embed=embed,view=self)

    @discord.ui.button(
        style=ButtonStyle.blurple,
        label="alors?",
        emoji="❓",
        custom_id="alors?",
        row=1
    )
    async def alors(self,interaction:discord.Interaction,button:discord.ui.Button):
        role=self.roles.alors
        user=interaction.user
        if not a_role(user,role):
            await user.add_roles(role,reason="À réagi avec l'auto-role")
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été ajouté",ephemeral=True)
        else:
            await user.remove_roles(role)
            await interaction.response.send_message(f"Le role {role.mention} vous à bien été enlevé",ephemeral=True)
        message = await interaction.channel.fetch_message(interaction.message.id)
        embed = message.embeds[0]
        embed.set_field_at(0,name=embed.fields[0].name,value=message_auto_role(interaction))
        await message.edit(embed=embed,view=self)

    @discord.ui.button(
        style=ButtonStyle.grey,
        label="Voir mes roles",
        custom_id="voir_role",
        row=2
    )
    async def view_role(self,interaction:discord.Interaction,button:discord.ui.Button):
        user=interaction.user
        virgule = ", "
        roles = []
        for role in user.roles:
            if role.id == 900046546656182322:
                pass
            else:
                roles.append(role.mention)
        roles.reverse()
        await interaction.response.send_message(f"vous avez les roles suivant : {virgule.join(roles)}",ephemeral=True)
        