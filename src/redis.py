# for the deployment environments , instead of replit db we will adopt the same behaviour using redis 
# mainly because of it's seamless key value pair and fast retrival 

import redis
import os

def executeRedis():
    try:
        # Create a Redis client
        r = redis.StrictRedis.from_url(os.getenv('REDIS_URL'))

        if r.ping():
            print(f"Connected to Redis server")

        # Commands Whis currently supports 
        commands = {
            "COVID": "This command lets u know about the current covid situation in any country \n Format - !COVID Country: <name>",
            "wiki": "This commands lets u search wiki for the query u mentioned \n Format - !wiki <query>",
            "randw": "This command returns an interesting random word, play with it u can increase ur vocab UwU \n Format - !randw",
            "randpic": "This command returns pic of a random character \n Format - !randpic",
            "gif": "This command returns a gif for ur query \n Format - !gif <query>",
            "hello": "Returns a warm and friendly hello UwU \n Format - !hello",
            "news": "This command returns latest news from BBC world, U can read the full news by clicking on Blue title which says BBC which will take u to the official BBC website, so that u can read the news thoroughly \n At last an option is provided which says read more which will redirect u to the official BBC world website. ",
            "gfg": "returns list of algorithms present on geeksforgeeks.com \n Format: !gfg (will return the list of categories around which algorithms are distributed), \n Format: !gfg > <category> will expand the category and return the list of algorithms related to the category \n Format: !gfg >> <Algorithm> will return the information algorithm specified in the query ",
            "w3s": "returns academic information given by w3school.com on a subject. \n Format: !w3s <subject> (will return list of topics related to the particular subject) .\n Format: !w3s <subject> > <topic> will return information on that particular topic "
        }

        # Setting each command in Redis
        for key, value in commands.items():
            r.hset("commands", key, value)

        # Gen-AI configuration
        ai_config = {
            'role': 'Your name is Whis, you are a great computer science teacher and you assist people with their queries by replying in no more than 200 words, you include coding examples whenever necessary'
        }

        # Setting AI configurations in Redis
        for key, value in ai_config.items():
            r.hset("ai", key, value)

        # Retrieve and print the AI role
        # print(r.hget("gpt", "role").decode('utf-8'))


        else:
            print(f"Could not connect to redis server x-x")

    except Exception as e:
        print(f"Error x-x: {e}")      