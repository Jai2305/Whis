import discord
import os 
from discord.message import Message
import requests
import json
import random
from bs4 import BeautifulSoup 

# All functionalities of the bot
from help import getHelpEmbed
from wiki import getWikiEmbed
from genAI import getAIEmbed
from news import getNewsEmbeds
from run import running
from gif import getGIFEmbed

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("Hello")

@client.event
async def on_message(message):

  WhisPrefix = ('Whis','!whis','!Whis','whis')
  
  if message.author == client.user:
    return
    
  content = message.content[:200]
  
  if content.startswith('!hello'):
    await message.channel.send('Hello!')

  elif content.startswith('!help'):
    await message.channel.send(embed = getHelpEmbed(message))

  elif content.startswith('!wiki'):
    await message.channel.send(embed = getWikiEmbed(message))

  elif content.startswith(WhisPrefix):
    await message.channel.send(embed = getAIEmbed(message))

  elif message.content.startswith('!news') :
    for embed in getNewsEmbeds(): await message.channel.send(embed = embed)
      
  elif message.content.startswith('!gif') :
    await message.channel.send(embed = getGIFEmbed(message))

running()
client.run(os.environ['DISCORD_KEY'])
