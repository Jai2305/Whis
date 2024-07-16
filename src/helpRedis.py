import discord
import redis
import os


def getHelpEmbed(message):
  ls= message.content.split(" ")
  r = None

  print(os.getenv('REDIS_URL'))
  r = redis.StrictRedis.from_url(os.getenv('REDIS_URL'))
  print(r.ping())

  embed=discord.Embed ( 
    title="Help", 
    color=discord.Color.from_rgb(51, 153, 102),
    type="article"
  )
  
  if len(ls)==1 :

    for key in r.hgetall("commands"):
      embed.add_field(name=key.decode('utf-8'), value=r.hget("commands", key).decode('utf-8'), inline=False)
      
    embed.add_field(name="!help <command>", 
                    value="U can always call !help <command> to know more about the command", 
                    inline=False)
    
  else :
    
    commands = ls[1:]
    for command in commands:
      if command in [key for key in r.hgetall("commands")]:
        embed.add_field(name="!help "+command, value=r.hget("commands", command), inline=False)
      else:
        embed.add_field(name="Error", value="Command "+ command + " not found", inline=False)
        
  return embed
    
