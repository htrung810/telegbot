from cProfile import run
from random import choices
from time import time
import data.link as link
import setup.setup as set_tele
import time


bot = set_tele.bot_tele
time_VN = set_tele.time_zone


# start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    start_help = f""" \n
    Chào {message.from_user.full_name}, đây là bot tự động của Trung, chúc bạn có một ngày mới vui vẻ.
    Bây giờ là: {time_VN}
    Gọi hỗ trợ lệnh hãy bấm /help.
    /bxh :   Cập nhật BXH top 10 mới nhất NHA.
    /kqxs:   Kết quả xổ số miền Bắc hôm nay.
    /cat :   Kêu gọi meow meow
    """
    bot.send_message(message.chat.id, start_help)


# Ngoai hang anh
@bot.message_handler(commands=['bxh'])
def bxh(message):
    bxh_nha = link.nha.nha()
    bot.reply_to(message, bxh_nha)


# Ket Qua xo so
@bot.message_handler(commands=['kqxs'])
def kqxs(message):
    kqxs_1 = link.kqxs_mb()
    bot.reply_to(message, kqxs_1)


# cute
@bot.message_handler(commands=['cat'])
def cats(message):
    a = link.cat()
    bot.send_photo(message.chat.id, a)


@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.send_message(m.chat.id,f"{choices(link.reply.reply_name)[0]}")
    time.sleep(1)


if __name__ == "__main__":
    bot.polling(none_stop=True, timeout= 10)