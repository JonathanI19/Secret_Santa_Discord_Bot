import discord

class MyClient(discord.Client):
    
    def init(self):
        pass
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$$test'):
            await message.channel.send('Hello!')
    
    async def on_ready(self):
        print(f"Logged on as {self.user}")