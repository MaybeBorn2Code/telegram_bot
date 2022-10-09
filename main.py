import telebot
import urllib.request
import json
import time
import requests
import config
import random
from telebot import types
from telebot import util


bot = telebot.TeleBot('ENTER YOUR TOKEN!')
url: str = 'https://gogoanime.herokuapp.com/recent-release'
url_quote: str = 'https://animechan.vercel.app/api/quotes'


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.send_message(message.from_user.id, f'Hi, {message.from_user.first_name}!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    anime = types.KeyboardButton('Watch anime')
    quotes = types.KeyboardButton('Anime quotes')
    markup.add(anime, quotes)
    bot.send_message(message.chat.id, "Welcome to Watch & Read Anime ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    global data
    global counter
    if message.text == 'Watch anime':
        r: Response = requests.get(url)
        data = r.json()
        lst = []
        for i in data:
            lst.append(i['animeTitle'])
        markup = types.InlineKeyboardMarkup(row_width=1)
        counter = 0
        for button in sorted(lst):
            counter += 1
            markup.add(
                types.InlineKeyboardButton(text=str(counter) + '. ' + button, callback_data=str(counter)))
        bot.send_message(message.chat.id, 'Selection of available anime', reply_markup=markup)

    elif message.text == 'Anime quotes':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        more_button = types.KeyboardButton('More!')
        exit_button = types.KeyboardButton('Exit')
        response = requests.get(url_quote)
        data_json = json.loads(response.text)
        first_random = (data_json[random.randint(0, 5)])
        anime = f'Anime title:\n {first_random["anime"]}'
        character = f'Character:\n {first_random["character"]}'
        quote = f'Quote:\n {first_random["quote"]}'
        markup.add(more_button, exit_button)
        bot.send_message(message.from_user.id, anime, reply_markup=markup)
        bot.send_message(message.from_user.id, character, reply_markup=markup)
        bot.send_message(message.from_user.id, quote, reply_markup=markup)
        bot.send_message(message.chat.id, 'Select an action below', reply_markup=markup)

    elif message.text == 'More!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        more_button = types.KeyboardButton('More!')
        exit_button = types.KeyboardButton('Exit')
        response = requests.get("https://animechan.vercel.app/api/quotes")
        data_json = json.loads(response.text)
        first_random = (data_json[random.randint(0, 5)])
        anime = f'Anime title:\n {first_random["anime"]}'
        character = f'Character:\n {first_random["character"]}'
        quote = f'Quote:\n {first_random["quote"]}'
        markup.add(more_button, exit_button)
        bot.send_message(message.from_user.id, anime, reply_markup=markup)
        bot.send_message(message.from_user.id, character, reply_markup=markup)
        bot.send_message(message.from_user.id, quote, reply_markup=markup)
        bot.send_message(message.chat.id, 'Select an action below', reply_markup=markup)

    elif message.text == 'Select an episode':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        exit_button = types.KeyboardButton('Exit')
        markup.add(exit_button)
        lst = []
        for i in data:
            lst.append(i['episodeUrl'])
        sort_lst = sorted(lst)
        bot.send_message(message.chat.id, f'Only one episode available!')
        bot.send_message(message.chat.id, sort_lst[number], reply_markup=markup)

    elif message.text == 'Exit':
        bot.send_message(message.from_user.id, "Welcome to Watch & Read Anime ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        anime = types.KeyboardButton('Watch anime')
        quotes = types.KeyboardButton('Anime quotes')
        markup.add(anime, quotes)
        bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    global number
    lst_title = []
    for i in data:
        lst_title.append(i['animeTitle'])
    sort_lst_title = sorted(lst_title)

    if call.data == '1':
        number = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '2':
        number = 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '3':
        number = 2
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '4':
        number = 3
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '5':
        number = 4
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '6':
        number = 5
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '7':
        number = 6
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '8':
        number = 7
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '9':
        number = 8
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '10':
        number = 9
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '11':
        number = 10
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '12':
        number = 11
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '13':
        number = 12
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '14':
        number = 13
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '15':
        number = 14
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '16':
        number = 15
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '17':
        number = 16
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '18':
        number = 17
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '19':
        number = 18
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)

    elif call.data == '20':
        number = 19
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        series = types.KeyboardButton('Select an episode')
        markup.add(series)
        bot.send_message(call.message.chat.id, f"You're selected - {sort_lst_title[number]}", reply_markup=markup)


bot.polling(non_stop=True)
