import os
import environs

env = environs.Env()

if bool(os.getenv("DEBUG", False)):
    env.read_env()

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
LIGHT_API = env.str("LIGHT_API", "http://localhost/light")