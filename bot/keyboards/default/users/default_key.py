# - *- coding: utf- 8 - *-

from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


start_button = ReplyKeyboardMarkup(resize_keyboard=True)
but_1 = KeyboardButton('F.A.Q')
start_button.add(but_1)


stop = ReplyKeyboardMarkup(resize_keyboard=True)
but_1 = KeyboardButton('❌ Отмена')
stop.add(but_1)


decision = ReplyKeyboardMarkup(resize_keyboard=True)
but_1 = KeyboardButton('Да')
but_2 = KeyboardButton('Нет')
decision.add(but_1)
decision.add(but_2)
