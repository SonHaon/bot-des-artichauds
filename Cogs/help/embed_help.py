import asyncio 
import discord 
from discord.ext import  commands 
from discord import  app_commands,ButtonStyle 
from discord.ui import * 
import random 


embeds_jeux = [
discord.Embed(title="**__Menu d'aide pour les commandes de jeux__**",description=
"""> </chifoumi:994680684864098364> : lance un chifoumi contre le joueur de son choix ou le bot

> </trouve_le_nombre:994652514114863154> : lance une partie de trouve le nombre

> </dé:1012375613979512884> : lance un dé, on peut choisir le nombre minimum et maximum que le dé peut donner
"""),
discord.Embed(title="**__Menu d'aide pour les commandes de jeux__**").add_field(name="**</chifoumi:994680684864098364> :**",value=
"""lance un chifoumi contre le joueur de son choix ou le bot

si le champ `adversaire` n'est pas renseigné, l'adversaire est le bot
"""),
discord.Embed(title="**__Menu d'aide pour les commandes de jeux__**").add_field(name="**</trouve_le_nombre:994652514114863154> :**",value=
"""lance une partie de trouve le nombre

le bot choisit un nombre entre 1 et 100,
le but du jeu est de trouver ce nombre en le moins d'essais possible,
à chaque essai le bot dira si le nombre est plus grand ou plus petit que le nombre proposé

vous pouvez choisir de changer la difficulté avec le paramètre `difficulté`, par défaut la difficulté est sur *normal*
"""),
discord.Embed(title="**__Menu d'aide pour les commandes de jeux__**").add_field(name="**</dé:1012375613979512884> :**",value=
"""lance un dé,

on peut choisir les valeur minimal et maximal que le dé peut donné grace au paramètre `nombre_minimun` et `nombre_maximum`
""")
]

embeds_normal = [
    discord.Embed(title="**__Menu d'aide pour les autres commandes__**",description=
"""> **</ping:1012375613979512883>** : répond pong

> **</quote:994642227559141467>** : permets de citer un message
"""),
discord.Embed(title="**__Menu d'aide pour les autres commandes__**").add_field(name="**</ping:1012375613979512883> :**",value=
"""répond pong

sert à avoir si le bot fonctionne
"""),
discord.Embed(title="**__Menu d'aide pour les autres commandes__**").add_field(name="**</quote:994642227559141467> :**",value=
"""permets de citer un message

il faut rentrer l'id du message a citer dans `id_du_message`

si vous ne savez pas comment recupérer l'id d'un message je vous invite a fait `/help id` et suivre le tuto
""")
]

embeds_moderation=[
    discord.Embed(title="**__Menu d'aide pour les commandes de modération__**",description=
"""> **</clear:1007719803278070010>** : clear un nombre donné de message
"""),
discord.Embed(title="**__Menu d'aide pour les commandes de modération__**").add_field(name="**</clear:1007719803278070010> :**",value=
"""clear un nombre donné de message

il faut rentrer le nombre de message à supprimmé dans `nombre_de_message`
""")
]

embeds_troll = [
    discord.Embed(title="**__Menu d'aide pour les commandes de troll__**",description=
"""> **</say:995223495153819648>** : fait envoyer un message au bot

> **</add_reaction:1012375613979512882>** : fait ajouter une reaction sur un message au bot
"""),
discord.Embed(title="**__Menu d'aide pour les commandes de troll__**").add_field(name="**</say:995223495153819648> :**",value=
"""fais envoyer un message au bot

il faut mettre le message à envoyer dans `message`,
on peut mettre le channel dans `channel`, par défaut c'est le channel ou la commande est effectué,
on peut mettre des fichiers dans `fichier`
"""),
discord.Embed(title="**__Menu d'aide pour les commandes de troll__**").add_field(name="**</add_reaction:1012375613979512882> :**",value=
"""fait ajouter une reaction sur un message au bot

il faut mettre l'emoji dans `emoji`
il faut mettre l'id du message dans `id_du_message`

si vous ne savez pas comment recupérer l'id d'un message je vous invite a fait `/help id` et suivre le tuto
""")
]

