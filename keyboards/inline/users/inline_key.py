# - *- coding: utf- 8 - *-

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(
    text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
start.add(but_1)


moves = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(
    text='♻️ Обновить', callback_data="♻️ Обновить")
but_2 = types.InlineKeyboardButton(
    text='Перевести деньги', callback_data="Перевести деньги")
but_3 = types.InlineKeyboardButton(
    text='Удалить кошелек', callback_data="Удалить кошелек")
but_4 = types.InlineKeyboardButton(
    text='Изменить данные', callback_data="Изменить данные")
but_5 = types.InlineKeyboardButton(
    text='Назад', callback_data="Назад")
moves.add(but_2)
moves.add(but_3)
moves.add(but_4)
moves.add(but_1, but_5)
