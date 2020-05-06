import discord 
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('What\'s poppin\'')

client.run('NzA3Njc3NjI5NzYyODk1ODk1.XrMSgw.NJopKSvHg1qNsaS16kghvkXr4wc')