embed_default=discord.Embed(title="**__Menu d'aide pour les commandes__**",description="""
choisissez grace au menu deroulant la categorie de la commandes pour laquelle vous voulez de l'aide""").add_field(name="**Catégorie :**",value="""
> **Jeux** : *</chifoumi:994680684864098364>*,  *</trouve_le_nombre:994652514114863154>*,  *</dé:1012375613979512884>*

> **Autre** : *</ping:1012375613979512883>*,  *</quote:994642227559141467>*""")

embed_default_admin=discord.Embed(title="**__Menu d'aide pour les commandes__**",description="""
choisissez grace au menu deroulant la categorie de la commandes pour laquelle vous voulez de l'aide""").add_field(name="**Catégorie :**",value="""
> **Jeux** : *</chifoumi:994680684864098364>*,  *</trouve_le_nombre:994652514114863154>*,  *</dé:1012375613979512884>*

> **Autre** : *</ping:1012375613979512883>*,  *</quote:994642227559141467>*

> **Modération** : *</clear:1007719803278070010>*

> **troll** : *</say:995223495153819648>*,  *</add_reaction:1012375613979512882>*""")

embeds_help=[embeds_jeux,embeds_normal]

embeds_help_admin=[embeds_jeux,embeds_normal,embeds_moderation,embeds_troll]



embeds_id_pc = [
discord.Embed(title="**__Trouver l'id d'un message sur pc__**",description="""
Pour trouver l'id d'un message il faut commencer par activer le mode développeur,
pour ça, il faut aller dans les paramètres*(image 1)*, dans `avancé` *(image 2)* et coché le mode développeur *(image 3)*.

ensuite, il suffit de faire clique droit sur le message et de cliquer sur copier l'identifiant *(image 4)* 
"""),
discord.Embed(title="image 1").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095888551411764/image_pc_1.png"),
discord.Embed(title="image 2").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095888912142486/image_pc_2.png"),
discord.Embed(title="image 3").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095889251872859/image_pc_3.png"),
discord.Embed(title="image 4").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095889692282940/image_pc_4.png")
]
embeds_id_iphone = [
discord.Embed(title="**__Trouver l'id d'un message sur iphone__**",description="""
Pour trouver l'id d'un message, il faut commencer par activer le mode développeur,
pour ça, il faut aller dans les paramètres *(image 1)*, dans `apparence` *(image 2)* et coché le mode développeur *(image 3)*.

ensuite, il suffit de faire rester appuyer sur le message et de cliquer sur `copier l'identifiant` *(image 4)* (il est possible qu'il fasse faire défiler le menu pour le voir)
"""),
discord.Embed(title="image 1").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095124642836590/image_iphone_1.jpeg"),
discord.Embed(title="image 2").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095124974178304/image_iphone_2.jpeg"),
discord.Embed(title="image 3").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095125322309672/image_iphone_3.jpeg"),
discord.Embed(title="image 4").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095125573972040/image_iphone_4.jpeg")
]
embeds_id_android = [
discord.Embed(title="**__Trouver l'id d'un message sur android__**",description="""
Pour trouver l'id d'un message, il faut commencer par activer le mode développeur,
pour ça, il faut aller dans les paramètres *(image 1)*, dans `apparence` *(image 2)* et coché le mode développeur *(image 3)*.

ensuite, il suffit de faire rester appuyer sur le message et de cliquer sur `copier l'identifiant` *(image 4)* (il est possible qu'il fasse faire défiler le menu pour le voir)
"""),
discord.Embed(title="image 1").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095097098833940/image_android_1.jpeg"),
discord.Embed(title="image 2").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095097639907409/image_android_2.jpeg"),
discord.Embed(title="image 3").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095097908346890/image_android_3.jpeg"),
discord.Embed(title="image 4").set_image(url="https://media.discordapp.net/attachments/1013092004890157116/1013095098218717266/image_android_4.jpeg")
]




embeds_id = [embeds_id_pc,embeds_id_iphone,embeds_id_android]