"""
JARVIS - A random Discord bot

Firebolt - Aug 31st 2023

Version 2.0 - Full remake of Jarvis from scratch
"""
import os
import discord
import python_weather
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    city = 'Charlottetown'

    if message.author == client.user:
        return

    if message.content == 'Jarvis, you there?':
        await message.channel.send('For you, sir, always.')

    if message.content == 'Jarvis, what is the weather in ' + city:
        await message.channel.send(python_weather.getweather())

client.run(TOKEN)