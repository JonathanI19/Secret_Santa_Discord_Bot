import discord
import os
import dotenv
def main():
    load_dotenv()
    TOKEN_KEY = os.getenv('TOKEN_KEY')
    
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(TOKEN_KEY)


if __name__=="__main__":
    main()