import json
import os

import discord
from discord.embeds import Embed
import requests
# from replit import db
import redis 


def aiResponse(query) :

  url = "https://chatgpt-42.p.rapidapi.com/chatgpt"
  r = redis.StrictRedis.from_url(os.getenv('REDIS_URL'))

  payload = {
    "messages": [
      {
        "role": r.hget("ai","role").decode('utf-8'),
        "content": query
      }
    ],
    "web_access": False
  }
  headers = {
    "x-rapidapi-key": os.getenv('RAPID_API_KEY'),
    "x-rapidapi-host": os.getenv('GPT_4.0_HOST'),
    "Content-Type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)

  return response.json()['result']


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
