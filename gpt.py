import json
import os

import discord
from discord.embeds import Embed
import requests

from replit import db

def gptResponse(query) :
  url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"
  payload = {}
  gptMessage = {}
  gptMessage['content'] = query
  
  for key in db["gpt"]:
    if key == "role":
      gptMessage['role'] = db["gpt"][key]
      continue 
    payload[key] = db["gpt"][key]

  payload["messages"] = [gptMessage]

  headers = {
    "x-rapidapi-key": os.getenv('RAPID_API_KEY'),
    "x-rapidapi-host": os.getenv('GPT_HOST'),
    "Content-Type": "application/json"
  }
  response = requests.post(url, json=payload, headers=headers)
  print(response.json())
  return response.json()["result"]


def getGPTEmbed(message) :
  query = message.content.split(" ")[1:]
  response = gptResponse(query)
  
  embed = discord.Embed(title="Whis replies",
                        color=discord.Color(value=int("9e0505",16)))

  #since total Embed limit is 6000, we will safecode our response 500 characters and since gpt is noded to reply within 200 words, it should exceed our limit 
  fields = 0
  while(fields < 5):
    fromIndex = fields*1023
    toIndex = (fields+1)*1023
    embed.add_field(name="", value = response[fromIndex:toIndex], inline=False)
    fields+=1

  return embed
