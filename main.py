import telebot


from flask import Flask, request
import os

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

courses = {
    'Python': 'python.org',
    'JS': 'learn.javascript.ru',
}
python = {
    'print': 'python.org',
    'input': 'python.org',
}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ты выбрал команду старт' + str(message.chat))

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Доступные команды: \n /help \n /start \n /courses')

@bot.message_handler(commands=['courses'])
def courses_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    for item in courses:
        url_button = telebot.types.InlineKeyboardButton(text=item, url=courses[item])
        keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Доступные курсы:', reply_markup=keyboard)

@bot.message_handler(commands=['python'])
def courses_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    for item in python:
        url_button = telebot.types.InlineKeyboardButton(text=item, url=python[item])
        keyboard.add(url_button)
    bot.send_message(message.chat.id, 'Доступные курсы:', reply_markup=keyboard)


@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot 29-05-2021", 200


@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='https://aternum.herokuapp.com/' + TOKEN)
    return "Python Telegram Bot", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))