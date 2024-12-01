import discord
import os
from dotenv import load_dotenv
from MyClient import MyClient

def main():
    load_dotenv()
    TOKEN_KEY = os.getenv('TOKEN_KEY')
    
    
    intents = discord.Intents.default()
    intents.message_content = True
    intents.presences = True
    intents.members = True
    client = MyClient(intents=intents)
    client.run(TOKEN_KEY)


if __name__=="__main__":
    main()