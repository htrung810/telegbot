from cProfile import run
from random import choices
from time import time
from bs4 import BeautifulSoup
import xoso as kq
import os, time, configparser, telebot, requests
from threading import Thread

#Set up
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "setup.cfg"))
config.sections()
token_tele = config['API-TOKEN']['TOKEN']
bot = telebot.TeleBot(f"{token_tele}", parse_mode= None)

#proxy VN
proxy = {'http': 'http://221.132.18.26:8090'}
#time VN
os.environ['TZ'] = 'Asia/Ho_Chi_Minh'
time.tzset()
time_VN = time.strftime('%H:%M')

# start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    global botzz
    botzz = message.chat.id
    start_help = f"""
    Chao {message.from_user.full_name}, day la bot tu dong cua Trung.
    Bay gio la: {time_VN}
    De goi ho tro hay nhan /help
    /bxh:   Cap nhat bang xep hang top 10 moi nhat cua NHA
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
        "https://www.24h.com.vn/bong-da/bang-xep-hang-bong-da-anh-c48a466585.html", proxies= proxy
        )
    handle_data = BeautifulSoup(markup=getdata.text, features= "lxml")
    info_topfive = handle_data.find_all(name='div', attrs={'class': 'info-club'})
    for i in range(0, 10):
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
        if time.strftime("%H:%M") == "19:00":
            for i in range(len(bot_id)):
                bot.send_message(bot_id[i], kq)
        time.sleep(60)


@bot.message_handler(func=lambda m: True)
def echo(m):
    reply_name = [
        "Hihi do ngok",
        "Dung co out hay o lai voi chung toi",
        "Qua la buon luon a",
        "Vị trà yêu thích của anh là gì? Đó là em.",
        "Chocolate đắng đầu lưỡi nhưng ngọt ở cuống họng, như tình yêu anh dành cho em.",
        "Anh có thể làm mọi thứ cho em, ngoại trừ việc yêu em lần nữa.",
        "Trên thế giới có 6 tỉ người. Anh nhớ em bởi vì 5,999,999,999 người còn lại không thể nào thay thế một người đặc biệt như em.",
        "Một cách đơn giản để hạnh phúc là tôn trọng những gì mình đang có.",
        "Người nghèo cũng thèm tiền, người giàu cũng thèm tiền. Chỉ có người anh minh mới thèm hạnh phúc.",
        "Khi yêu ai đó cách mà người ấy gọi tên bạn cũng khiến bạn mỉm cười hạnh phúc.",
        "Yêu một người là nghĩ về người đó cuối cùng trước khi đi ngủ và nhớ về người đó đầu tiên khi tỉnh dậyDuyên do trời định, phận do trời tạo nhưng hạnh phúc là do chính bản thân mình tạo ra. Hãy nhớ và trân trọng điều đó nhé!",
        "Tình yêu biến những điều vô nghĩa của cuộc đời thành những gì có ý nghĩa, làm cho những bất hạnh trở thành hạnh phúc.",
        "Cảm giác hạnh phúc và bình yên nhất chính là được ôm trọn người mình yêu vào buổi tối và nhìn thấy họ đầu tiên vào buổi sáng.",
        "Muốn hạnh phúc trong tình yêu hãy cho đi nhiều hơn, hãy tha thứ, hãy thông cảm, và hãy yêu thương nhiều hơn.",
        "Yêu chính là muốn ở cạnh người đó không rời dù chỉ một phút một giây.",
        "Em biết không?Trên đời này có 2 thứ anh không nên đánh mất.\nThứ nhất là em. Thứ hai là tình yêu của em!"
    ]
    bot.send_message(m.chat.id,f"{choices(reply_name)[0]}")
    time.sleep(1)


if __name__ == "__main__":
    Thread(target= run).start()
    bot.polling(none_stop=True, timeout= 10)