import discord
from SSUser import SSUser

class MyClient(discord.Client):
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$$randomize'):
            await self.randomize_secret_santa_process(message)
    
    async def on_ready(self):
        print(f"Logged on as {self.user}")
        
    async def randomize_secret_santa_process(self, message):
        self.user_list = []
        self.set_channel_id(message.channel.id)
        self.generate_SSusers()
        # self.assign_secret_santas()

        
    def generate_SSusers(self):
        channel = self.get_channel(self.get_channel_id())
        members = channel.members
        for member in members:
            self.user_list.append(SSUser(member))

    def assign_secret_santas(self):
        users = self.generate_user_list()


    def get_channel_id(self):
        return self.channel_id
    
    def set_channel_id(self, id):
        self.channel_id = id
