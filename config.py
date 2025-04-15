import telebot
import os
import json

bot = telebot.TeleBot("7577691917:AAEniJn3L7vs9XTa0s2M5G4z4LKnJ2UXfS0") 

DATA_FOLDER = "data"
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

user_steps = {}

def get_config_file(user_id):
    return os.path.join(DATA_FOLDER, f"{user_id}_config.json")


@bot.message_handler(commands=['config'])
def config_start(message):
    user_steps[message.chat.id] = {
        'step': 'income',
        'income': 0,
        'budgets': {}
    }
    bot.send_message(message.chat.id, "Please enter your *monthly income* (numbers only):")

@bot.message_handler(func=lambda msg: msg.chat.id in user_steps)
def handle_config_steps(message):
    user_id = message.chat.id
    step_info = user_steps[user_id]

    if step_info['step'] == 'income':
        try:
            income = float(message.text)
            step_info['income'] = income
            step_info['step'] = 'budgets'
            bot.send_message(user_id, "Now enter budgets like: `food 200` or `rent 300`\nSend `done` to finish.")
        except:
            bot.send_message(user_id, "Please enter a valid number for income.")

    elif step_info['step'] == 'budgets':
        if message.text.lower() == 'done':
            # Сохраняем данные
            config_path = get_config_file(user_id)
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(step_info, f, indent=2)
            user_steps.pop(user_id)
            bot.send_message(user_id, "Income and budgets saved!")
        else:
            try:
                category, amount = message.text.split()
                amount = float(amount)
                step_info['budgets'][category] = amount
                bot.send_message(user_id, f"Added: {category} — {amount}₸")
            except:
                bot.send_message(user_id, "Please use format: category amount (e.g. rent 300)")

bot.polling(none_stop=True) 