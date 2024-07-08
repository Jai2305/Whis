import discord
import os 
from discord.message import Message
import requests
import json
import random
from bs4 import BeautifulSoup 
from help import getHelpEmbed
from wiki import getWikiEmbed
from genAI import getAIEmbed
from news import getNewsEmbeds


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
    
  content = message.content[:200]
  
  if content.startswith('!hello'):
    await message.channel.send('Hello!')

  if content.startswith('!help'):
    await message.channel.send(embed = getHelpEmbed(message))

  if content.startswith('!wiki'):
    await message.channel.send(embed = getWikiEmbed(message))

  WhisPrefix = ('Whis','!whis','!Whis','whis')
  if content.startswith(WhisPrefix):
    await message.channel.send(embed = getAIEmbed(message))

  if message.content.startswith('!news') :
    for embed in getNewsEmbeds(): await message.channel.send(embed = embed)

client.run(os.environ['DISCORD_KEY'])
