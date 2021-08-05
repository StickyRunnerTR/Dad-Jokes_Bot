import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix=None, help_command=None)

@client.event
async def on_ready():
    print('Currently Online as {0.user}'.format(client))

@commands.cooldown(1, 60, commands.BucketType.guild)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith( "i am dad"):
        await message.channel.send('No, I am dad')

    elif message.content.lower().startswith("im dad"):
        await message.channel.send('No, I am dad')

    elif message.content.lower().startswith("i'm dad" or "im dad" or "i am dad"):
        await message.channel.send('No, I am dad')

    elif message.content.lower().startswith("i'm "):
        await message.channel.send('Hi {}, i\'m Dad'.format(message.content[4:]))
        await message.add_reaction('<:OMEGALUL:861981687542186045>')
    
    elif message.content.lower().startswith("im "):
        await message.channel.send('Hi {}, i\'m Dad'.format(message.content[3:]))
        await message.add_reaction('<:OMEGALUL:861981687542186045>')

    elif message.content.lower().startswith("i am "):
        await message.channel.send('Hi {}, i\'m Dad'.format(message.content[5:]))
        await message.add_reaction('<:OMEGALUL:861981687542186045>')
   

client.run(os.getenv('TOKEN'))
