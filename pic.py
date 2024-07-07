# import discord
# import requests
# import json
# import random
# from bs4 import BeautifulSoup 


# def pic(req) :
#   r = random.randint(1,50000)
#   headers = {
#       'x-rapidapi-key': os.getenv('GK'),
#       'x-rapidapi-host': os.getenv('GH')
#       }
#   url = "https://jikan1.p.rapidapi.com/character/"+str(r)+"/pictures" 
#   response = requests.get( url, headers=headers).text

#   resj= json.loads(response)
#   return resj


# def getPicEmbed :
#   streq = message.content.split("$randpic")[1]
#   responsej= pic(streq)
#   embed = discord.Embed(title="Here is a picture of a random character UwU",color=discord.Color.red() )
#   try :
#     embed.set_image(url=responsej['pictures'][0]['large']) 
#     await message.channel.send(embed=embed)
#   except :
#     await on_message(message)  