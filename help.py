import discord
from replit import db

def getHelpEmbed(message):
  ls= message.content.split(" ")

  embed=discord.Embed ( 
    title="Help", 
    color=discord.Color.from_rgb(51, 153, 102),
    type="article"
  )
  
  if len(ls)==1 :

    for key in db["commands"]:

      embed.add_field(name=key, value=db[key], inline=False)
      
    embed.add_field(name="!help <command>", 
                    value="U can always call !help <command> to know more about the command", 
                    inline=False)
    
  else :
    
    commands = ls[1:]
    for command in commands:
      if command in db["commands"]:
        embed.add_field(name="!help "+command, value=db["commands"][command], inline=False)
      else:
        embed.add_field(name="Error", value="Command "+ command + " not found", inline=False)
        
  return embed
    
