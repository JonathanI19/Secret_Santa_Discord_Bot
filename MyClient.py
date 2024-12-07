import discord
from SSUser import SSUser
from numpy import random

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
        self.assign_secret_santas(self.generate_SSusers())
        await self.send_secret_santas()

    def generate_SSusers(self):
        channel = self.get_channel(self.get_channel_id())
        members = channel.members
        for member in members:
            if member.bot is not True:
                self.user_list.append(SSUser(member))
        return self.user_list

    def choose_candidate(self, member_list):
        return member_list[random.randint(0,len(member_list))]

    def assign_secret_santas(self,users):
        unassigned_participants = []
        for user in users:
            unassigned_participants.append(user)
        for user in users:
            candidate = user
            while candidate == user:
                candidate = self.choose_candidate(unassigned_participants)
            unassigned_participants.remove(candidate)
            user.set_ssid(candidate._id)
            user.set_ssname(candidate._name)
            
    async def send_secret_santas(self):
        for member in self.user_list:
            user = self.get_user(member.get_id())
            await user.send(f"HO HO HO HO HO HO HO")
            
            await user.send("######################################")
            
            await user.send("Welcome to Secret Santa 2024!")
            
            await user.send("######################################")
            
            await user.send("Here are some important rules to keep in mind:")
            await user.send("Budget: ~$20")
            await user.send("Platform: Steam/PSN for Greg")
            await user.send("When: When buying on steam, schedule delivery for Christmas Morning at 10AM")
            await user.send("Please post your steam friend code/username or PSN username in the chat")
            
            await user.send("######################################")
            
            await user.send("You are " + member.get_ssname()+ "'s Secret Santa!")
            
            await user.send("https://thumbs.dreamstime.com/b/bad-santa-28240249.jpg")

        
    
    def get_channel_id(self):
        return self.channel_id
    
    def set_channel_id(self, id):
        self.channel_id = id     