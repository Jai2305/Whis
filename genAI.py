import json
import os

import discord
from discord.embeds import Embed
import requests

from replit import db

import requests

def aiResponse(query) :

  url = "https://chat-gpt-3-5-turbo2.p.rapidapi.com/"

  querystring = {"question": db['gpt']['role']+' '+query}

  headers = {
    "x-rapidapi-key": os.getenv('RAPID_API_KEY'),
    "x-rapidapi-host": os.getenv('GPT_3.5_HOST')
  }

  response = requests.get(url, headers=headers, params=querystring)
  
  return response.json()['answer']


def getAIEmbed(message) :
  query = " ".join(message.content.split(" ")[1:])
  response = aiResponse(query)
  
  embed = discord.Embed(title="Whis replies",
                        color=discord.Color.from_rgb(153, 0, 255))

  #since total Embed limit is 6000, we will safecode our response 500 characters and since AI is trained to reply within 200 words, it should not exceed our limit 
  
  fields = 0
  while(fields < 5):
    fromIndex = fields*1023
    toIndex = (fields+1)*1023
    embed.add_field(name="", value = response[fromIndex:toIndex], inline=False)
    fields+=1

  return embed
