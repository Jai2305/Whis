import discord
import os 
import requests
import json
import random
from bs4 import BeautifulSoup 

from help import getHelpEmbed
from wiki import getWikiEmbed



intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("Hello")

@client.event
async def on_message(message):
  
  if message.author == client.user:
    return
    
  if message.content.startswith('!hello'):
    await message.channel.send('Hello!')
    
  if message.content.startswith('!help'):
    await message.channel.send(embed=getHelpEmbed(message))

  if message.content.startswith('!wiki'):
    await message.channel.send(embed=getWikiEmbed(message))

client.run(os.environ['DISCORD_KEY'])
