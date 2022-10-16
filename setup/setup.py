import os,time, configparser, telebot


#Set up
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "setup.cfg"))
config.sections()
token_tele = config['API-TOKEN']['TOKEN']
bot_tele = telebot.TeleBot(f"{token_tele}", parse_mode= None)


#set time VN
os.environ['TZ'] = 'Asia/Ho_Chi_Minh'
time.tzset()
time_zone = time.strftime('%H:%M')