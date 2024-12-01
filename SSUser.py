import discord

class SSUser(discord.User):
    
    def __init__(self, member):
        self._name = member.name  # Private attribute
        self._id = member.id # Private attribut
        self._ssid = "" # Private attribut

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def get_id(self):
        return self._id

    def get_ssid(self):
        return self._ssid

    def set_ssid(self, ssid):
        self._ssid = ssid