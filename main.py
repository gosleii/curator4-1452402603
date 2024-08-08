import telebot

bot = telebot.TeleBot("7240912162:AAGAc_U8zZfkO-xGD4Wp2_8_FoeWqx7aL8g")


@bot.message_handler(commands=['start'])
def main_1(message):
    bot.send_message(message.chat.id, "*привет! это бот, который поможет тебе в подготовке к егэ*",
                     parse_mode='Markdown')


@bot.message_handler(commands=['physics_exam_chanell'])
def main_2(message):
    bot.send_message(message.chat.id, "[*бесплатный * тгк преподавателя умскул по физике](https: // t.me / tesla_phys)", parse_mode='Markdown')

@bot.message_handler(commands=['math_exam_chanell'])
def main_3(message):
    bot.send_message(message.chat.id,
                     "[*бесплатный * тгк преподавателя умскул по математике](https: // t.me / art_matanit)", parse_mode='Markdown')

@bot.message_handler(commands=['rus_exam_chanell'])
def main_4(message):
    bot.send_message(message.chat.id,
                     "[*бесплатный * тгк преподавателя умскул по русскому языку](https: // t.me / dolgih_umrus)", parse_mode='Markdown')

@bot.message_handler(commands=['umschool_textbook'])
def main_5(message):
    bot.send_message(message.chat.id,
                     "[_учебник умскул по всем предметам_](https: // umschool.net / library / category / uchebnik /)", parse_mode='Markdown')



bot.infinity_polling()