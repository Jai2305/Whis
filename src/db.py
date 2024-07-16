# from replit import db

# for key in db.keys():
#   del db[key]

# commands={
#   "COVID":"This command lets u know about the current covid situation in any country \n Format - $COVID Country: <name>",
  
#   "wiki":"This commands lets u search wiki for the query u mentioned \n Format - $wiki <query>",
  
#   "randw":"This command returns an interesting random word, play with it u can increase ur vocab UwU \n Format - $randw",
  
#   "randpic":"This command returns pic of a random character \n Format - $randpic",
  
#   "gif":"This command returns a gif for ur query \n Format - $gif <query>",
  
#   "hello":"Returns a warm and friendly hello UwU \n Format - $hello",
  
#   "news":"This command returns latest news from BBC world, U can read the full news by clicking on Blue title which says BBC which will take u to the official BBC website, so that u can read the news thoroughly \n At last an option is provided which says read more which will redirect u to the official BBC world website. " ,

#   "gfg":"returns list of algorithms present on geeksforgeeks.com \n Format: $gfg (will return the list of categories around which algorithms are distributed), \n Format: $gfg > <category> will expand the category and return the list of algorithms related to the category \n Format: $gfg >> <Algorithm> will return the information algorithm specified in the query ",

#   "w3s":"returns academic information given by w3school.com on a subject. \n Format: $w3s <subject> (will return list of topics related to the particular subject) .\n Format: $w3s <subject> > <topic> will return information on that particular topic "
#   }

# db["commands"] = commands
# for key,value in dict_command.items():
#   db[key]=value

# gptValue = {'role':'Your name is Whis, you are a great computer science teacher and you assist people with their queries by replying in no more than 200 words, you include coding examples whenever necesarry', 
#        'system_prompt':'',
#        'temperature':0.9,
#        'top_k':5,
#        'top_p':0.9,
#        "max_tokens": 256,
#        "web_access": False
#       }

# db["gpt"]["role"] = 'Your name is Whis, you are a great computer science teacher and you assist people with their programming related queries in a simple and concise way in no more than 200 words, you include coding examples whenever necesarry, If multiple questions are asked in the same query then you will give answers to all of them in 50 words or less...'
# print(db["gpt"]["role"])

# for key in db["gpt"]:
#   print(db["gpt"][key])

