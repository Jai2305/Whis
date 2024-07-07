import discord
from replit import db

def getHelpEmbed(message):
  ls=message.content.split(" ")
  if len(ls)==1 :
    embed=discord.Embed(title="Help", 
                        color=discord.Color(value=int("9e0505",16)),
                        type="article"
                       )
    
    for key in db:
      embed.add_field(name=key, value=db[key], inline=False)
      
    embed.add_field(name="$help <command>", 
                    value="U can always call $help <command> to know more about the command", 
                    inline=False)
    
    return embed

