from re import M
import discord
from discord.embeds import Embed
import requests
from bs4 import BeautifulSoup 
from replit import db

import requests


MAIN_URL = 'https://www.geeksforgeeks.org/'
DIV_CLASS_MAIN_TOPICS = 'HomePageArticlesContainer_homePageArticlesContainer_cardsContainer__edrGd'

def getTopics():
  
  url = MAIN_URL
  res = requests.get(url).text
  soup = BeautifulSoup(res, "html.parser")
  container = soup.find('div', {'class': DIV_CLASS_MAIN_TOPICS})
  anchors = container.findAll('a')
  
  # List of sets of (title, url)
  topics = [(anchor.find('span').text, anchor['href']) for anchor in anchors]
  return topics
  

def getGFGEmbed(message):

  request = message.content.split(">")
  print(request)
  print(len(request))
  
  embed = discord.Embed(title="GeeksforGeeks", 
                        color = discord.Color.from_rgb(0, 153, 51),
                        url = MAIN_URL)
  if len(request) == 1: 
    topics = getTopics()
    print(topics)
    for topic in topics:
      
      urlEmbededTopic = f"[{topic[0]}]({topic[1]})"
      embed.add_field(name = '', value = urlEmbededTopic)

  return embed 
    