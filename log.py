import telebot
import os
import csv
from datetime import datetime

bot = telebot.TeleBot("7577691917:AAEniJn3L7vs9XTa0s2M5G4z4LKnJ2UXfS0")

DATA_FOLDER = "data"
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

log_steps = {}

def get_transaction_file(user_id):
    return os.path.join(DATA_FOLDER, f"{user_id}_transactions.csv")


@bot.message_handler(commands=['log'])
def log_start(message):
    log_steps[message.chat.id] = {'step': 'type'}
    bot.send_message(message.chat.id, "What type of transaction?\nType `income` or `expense`:")

@bot.message_handler(func=lambda msg: msg.chat.id in log_steps)
def log_handler(message):
    user_id = message.chat.id
    step_data = log_steps[user_id]

    
    if step_data['step'] == 'type':
        if message.text.lower() not in ['income', 'expense']:
            bot.send_message(user_id, "Please type `income` or `expense`.")
            return
        step_data['type'] = message.text.lower()
        step_data['step'] = 'category'
        bot.send_message(user_id, "Enter the *category* (e.g. salary, food, rent):")
        return

   
    if step_data['step'] == 'category':
        step_data['category'] = message.text
        step_data['step'] = 'amount'
        bot.send_message(user_id, "Enter the *amount* (only number):")
        return

  
    if step_data['step'] == 'amount':
        try:
            amount = float(message.text)
            step_data['amount'] = amount
            step_data['step'] = 'done'

           
            file_path = get_transaction_file(user_id)
            with open(file_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([
                    step_data['type'],
                    step_data['category'],
                    step_data['amount'],
                    datetime.now().strftime("%Y-%m-%d %H:%M")
                ])

            bot.send_message(user_id, f"Logged: {step_data['type']} - {step_data['category']} - {step_data['amount']}₸")
            log_steps.pop(user_id)
        except:
            bot.send_message(user_id, "Please enter a valid number.")

@bot.message_handler(commands=['summary'])
def summary_handler(message):
    user_id = message.chat.id
    file_path = os.path.join(DATA_FOLDER, f"{user_id}_transactions.csv")

    if not os.path.exists(file_path):
        bot.send_message(user_id, "No data yet.")
        return

    income = 0
    expense = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for row in csv.reader(file):
            if row[0] == 'income':
                income += float(row[2])
            elif row[0] == 'expense':
                expense += float(row[2])

    balance = income - expense

    bot.send_message(user_id, f"Summary:\nIncome: {income}₸\nExpense: {expense}₸\nBalance: {balance}₸")
    
bot.polling(none_stop=True)    
