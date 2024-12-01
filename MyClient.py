import discord

class MyClient(discord.Client):
    
    def init():
        pass
    
    
    async def on_ready(self):
        print(f"Logged on as {self.user}")