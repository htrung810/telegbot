import os
import environs

env = environs.Env()

if bool(os.getenv("DEBUG", False)):
    env.read_env()
#TOKEN BOT
TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN") 


#light
LIGHT_API = env.str("LIGHT_API", "http://localhost/light")