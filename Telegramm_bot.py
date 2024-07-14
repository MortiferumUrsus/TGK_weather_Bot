import os
import telebot
from get_weather_selen import make_immage

TOKEN = '7041608618:AAEjeXmonWdL0algn73OiTBMVsgCytXj9Aw'
bot = telebot.TeleBot(TOKEN)
channel_id = '@Stepan_weather'

def make_post(url, city):
    make_immage(url, city)
    post_text = f'Погода в {city} на сегодня'
    image_path = f'saved_images/cropped_screenshot_{city}.png'
    with open(image_path, 'rb') as image_file:
        bot.send_photo(channel_id, image_file, caption=post_text)
    os.remove(f"saved_images/cropped_screenshot_{city}.png")
    os.remove(f"saved_images/full_screenshot_{city}.png")

def every_day_post():
    url_Moscow = 'https://www.gismeteo.by/weather-moscow-4368/'
    url_Zvenigorod = 'https://www.gismeteo.by/weather-zvenigorod-11444/'
    url_Podolsk = 'https://www.gismeteo.by/weather-podolsk-11955/'
    make_post(url_Moscow, 'Москве')
    make_post(url_Zvenigorod, 'Звенигороде')
    make_post(url_Podolsk, 'Подольске')
