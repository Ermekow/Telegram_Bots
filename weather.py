import requests
import json
import aiogram


open_weather_api = '5006304cfaafa91b7d3a288ccbd08aa9'
tb_token = '5083353059:AAERl6ogvqCEUomxgQ3rEkjTOg-o51kidVc'

bot = aiogram.Bot(token=tb_token)
dp = aiogram.Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: aiogram.types.Message):
    await message.reply('привет,напиши город чтобы узнать погоду')

@dp.message_handler()
async def get_weather(message: aiogram.types.Message):

    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q'
                 f'={message.text}&appid'
                 f'={open_weather_api}&units=metric&lang=ru')

    data = r.json()
    country = data['name']
    temp = data['main']['temp']
    weather = data['weather'][0]['main']
    wind = data['wind']['speed']

    await  message.reply(f'Погода в городе {country}, - {temp}, {weather}, Скорость ветра {wind}')

if __name__ == '__main__':
    aiogram.executor.start_polling(dp)

