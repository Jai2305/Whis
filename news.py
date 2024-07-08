import discord
import requests
from bs4 import BeautifulSoup 


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
  images = [newsCard.find('img', {'class':'sc-13b8515c-0 hbOWRP'})['src'] 
            for newsCard in newsCards]
  links = [url_base+newsCard.find('a',  {'data-testid': 'internal-link'})['href'] 
           for newsCard in newsCards]

  return headlines, images, descriptions, links


def getNewsEmbeds() :
  
  embeds = []
  headlines, images, descriptions, links = news()
  
  for i in range(TOTAL_NEWS):
    embed = discord.Embed(title=headlines[i],
                          color=discord.Color(value=int("c40831",16)),
                          url= links[i])
    embed.set_image(url=images[i])
    embed.add_field(name="Description", value=descriptions[i], inline=False)
    embeds.append(embed)

  return embeds
