from os import name
import requests
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



tg_bot_token = '5032227702:AAHNqAlV7b275O4q-fLa8WEFMj1EubL8n3s'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рик')
    item2 = types.KeyboardButton("Морти")
    item3 = types.KeyboardButton('Саммер')
    item4 = types.KeyboardButton("Бет")
    item5 = types.KeyboardButton('джерри')
    markup.add(item1,item2,item3,item4,item5)
    await message.reply(f"доброе утро , напишите имя героя", reply_markup=markup)
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await  message.reply('Привет\nэтот бот поможет узнать информацию о персонажей в мульти вселенной Рика и Морти\nнапиши команду /start что бы начать\nкогда начнешь внизу появится кнопки с именами героев\nвыбери одного из них и я дам тебе информацию о нем')

@dp.message_handler(content_types=['text'])
async def get_weather(message: types.Message):
    global data , name,gender,status,species
    if message.text =='Рик':
        r = requests.get(
            f'https://rickandmortyapi.com/api/character/1')
        data = r.json()
        name = data['name']
        statuis = data['status']
        species = data['species']
        gender = data['gender']
        imeg = data['image']
        button = InlineKeyboardMarkup(row_width=1)
        markup = InlineKeyboardButton(text="Фото" , url="https://rickandmortyapi.com/api/character/avatar/1.jpeg")
        button.add(markup)
        await message.reply(f"Имя : {name}\nСтатус : {statuis}\nВид : {species}\nПол : {gender}", reply_markup=button)

    if message.text =='Морти':
        r = requests.get(
        f'https://rickandmortyapi.com/api/character/2')
        data = r.json()
        name = data['name']
        statuis = data['status']
        species = data['species']
        gender = data['gender']
        imeg = data['image']
        button2 = InlineKeyboardMarkup(row_width=1)
        markup1 = InlineKeyboardButton(text="Фото", url="https://rickandmortyapi.com/api/character/avatar/2.jpeg")
        button2.add(markup1)
        await message.reply(f"Имя : {name}\nСтатус : {statuis}\nВид : {species}\nПол : {gender}", reply_markup=button2)
    if message.text =='Саммер':
        r = requests.get(
        f'https://rickandmortyapi.com/api/character/3')
        data = r.json()
        name = data['name']
        statuis = data['status']
        species = data['species']
        gender = data['gender']
        imeg = data['image']
        button3 = InlineKeyboardMarkup(row_width=1)
        markup2 = InlineKeyboardButton(text="Фото", url="https://rickandmortyapi.com/api/character/avatar/3.jpeg")
        button3.add(markup2)
        await message.reply(f"Имя : {name}\nСтатус : {statuis}\nВид : {species}\nПол : {gender}", reply_markup=button3)
    if message.text =='Бет':
        r = requests.get(
        f'https://rickandmortyapi.com/api/character/4')
        data = r.json()
        name = data['name']
        statuis = data['status']
        species = data['species']
        gender = data['gender']
        imeg = data['image']
        button5 = InlineKeyboardMarkup(row_width=1)
        markup3 = InlineKeyboardButton(text="Фото", url="https://rickandmortyapi.com/api/character/avatar/4.jpeg")
        button5.add(markup3)
        await message.reply(f"Имя : {name}\nСтатус : {statuis}\nВид : {species}\nПол : {gender}", reply_markup=button5)

    if message.text =='джерри':
        r = requests.get(
        f'https://rickandmortyapi.com/api/character/5')
        data = r.json()
        name = data['name']
        statuis = data['status']
        species = data['species']
        gender = data['gender']
        imeg = data['image']
        button6 = InlineKeyboardMarkup(row_width=1)
        markup4 = InlineKeyboardButton(text="Фото", url="https://rickandmortyapi.com/api/character/avatar/5.jpeg")
        button6.add(markup4)
        await message.reply(f"Имя : {name}\nСтатус : {statuis}\nВид : {species}\nПол : {gender}", reply_markup=button6)


   


            

executor.start_polling(dp)



