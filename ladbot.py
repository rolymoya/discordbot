import discord 
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('What\'s poppin\'')

@client.command()
async def ping(ctx):
    await ctx.send(f'pongus: {round(client.latency * 1000)}ms')


@client.command(aliases = ['8ball'])
async def eightball(ctx, *,question):
    responses = ['It is certain.', 
    'It is decidedly so.', 
    'Without a doubt.',
    'Yes – definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    'Don\'t count on it.',
    'My reply is no.',
    'My sources say no.',
    'Outlook not so good.',
    'Very doubtful.']

    await ctx.send(f'🎱 {random.choice(responses)}')

@client.command()
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit = amount + 1)
    await ctx.send(f'{ctx.message.author.roles}')


client.run('NzA3Njc3NjI5NzYyODk1ODk1.XrbrpA.6N2JPYo5Rhn9st89xIhrGgPC1Fg') 
