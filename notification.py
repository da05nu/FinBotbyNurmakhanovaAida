import telebot

bot = telebot.TeleBot("7577691917:AAEniJn3L7vs9XTa0s2M5G4z4LKnJ2UXfS0")

import threading
import time

notified_users = set()  

@bot.message_handler(commands=['notifyon'])
def notify_on(message):
    user_id = message.chat.id
    if user_id not in notified_users:
        notified_users.add(user_id)
        bot.send_message(user_id, "Notifications turned ON.")
    else:
        bot.send_message(user_id, "Notifications already ON.")

@bot.message_handler(commands=['notioff'])
def noti_off(message):
    user_id = message.chat.id
    if user_id in notified_users:
        notified_users.remove(user_id)
        bot.send_message(user_id, "Notifications turned OFF.")
    else:
        bot.send_message(user_id, "Notifications already OFF.")

bot.polling(none_stop=True)  



