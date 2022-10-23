from data.light import LightController
import data.link as link
import telebot
import config
from data.datetime import local_now
from logger import init_logger


logger = init_logger()


bot = telebot.TeleBot(f"{config.TELEGRAM_BOT_TOKEN}", parse_mode= None)
light_controller = LightController(api=config.LIGHT_API)


# start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    now = local_now()
    start_help = f""" \n
    Chào {message.from_user.full_name}, đây là bot tự động của Trung, chúc bạn có một ngày mới vui vẻ.
    Bây giờ là: {now}
    Gọi hỗ trợ lệnh hãy bấm /help.
    /bxh :   Cập nhật BXH top 10 mới nhất NHA.
    /kqxs:   Kết quả xổ số miền Bắc hôm nay.
    /cat :   Kêu gọi meow meow
    /on :   Bật đèn
    /off :   Tắt  đèn
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


@bot.message_handler(commands=['on'])
def turn_on(message):
    try:
        light_controller.turn_on()
    except Exception as e:
        msg = "Có lỗi xảy ra khi bật đèn"
        bot.reply_to(message, f"Error: {msg}")
        logger.exception("Turn On Error: %s", e)
    else:
        bot.reply_to(message, "Đã bật đèn")


@bot.message_handler(commands=['off'])
def turn_off(message):
    try:
        light_controller.turn_off()
    except Exception as e:
        msg = "Có lỗi xảy ra khi tắt đèn"
        bot.reply_to(message, f"Error: {msg}")
        logger.exception("Turn Off Error: %s", e)
    else:
        bot.reply_to(message, "Đã tắt đèn")


if __name__ == "__main__":
    logger.info("Bot started")
    bot.polling(none_stop=True, timeout= 10)