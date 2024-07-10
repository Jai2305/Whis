import discord
import requests
import json
import random
from bs4 import BeautifulSoup 


COLOR_WIKI = discord.Color.from_rgb(255, 255, 255)
ERROR_MESSAGE = "There is no clear response of your query, check ur query once, maybe try capitalizing the first letter for the words if it's a title:"


def wikisearch(query) :
  query = query.strip()
  q = query.split(" ")
  query = "_".join(q)
  url = "http://en.wikipedia.org/wiki/"+query
  return url
  
def getWikiEmbed(message):
  # print(message)
  query = message.content.split("!wiki")[1]
  url = wikisearch(query)

  res = requests.get(url).text
  soup = BeautifulSoup(res,"html.parser")
  res = soup.findAll('p')
  ltxt = 0
  stresponse = ""
  
  for line in res :
    stresponse = stresponse+line.text
    ltxt = len(stresponse)
    if ltxt > 400 :
      break 
      
  if stresponse.startswith('Other reasons this message may be displayed:') :
    embed = discord.Embed(title = query.strip(),
                          color = discord.Color(value=int("c40831",16)),
                          url = url )
    embed.add_field(name="Error :", value = ERROR_MESSAGE)
    return embed

  try:
    embed = discord.Embed(title = query.strip(),
                          color = COLOR_WIKI, url=url )
    embed.add_field(name="According to Wiki :", 
                    value = stresponse, inline=False)
    embed.add_field(name="For reading furthur" ,
                  value="click on the title of the response hilighted in blue color ")
  except:
    embed = discord.Embed(title=query.strip(),
                          color=discord.Color.from_rgb(255, 255, 255),url=url )
    embed.add_field(name="The information is pretty huge " ,
                    value="for reading wikipedia for ur query click on the title of the response hilighted in blue color ")

  return embed