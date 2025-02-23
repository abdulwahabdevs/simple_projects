import asyncio

from config import api_key
from discord import Intents, Client
import responses
import random

def run_bot(token: str):
    # basic setup
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents=intents)
    knowledge: dict = responses.load_knowledge('knowledge.json')

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content == 'roll':
            await message.channel.send('Rolling...')
            roll = random.randint(1, 6)
            await message.channel.send(str(roll))

        if message.content and message.content != 'roll':
            print(f'({message.channel}) {message.author}: "{message.content}"')
            response: str = responses.get_response(message.content, knowledge=knowledge)
            await message.channel.send(response)
        else:
            print('!!!Could not read the message!!!')

    client.run(token=token)

if __name__ == '__main__':
    run_bot(api_key)
