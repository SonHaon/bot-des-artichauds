import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 

from ..couleurs import couleur 
from ..fonction import date_now

import logging 
logger = logging.getLogger('discord.artichauds') 

class trouve_le_nombre(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="trouve_le_nombre",description="flm")
    @app_commands.choices(tentative= [
        app_commands.Choice(name=f"trop trop trop simple (infini essais)",value="999"),
        app_commands.Choice(name="très facile (8 essais)",value="8"),
        app_commands.Choice(name="facile (7 essais)",value="7"),
        app_commands.Choice(name="normal (6 essais)",value="6"),
        app_commands.Choice(name="difficile (5 essais)",value="5"),
        app_commands.Choice(name="très difficile (4 essais)",value="4"),
        app_commands.Choice(name="impossible (3 essais)",value="3"),
        app_commands.Choice(name="1 essai (1 essai)",value="1")
    ])
    @app_commands.rename(tentative="difficulté")
    @app_commands.describe(tentative="difficulté du jeu")
    async def trouve_le_nombre(self,interaction:discord.Interaction,tentative:str="6"):
        tentative=int(tentative)
        nombre = random.randint(1,100)
        def check_message(message:discord.Message):
            return message.author == interaction.user and message.channel == interaction.channel
        nombre_proposé = []
        résultat = []
        embed:discord.Embed = discord.Embed(
            title="**__Trouve le nombre__**",
            description=f"j'ai choisi un nombre entre 1 et 100 tu as {tentative} essai pour le trouver",
            color= couleur.gris
        )
        embed.set_author(name=interaction.user.display_name,icon_url=interaction.user.display_avatar.url)
        embed.set_footer(text=interaction.guild.name,icon_url=interaction.guild.icon.url)
        await interaction.response.send_message(embed=embed)


        for loop in range(1000):
            while True:
                try:
                    essai:discord.Message = await self.bot.wait_for("message", timeout = 30, check = check_message)
                    try:
                        if not essai.content.isdigit():
                            raise
                        if int(essai.content) >= 0 and int(essai.content) <= 100:
                            break
                    except:
                        await interaction.channel.send(content="Veuillez entrer un nombre valide",delete_after=5)
                        await essai.delete()
                except:
                    embed.add_field(name="**__LE TEMPS EST ÉCOULÉ !__**",value="perdu")
                    await interaction.edit_original_response(embed=embed)
                    await interaction.channel.send(content="Le temps est écoulé",delete_after=5)
                    return
            await essai.delete()
            essai = int(essai.content)
            tentative -= 1
            nombre_proposé.append(str(essai))
            if essai == nombre:
                win = True
                break
            elif tentative == 0:
                win = False
                break
            if essai < nombre:
                résultat.append(str(f"**{loop+1})** Le nombre que j'ai choisi est plus **grand** que *{essai}*"))
            elif essai > nombre:
                résultat.append(str(f"**{loop+1})** Le nombre que j'ai choisi est plus **petit** que *{essai}*"))
        
            if loop == 0:
                embed.add_field(name="nombre proposé :", value=", ".join(nombre_proposé),inline=False)
                embed.add_field(name="résultat :",value="\n".join(résultat),inline=False)
                embed.add_field(name="tentative restante :", value=f"{tentative} essais",inline=False)
            else:
                embed.set_field_at(index=0,name="nombre proposé :", value=", ".join(nombre_proposé),inline=False)
                embed.set_field_at(index=1,name="résultat :",value="\n".join(résultat),inline=False)
                embed.set_field_at(index=2,name="tentative restante :", value=f"{tentative} essais",inline=False)
            
            await interaction.edit_original_response(embed = embed)
        
        webhook:discord.Webhook = await self.bot.channel.logs.webhooks()
        webhook = webhook[0]
        if win:
            résultat.append(str(f"**{loop+1})** Bravo vous avez trouvé le nombre que j'avais choisi\nLe nombre était : **__{nombre}__**"))
            embed = discord.Embed(title=embed.title,description=embed.description,color=couleur.full_vert)
            embed.add_field(name="nombre proposé :", value=", ".join(nombre_proposé),inline=False)
            embed.add_field(name="résultat :",value="\n".join(résultat),inline=False)
            embed.add_field(name="nombre d'éssais :",value = f"{loop-tentative} essais")
            logger.info(f"'{interaction.user.display_name}' a gagné sa partie de 'trouve_le_nombre' dans le channel '{interaction.channel.name}', le nombre était '{nombre}'")
            await webhook.send(f"{date_now()} j'ai gagné ma partie de **trouve_le_nombre** dans {interaction.channel.mention}, le nombre était **{nombre}**",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)
        elif not(win):
            embed = discord.Embed(title=embed.title,description=embed.description,color=couleur.full_rouge)
            résultat.append(str(f"**{loop+1})** Dommage vous n'avez pas trouvé le nombre que j'avais choisi.\nLe nombre était : **__{nombre}__**"))
            embed.add_field(name="nombre proposé :", value=", ".join(nombre_proposé),inline=False)
            embed.add_field(name="résultat :",value="\n".join(résultat),inline=False)
            logger.info(f"'{interaction.user.display_name}' a perdu sa partie de 'trouve_le_nombre' dans le channel '{interaction.channel.name}', le nombre était '{nombre}'")
            await webhook.send(f"{date_now()} j'ai perdu ma partie de **trouve_le_nombre** dans {interaction.channel.mention}, le nombre était **{nombre}**",username=interaction.user.display_name,avatar_url=interaction.user.display_avatar.url)
        await interaction.edit_original_response(embed=embed)

