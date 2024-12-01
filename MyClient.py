import discord

class MyClient(discord.Client):
    
    def init(self):
        self.user_list = []
        self.channel_id = 0
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$$randomize'):
            await self.randomize_secret_santa_process(message)
    
    async def on_ready(self):
        print(f"Logged on as {self.user}")
        print(self.get_all_channels())
        
    async def randomize_secret_santa_process(self, message):
        self.set_channel_id(message.channel.id)
        self.generate_user_list()

    def get_channel_id(self):
        return self.channel_id
    
    def set_channel_id(self, id):
        self.channel_id = id
        
    def generate_user_list(self):
        channel = self.get_channel(self.get_channel_id())
        members = channel.members

