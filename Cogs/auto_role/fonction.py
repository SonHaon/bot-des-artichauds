import os,json,discord

path=os.path.dirname(os.path.abspath(__file__))+"/info"
true_false={True:"✅ Activé",False:"❌ Désactivé"}

def infos()->dict:
    with open(f"{path}/info.json") as file:
        info=json.load(file)
    return info

def infos_save(info)->None:
    with open(f"{path}/info.json","w") as file:
        file.write(json.dumps(info))

def message_auto_role(interaction:discord.Interaction):
    info = infos()
    message=info["config"]["message_nombre"]
    roles:list=info["roles"]
    message = [message.format(nombre=len(interaction.guild.get_role(role['id']).members),mention=interaction.guild.get_role(role['id']).mention) for role in roles]
    return "\n".join(message)