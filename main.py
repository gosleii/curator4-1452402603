import telebot

bot = telebot.TeleBot("7242541800:AAG4e7pfIO7YI2Qi3nCvj9Q6di97m7SHt9E")


@bot.message_handler(commands=["lets_start"])
def start_handler(message):
    bot.send_message(message.chat.id, "hello world")


@bot.message_handler(commands=["newcommand"])
def start_handler(message):
    bot.send_message(message.chat.id, "[I want sleep](https://t.me/urikalegenda)", parse_mode="Markdown")


@bot.message_handler(commands=["the_wather_in_crimea"])
def start_handler(message):
    bot.send_message(message.chat.id, "погода в Крыму прекрасная, температура +50, все как мы любим")


bot.infinity_polling()