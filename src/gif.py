import discord
import requests
import json
import random
from bs4 import BeautifulSoup 


def gif(query) :

  url = "https://tenor.com/search/"+query

  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  gifs = soup.findAll('div',{'class':'Gif'})
  urls = [gif.find('img')['src'] for gif in gifs]

  return urls, len(urls)
  
def getGIFEmbed(message) :
  req = message.content.split("!gif")[1]

  imgURLs, totalImages = gif(req)
  embed=discord.Embed(title = req, 
                      color=discord.Color.from_rgb(204, 153, 0))
  try :
    embed.set_image(url = imgURLs[random.randint(0, totalImages-1)])
  except :
    embed.add_field(name = "Error", value= "something went wrong X X")
    
  return embed
  
gif("Naruto")