from cProfile import run
from email import message
from unicodedata import name
from bs4 import BeautifulSoup
import ex9_2 as kq
import requests
import telebot
import configparser
import os
import time
from datetime import datetime
from threading import Thread


#Set up
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "setup.cfg"))
config.sections()
token_tele = config['API-TOKEN']['TOKEN']
bot = telebot.TeleBot(f"{token_tele}", parse_mode= None)


# start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    global botzz
    botzz = message.chat.id
    localtime = datetime.now().strftime("%H:%M")
    start_help = f"""
    Chao {message.from_user.full_name}, day la bot tu dong cua Trung.
    Bay gio la: {localtime}
    De goi ho tro hay nhan /help
    /bxh:   Cap nhat bang xep hang top 5 moi nhat cua NHA
    /kqxs:  Ket qua xo so mien Bac ngay hom nay
    /cat:   1 su dang iu khong he nhe hehe
    """
    bot.send_message(message.chat.id, start_help)


def save_bot():
    try:
        bot_id = []
        if botzz not in bot_id:
            bot_id.append(botzz)
    except NameError:
        pass
    return bot_id


# Ngoai hang anh
def nha():
    name_clb = []
    getdata = requests.get(
        "https://www.24h.com.vn/bong-da/bang-xep-hang-bong-da-anh-c48a466585.html"
        )
    handle_data = BeautifulSoup(markup=getdata.text, features= "lxml")
    info_topfive = handle_data.find_all(name='div', attrs={'class': 'info-club'})
    for i in range(0, 5):
        clb_f = " ".join(info_topfive[i].text.split())
        name_clb.append(f"TOP{i + 1}: {clb_f}")
    result = '\n'.join(name_clb)
    return result
@bot.message_handler(commands=['bxh'])
def bxh(message):
    bxh_nha = nha()
    bot.reply_to(message, bxh_nha)


# Ket Qua xo so
def kqxs_hehe():
    price = kq.get_xoso()
    result_1 = []
    for i in price:
        if i == "g0":
            result_1.append(f"Giai Dac Biet: {price[i]}")
        else:
            a = f'{i}: {price[i]}'
            result_1.append(a)
    result = "\n".join(result_1)
    return result
@bot.message_handler(commands=['kqxs'])
def kqxs(message):
    kqxs_1 = kqxs_hehe()
    bot.reply_to(message, kqxs_1)


# cute
def cat():
    c = requests.get("https://api.thecatapi.com/v1/images/search").json()
    for image in c:
        return image["url"]
@bot.message_handler(commands=['cat'])
def cats(message):
    a = cat()
    bot.send_photo(message.chat.id, a)


def run():
    while True:
        kq = kqxs_hehe()
        bot_id = save_bot()
        if datetime.now().strftime("%H:%M") == "20:26":
            for i in range(len(bot_id)):
                bot.send_message(bot_id[i], kq)
        time.sleep(60)


@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.send_message(m.chat.id,"Khong co gi de reply lai het :'((")
    time.sleep(1)


if __name__ == "__main__":
    Thread(target= run).start()
    bot.polling(none_stop=True, timeout= 10)