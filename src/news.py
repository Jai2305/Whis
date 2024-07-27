import discord
import requests
from bs4 import BeautifulSoup 
import random


TOTAL_NEWS = 5

def news():

  url_base = "https://www.bbc.com"
  url = url_base+"/news/world"
  res = requests.get(url).text
  
  soup = BeautifulSoup(res,'html.parser')
  newsCards = set(soup.findAll('div',  {'data-testid': 'edinburgh-card'}))
  
  headlines = [newsCard.find('h2', {'data-testid': 'card-headline'}).text 
               for newsCard in newsCards]
  descriptions = [newsCard.find('p', {'data-testid': 'card-description'}).text 
                  for newsCard in newsCards]
  images = [newsCard.find('div', {'data-testid': 'card-media'})
                .findAll('img')[1]['src'] for newsCard in newsCards]
  links = [url_base+newsCard.find('a',  {'data-testid': 'internal-link'})['href'] 
           for newsCard in newsCards]

  return headlines, images, descriptions, links


def getNewsEmbeds() :
  
  embeds = []
  headlines, images, descriptions, links = news()
  totalResponses = len(headlines)
  
  for i in range(TOTAL_NEWS):
    index = random.randint(0, totalResponses-1)
     
    embed = discord.Embed(title = headlines[index],
                          color = discord.Color.from_rgb(0, 153, 255),
                          url = links[index])
    embed.set_image(url=images[index])
    embed.add_field(name="Description", value=descriptions[index], inline=False)
    embeds.append(embed)

  return embeds
