import discord


class get_role:
    def __init__(self, guild:discord.Guild):
        self.chef:discord.Role = guild.get_role(948658049055359046)
        self.ninja_bot:discord.Role = guild.get_role(967510428425015326)
        self.motoculteur:discord.Role = guild.get_role(957045383891152916)
        self.targaryen:discord.Role = guild.get_role(996007769272487987)
        self.jardinier:discord.Role = guild.get_role(948895100346437676)
        self.duo:discord.Role = guild.get_role(948898886515314719)
        self.duel:discord.Role = guild.get_role(948914611644674098)
        self.infini:discord.Role = guild.get_role(967472469101387806)
        self.android:discord.Role = guild.get_role(948915502556794902)
        self.ios:discord.Role = guild.get_role(948914689927155764)
        self.alors:discord.Role = guild.get_role(1000491495117312100)
        self.test:discord.Role = guild.get_role(957631055848939600)