# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='Jarvis, ')


@bot.command(name='insult', help='Insults target with a random insult.')
async def insult(ctx, target):
    insults = [
        ' you smell like hobbit feet.',
        ' you\'re so dumb you had to take grade 13.',
        ' if you were a rock band you\'d be Nickelback.',
        ' you make murder sound like a *really* good idea when you talk.'
    ]

    response = target + random.choice(insults)
    await ctx.send(response)


@bot.command(name='compliment', help='Compliments target with random compliment.')
async def compliment(ctx, target):
    compliments = [
        ' you\'re hotter than Scarlett Johansson in the middle of a supernova.',
        ' you\'re like, the best thing since porn.',
        ' you\'re like crack, but in a good way.',
        ' you got a nice ass.'
    ]

    response = target + random.choice(compliments)
    await ctx.send(response)


@bot.event
async def on_ready():
    print('J.A.R.V.I.S. is online!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'Jarvis, you there?':
        response = 'For you, sir, always.'
        await message.channel.send(response)

    if message.content == 'Jarvis, you ever hear the tale of Jonah?':
        response = 'I wouldn\'t consider him a role model.'
        await message.channel.send(response)

    await bot.process_commands(message)


bot.run(TOKEN)
