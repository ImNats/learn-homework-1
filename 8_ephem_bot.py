"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def ask_planet(update, context):
    text = '''Классно!!! Расположение какой планеты ты хочешь узнать?
    Вот какие планеты я знаю:
        Mercury
        Venus
        Mars
        Jupiter
        Saturn
        Uranus
        Neptune
        Pluto
        Sun
        Moon
    Введи в отчет название планеты на английском языке '''
    update.message.reply_text(text)


def find_planet(update, context):
    user_planet = update.message.text
    planet_not_found = False

    if user_planet == 'Mercury':
        planet_id=ephem.Mercury('2022/09/19')
    elif user_planet == 'Venus':
        planet_id=ephem.Venus('2022/09/19')
    elif user_planet == 'Mars':
        planet_id=ephem.Mars('2022/09/19')
    elif user_planet == 'Jupiter':
        planet_id=ephem.Jupiter('2022/09/19')
    elif user_planet == 'Saturn':
        planet_id=ephem.Saturn('2022/09/19')
    elif user_planet == 'Uranus':
        planet_id=ephem.Uranus('2022/09/19')
    elif user_planet == 'Neptune':
        planet_id=ephem.Neptune('2022/09/19')
    elif user_planet == 'Pluto':
        planet_id=ephem.Pluto('2022/09/19')
    elif user_planet == 'Sun':
        planet_id=ephem.Sun('2022/09/19')
    elif user_planet == 'Moon':
        planet_id=ephem.Moon('2022/09/19')
    else:
        planet_not_found = True

    if planet_not_found:
        text_to_user = 'Попробуй еще раз, я тебя не понял'
    else:
        text_to_user = 'Она была в созвездии '+ephem.constellation(planet_id)[1]

    return text_to_user


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", ask_planet))
    dp.add_handler(MessageHandler(Filters.text, find_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
