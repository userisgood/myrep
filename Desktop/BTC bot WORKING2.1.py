import telebot
import requests
from telebot import types
import datetime
token = "582019256:AAGi-KLHwhu8KBgTN-lYTybVZa_DoPEfy1A"
tb = telebot.TeleBot(token)


def get_time():
    URL = 'https://api.binance.com/api/v1/time'
    r = requests.get(URL).json()
    time = r['serverTime']
    return 'Дата и время: ' + datetime.datetime.fromtimestamp(int(time//1000)).strftime('%Y-%m-%d %H:%M:%S')
    
def courceeb():
    URL = 'https://api.binance.com/api/v1/trades?symbol=ETHBTC'
    r = requests.get(URL).json()
    price = r[-1]['price']
    return 'Курс '+ str(price)+' BTC за 1 эфир.'

@tb.message_handler(commands=['start'])
def say_hello(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton(text='/time')
    itembtn2 = types.KeyboardButton(text='/ethbtc')
    itembtn3 = types.KeyboardButton(text='/d')
    itembtn4 = types.KeyboardButton(text='/e')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    tb.send_message(message.chat.id, 'Привет! Я binance-бот, тыкни на кнопку, чтобы узнать интересующую информацию: /time - показывает дату и время сервера, /ethbtc - курc ETH/BTC, /d - выбирает букву d, /e - выбирает букву e.', reply_markup=markup) #, reply_markup=markup)

@tb.message_handler(commands=['time'])
def send_value1(message):
    tb.send_message(message.chat.id, get_time()) 

@tb.message_handler(commands=['ethbtc'])
def send_value(message):
    tb.send_message(message.chat.id, courceeb())   #, reply_markup=markup)

@tb.message_handler(commands=['d'])
def send_mesd(message):
    tb.send_message(message.chat.id, "Это буква d.")

@tb.message_handler(commands=['e'])
def send_mesd(message):
    tb.send_message(message.chat.id, "Это буква e.")



# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#    bot.reply_to(message, message.text)

tb.polling()
