import discord
import requests
import json
import random
from bs4 import BeautifulSoup 

HYPER_LINK_ATTR = {'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor'}
HEADING_ATTR = {'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'}
SUMMARY_ATTR = {'class':'gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary gs-u-display-none gs-u-display-block@m'}
IMAGE_ATTR = {'class':'gs-o-responsive-image gs-o-responsive-image--16by9'}
IMAGE_ATTR_FIRST_EMBED = {'class':'gs-o-responsive-image gs-o-responsive-image--16by9 gs-o-responsive-image--lead'}
SUMMARY_ATTR_FIRST_EMBED = {'class':'gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary'}

def news():

  url="https://www.bbc.com/news/world"
  res= requests.get(url).text
  soup=BeautifulSoup(res,'html.parser')
  return soup
  
def getNewsEmbeds() :
  
  soup=news()
  hyperlink = soup.findAll('a', HYPER_LINK_ATTR)
  heading = soup.findAll('a', HEADING_ATTR)
  #hn=soup.findAll('h3',{'class':'gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text'})
  summary = soup.findAll('p', SUMMARY_ATTR)
  image = soup.findAll('div', IMAGE_ATTR)
  imagesFirstEmbed=soup.findAll('div', IMAGE_ATTR_FIRST_EMBED)
  summaryFirstEmbed=soup.findAll('p', SUMMARY_ATTR_FIRST_EMBED)
  
  embeds=[]
  # custom initial embed

  firstEmbed = discord.Embed(title="BBC News",
                             url="https://www.bbc.com"+str(hyperlink[0]['href']),
                             color=discord.Color(value=int("b50f04",16)))
  firstEmbed.add_field(name="Top:\n"+str(hyperlink[0]('h3')[0].text),
                       value=str(summaryFirstEmbed[0].text))
  firstEmbed.set_image(url=str(imagesFirstEmbed[0]('img')[0]['src']))
  embeds.append(firstEmbed)
  
  for i in range(0,len(summary)) :
    embed=discord.Embed(title="BBC News",url="https://www.bbc.com"+str(heading[i]['href']),color=discord.Color(value=int("b50f04",16)))
    embed.add_field(name=str(heading[i]('h3')[0].text),
                    value=str(summary[i].text))
    imageURL = str(image[i]('img')[0]['data-src'])
    imageURL = imageURL.replace('{width}','400')
    embed.set_image(url = imageURL)
    embeds.append(embed)



  lastEmbed = discord.Embed(title="read more... ",
                            url="https://www.bbc.com/world",
                            color=discord.Color(value=int("b50f04",16)))

  return embeds