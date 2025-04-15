import telebot

bot = telebot.TeleBot("7577691917:AAEniJn3L7vs9XTa0s2M5G4z4LKnJ2UXfS0")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Welcome to FinBot! Use /help for list of commands')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
            "/start - launching the FinBot\n" \
            "/hepl - list of commands\n" 
            "/log - expenses and income categories\n"
            "/config - configure income and budjet per category\n"
            "/summary - view balance and budjet summaries\n"
            "/notifyon - turn on the notifications\n"
            "/notioff - turn off the notifications"
    )               


bot.polling(none_stop=True) 