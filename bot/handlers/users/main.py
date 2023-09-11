# - *- coding: utf- 8 - *-

import random
import hashlib
import datetime
from time import sleep

import aiogram
from SimpleQIWI import *
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle

from data import db
from loader import dp
from keyboards.inline.users.inline_key import start
from states.main import New_Number, New_Token, Send_Money
from keyboards.default.users.default_key import start_button, stop, decision


@dp.message_handler(commands=["info"])
async def help_command(message: types.Message):
    await dp.bot.send_message(message.chat.id, '<a><i>Внимание! Этот проект создан для упрощения работы с API Qiwi. Бот представляет из себя более улучшенную и удобную версию взаимодействия с интернет-кошельком. Данные, которые вы вводите для добавления кошелька должны быть исключительно вашими. Использование чужих данных для взаимодействия с кошельком - является противозаконным.</i>\n\nРазработчик: @por0vos1k\nПроект на Github - <a href="https://github.com/famaxth/Qiwi-Bot">ссылка</a></a>', parse_mode='HTML', reply_markup=start_button)


@dp.message_handler()
async def main(message):
    if message.text == "F.A.Q":
        await dp.bot.send_message(message.chat.id, '<a><i>Внимание! Этот проект создан для упрощения работы с API Qiwi. Бот представляет из себя более улучшенную и удобную версию взаимодействия с интернет-кошельком. Данные, которые вы вводите для добавления кошелька должны быть исключительно вашими. Использование чужих данных для взаимодействия с кошельком - является противозаконным.</i>\n\nРазработчик: @por0vos1k\nПроект на Github - <a href="https://github.com/famaxth/Qiwi-Bot">ссылка</a></a>', parse_mode='HTML')
    else:
        number = int((db.return_numbers(message.chat.id))['numbers'])
        if number == 0:
            await dp.bot.send_message(message.chat.id, "У вас еще нет активированных кошельков.", reply_markup=start)
        else:
            number = int((db.return_numbers(message.chat.id))['numbers'])
            if number == 0:
                await dp.bot.send_message(message.chat.id, "У вас еще нет активированных кошельков.", reply_markup=start)
            else:
                count = int((db.return_user_numbers(
                    message.chat.id))['COUNT(*)'])
                if count == 1:
                    result = db.return_all_info(message.chat.id)
                    number_1 = result[0]['number']
                    keyboard = types.InlineKeyboardMarkup()
                    but_1 = types.InlineKeyboardButton(
                        text=f'{number_1}', callback_data=f'{number_1}')
                    but_2 = types.InlineKeyboardButton(
                        text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
                    keyboard.add(but_1)
                    keyboard.add(but_2)
                    await dp.bot.send_message(message.chat.id, "Ваши кошельки:", reply_markup=keyboard)
                elif count == 2:
                    result = db.return_all_info(message.chat.id)
                    number_1 = result[0]['number']
                    number_2 = result[1]['number']
                    keyboard = types.InlineKeyboardMarkup()
                    but_1 = types.InlineKeyboardButton(
                        text=f'{number_1}', callback_data=f'{number_1}')
                    but_2 = types.InlineKeyboardButton(
                        text=f'{number_2}', callback_data=f'{number_2}')
                    but_3 = types.InlineKeyboardButton(
                        text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
                    keyboard.add(but_1)
                    keyboard.add(but_2)
                    keyboard.add(but_3)
                    await dp.bot.send_message(message.chat.id, "Ваши кошельки:", reply_markup=keyboard)
                elif count == 3:
                    result = db.return_all_info(message.chat.id)
                    number_1 = result[0]['number']
                    number_2 = result[1]['number']
                    number_3 = result[2]['number']
                    keyboard = types.InlineKeyboardMarkup()
                    but_1 = types.InlineKeyboardButton(
                        text=f'{number_1}', callback_data=f'{number_1}')
                    but_2 = types.InlineKeyboardButton(
                        text=f'{number_2}', callback_data=f'{number_2}')
                    but_3 = types.InlineKeyboardButton(
                        text=f'{number_3}', callback_data=f'{number_3}')
                    but_4 = types.InlineKeyboardButton(
                        text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
                    keyboard.add(but_1)
                    keyboard.add(but_2)
                    keyboard.add(but_3)
                    keyboard.add(but_4)
                    await dp.bot.send_message(message.chat.id, "Ваши кошельки:", reply_markup=keyboard)
                elif count == 4:
                    result = db.return_all_info(message.chat.id)
                    number_1 = result[0]['number']
                    number_2 = result[1]['number']
                    number_3 = result[2]['number']
                    number_4 = result[3]['number']
                    keyboard = types.InlineKeyboardMarkup()
                    but_1 = types.InlineKeyboardButton(
                        text=f'{number_1}', callback_data=f'{number_1}')
                    but_2 = types.InlineKeyboardButton(
                        text=f'{number_2}', callback_data=f'{number_2}')
                    but_3 = types.InlineKeyboardButton(
                        text=f'{number_3}', callback_data=f'{number_3}')
                    but_4 = types.InlineKeyboardButton(
                        text=f'{number_4}', callback_data=f'{number_4}')
                    but_5 = types.InlineKeyboardButton(
                        text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
                    keyboard.add(but_1)
                    keyboard.add(but_2)
                    keyboard.add(but_3)
                    keyboard.add(but_4)
                    keyboard.add(but_5)
                    await dp.bot.send_message(message.chat.id, "Ваши кошельки:", reply_markup=keyboard)
                elif count == 5:
                    result = db.return_all_info(message.chat.id)
                    number_1 = result[0]['number']
                    number_2 = result[1]['number']
                    number_3 = result[2]['number']
                    number_4 = result[3]['number']
                    number_5 = result[4]['number']
                    keyboard = types.InlineKeyboardMarkup()
                    but_1 = types.InlineKeyboardButton(
                        text=f'{number_1}', callback_data=f'{number_1}')
                    but_2 = types.InlineKeyboardButton(
                        text=f'{number_2}', callback_data=f'{number_2}')
                    but_3 = types.InlineKeyboardButton(
                        text=f'{number_3}', callback_data=f'{number_3}')
                    but_4 = types.InlineKeyboardButton(
                        text=f'{number_4}', callback_data=f'{number_4}')
                    but_5 = types.InlineKeyboardButton(
                        text=f'{number_5}', callback_data=f'{number_5}')
                    but_6 = types.InlineKeyboardButton(
                        text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
                    keyboard.add(but_1)
                    keyboard.add(but_2)
                    keyboard.add(but_3)
                    keyboard.add(but_4)
                    keyboard.add(but_5)
                    keyboard.add(but_6)
                    await dp.bot.send_message(message.chat.id, "Ваши кошельки:", reply_markup=keyboard)
                elif count == 6:
                    result = db.return_all_info(message.chat.id)
                    number_1 = result[0]['number']
                    number_2 = result[1]['number']
                    number_3 = result[2]['number']
                    number_4 = result[3]['number']
                    number_5 = result[4]['number']
                    number_6 = result[5]['number']
                    keyboard = types.InlineKeyboardMarkup()
                    but_1 = types.InlineKeyboardButton(
                        text=f'{number_1}', callback_data=f'{number_1}')
                    but_2 = types.InlineKeyboardButton(
                        text=f'{number_2}', callback_data=f'{number_2}')
                    but_3 = types.InlineKeyboardButton(
                        text=f'{number_3}', callback_data=f'{number_3}')
                    but_4 = types.InlineKeyboardButton(
                        text=f'{number_4}', callback_data=f'{number_4}')
                    but_5 = types.InlineKeyboardButton(
                        text=f'{number_5}', callback_data=f'{number_5}')
                    but_6 = types.InlineKeyboardButton(
                        text=f'{number_6}', callback_data=f'{number_6}')
                    but_7 = types.InlineKeyboardButton(
                        text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
                    keyboard.add(but_1)
                    keyboard.add(but_2)
                    keyboard.add(but_3)
                    keyboard.add(but_4)
                    keyboard.add(but_5)
                    keyboard.add(but_6)
                    keyboard.add(but_7)
                    await dp.bot.send_message(message.chat.id, "Ваши кошельки:", reply_markup=keyboard)
                elif count == 7:
                    result = db.return_all_info(message.chat.id)
                    number_1 = result[0]['number']
                    number_2 = result[1]['number']
                    number_3 = result[2]['number']
                    number_4 = result[3]['number']
                    number_5 = result[4]['number']
                    number_6 = result[5]['number']
                    number_7 = result[6]['number']
                    keyboard = types.InlineKeyboardMarkup()
                    but_1 = types.InlineKeyboardButton(
                        text=f'{number_1}', callback_data=f'{number_1}')
                    but_2 = types.InlineKeyboardButton(
                        text=f'{number_2}', callback_data=f'{number_2}')
                    but_3 = types.InlineKeyboardButton(
                        text=f'{number_3}', callback_data=f'{number_3}')
                    but_4 = types.InlineKeyboardButton(
                        text=f'{number_4}', callback_data=f'{number_4}')
                    but_5 = types.InlineKeyboardButton(
                        text=f'{number_5}', callback_data=f'{number_5}')
                    but_6 = types.InlineKeyboardButton(
                        text=f'{number_6}', callback_data=f'{number_6}')
                    but_7 = types.InlineKeyboardButton(
                        text=f'{number_7}', callback_data=f'{number_7}')
                    but_8 = types.InlineKeyboardButton(
                        text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
                    keyboard.add(but_1)
                    keyboard.add(but_2)
                    keyboard.add(but_3)
                    keyboard.add(but_4)
                    keyboard.add(but_5)
                    keyboard.add(but_6)
                    keyboard.add(but_7)
                    keyboard.add(but_8)
                    await dp.bot.send_message(message.chat.id, "Ваши кошельки:", reply_markup=keyboard)
                elif count == 8:
                    result = db.return_all_info(message.chat.id)
                    number_1 = result[0]['number']
                    number_2 = result[1]['number']
                    number_3 = result[2]['number']
                    number_4 = result[3]['number']
                    number_5 = result[4]['number']
                    number_6 = result[5]['number']
                    number_7 = result[6]['number']
                    number_8 = result[7]['number']
                    keyboard = types.InlineKeyboardMarkup()
                    but_1 = types.InlineKeyboardButton(
                        text=f'{number_1}', callback_data=f'{number_1}')
                    but_2 = types.InlineKeyboardButton(
                        text=f'{number_2}', callback_data=f'{number_2}')
                    but_3 = types.InlineKeyboardButton(
                        text=f'{number_3}', callback_data=f'{number_3}')
                    but_4 = types.InlineKeyboardButton(
                        text=f'{number_4}', callback_data=f'{number_4}')
                    but_5 = types.InlineKeyboardButton(
                        text=f'{number_5}', callback_data=f'{number_5}')
                    but_6 = types.InlineKeyboardButton(
                        text=f'{number_6}', callback_data=f'{number_6}')
                    but_7 = types.InlineKeyboardButton(
                        text=f'{number_7}', callback_data=f'{number_7}')
                    but_8 = types.InlineKeyboardButton(
                        text=f'{number_8}', callback_data=f'{number_8}')
                    but_9 = types.InlineKeyboardButton(
                        text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
                    keyboard.add(but_1)
                    keyboard.add(but_2)
                    keyboard.add(but_3)
                    keyboard.add(but_4)
                    keyboard.add(but_5)
                    keyboard.add(but_6)
                    keyboard.add(but_7)
                    keyboard.add(but_8)
                    keyboard.add(but_9)
                    await dp.bot.send_message(message.chat.id, "Ваши кошельки:", reply_markup=keyboard)
                elif count == 9:
                    result = db.return_all_info(message.chat.id)
                    number_1 = result[0]['number']
                    number_2 = result[1]['number']
                    number_3 = result[2]['number']
                    number_4 = result[3]['number']
                    number_5 = result[4]['number']
                    number_6 = result[5]['number']
                    number_7 = result[6]['number']
                    number_8 = result[7]['number']
                    number_9 = result[8]['number']
                    keyboard = types.InlineKeyboardMarkup()
                    but_1 = types.InlineKeyboardButton(
                        text=f'{number_1}', callback_data=f'{number_1}')
                    but_2 = types.InlineKeyboardButton(
                        text=f'{number_2}', callback_data=f'{number_2}')
                    but_3 = types.InlineKeyboardButton(
                        text=f'{number_3}', callback_data=f'{number_3}')
                    but_4 = types.InlineKeyboardButton(
                        text=f'{number_4}', callback_data=f'{number_4}')
                    but_5 = types.InlineKeyboardButton(
                        text=f'{number_5}', callback_data=f'{number_5}')
                    but_6 = types.InlineKeyboardButton(
                        text=f'{number_6}', callback_data=f'{number_6}')
                    but_7 = types.InlineKeyboardButton(
                        text=f'{number_7}', callback_data=f'{number_7}')
                    but_8 = types.InlineKeyboardButton(
                        text=f'{number_8}', callback_data=f'{number_8}')
                    but_9 = types.InlineKeyboardButton(
                        text=f'{number_9}', callback_data=f'{number_9}')
                    but_10 = types.InlineKeyboardButton(
                        text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
                    keyboard.add(but_1)
                    keyboard.add(but_2)
                    keyboard.add(but_3)
                    keyboard.add(but_4)
                    keyboard.add(but_5)
                    keyboard.add(but_6)
                    keyboard.add(but_7)
                    keyboard.add(but_8)
                    keyboard.add(but_9)
                    keyboard.add(but_10)
                    await dp.bot.send_message(message.chat.id, "Ваши кошельки:", reply_markup=keyboard)
                elif count == 10:
                    result = db.return_all_info(message.chat.id)
                    number_1 = result[0]['number']
                    number_2 = result[1]['number']
                    number_3 = result[2]['number']
                    number_4 = result[3]['number']
                    number_5 = result[4]['number']
                    number_6 = result[5]['number']
                    number_7 = result[6]['number']
                    number_8 = result[7]['number']
                    number_9 = result[8]['number']
                    number_10 = result[9]['number']
                    keyboard = types.InlineKeyboardMarkup()
                    but_1 = types.InlineKeyboardButton(
                        text=f'{number_1}', callback_data=f'{number_1}')
                    but_2 = types.InlineKeyboardButton(
                        text=f'{number_2}', callback_data=f'{number_2}')
                    but_3 = types.InlineKeyboardButton(
                        text=f'{number_3}', callback_data=f'{number_3}')
                    but_4 = types.InlineKeyboardButton(
                        text=f'{number_4}', callback_data=f'{number_4}')
                    but_5 = types.InlineKeyboardButton(
                        text=f'{number_5}', callback_data=f'{number_5}')
                    but_6 = types.InlineKeyboardButton(
                        text=f'{number_6}', callback_data=f'{number_6}')
                    but_7 = types.InlineKeyboardButton(
                        text=f'{number_7}', callback_data=f'{number_7}')
                    but_8 = types.InlineKeyboardButton(
                        text=f'{number_8}', callback_data=f'{number_8}')
                    but_9 = types.InlineKeyboardButton(
                        text=f'{number_9}', callback_data=f'{number_9}')
                    but_10 = types.InlineKeyboardButton(
                        text=f'{number_10}', callback_data=f'{number_10}')
                    but_11 = types.InlineKeyboardButton(
                        text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
                    keyboard.add(but_1)
                    keyboard.add(but_2)
                    keyboard.add(but_3)
                    keyboard.add(but_4)
                    keyboard.add(but_5)
                    keyboard.add(but_6)
                    keyboard.add(but_7)
                    keyboard.add(but_8)
                    keyboard.add(but_9)
                    keyboard.add(but_10)
                    keyboard.add(but_11)
                    await dp.bot.send_message(message.chat.id, "Ваши кошельки:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == '🌀 Добавить номер 🌀', state=None)
async def add_number_1(call: types.CallbackQuery, state: FSMContext):
    number = int((db.return_numbers(call.message.chat.id))['numbers'])
    if number < 10:
        await dp.bot.send_message(call.message.chat.id, "Введите номер в международном формате и без +", reply_markup=stop)
        await New_Number.Q1.set()
    else:
        await dp.bot.send_message(call.message.chat.id, "Вы уже добавили максимально возможное количество кошельков. Удалите один из них для того, чтобы добавить новый.", reply_markup=start_button)


@dp.callback_query_handler(lambda c: c.data == 'Назад', state=None)
async def back(call: types.CallbackQuery, state: FSMContext):
    number = int((db.return_numbers(call.message.chat.id))['numbers'])
    if number == 0:
        await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="У вас еще нет активированных кошельков.", reply_markup=start)
    else:
        count = int((db.return_user_numbers(call.message.chat.id))['COUNT(*)'])
        if count == 1:
            result = db.return_all_info(call.message.chat.id)
            number_1 = result[0]['number']
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text=f'{number_1}', callback_data=f'{number_1}')
            but_2 = types.InlineKeyboardButton(
                text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
            keyboard.add(but_1)
            keyboard.add(but_2)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваши кошельки:", reply_markup=keyboard)
        elif count == 2:
            result = db.return_all_info(call.message.chat.id)
            number_1 = result[0]['number']
            number_2 = result[1]['number']
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text=f'{number_1}', callback_data=f'{number_1}')
            but_2 = types.InlineKeyboardButton(
                text=f'{number_2}', callback_data=f'{number_2}')
            but_3 = types.InlineKeyboardButton(
                text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
            keyboard.add(but_1)
            keyboard.add(but_2)
            keyboard.add(but_3)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваши кошельки:", reply_markup=keyboard)
        elif count == 3:
            result = db.return_all_info(call.message.chat.id)
            number_1 = result[0]['number']
            number_2 = result[1]['number']
            number_3 = result[2]['number']
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text=f'{number_1}', callback_data=f'{number_1}')
            but_2 = types.InlineKeyboardButton(
                text=f'{number_2}', callback_data=f'{number_2}')
            but_3 = types.InlineKeyboardButton(
                text=f'{number_3}', callback_data=f'{number_3}')
            but_4 = types.InlineKeyboardButton(
                text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
            keyboard.add(but_1)
            keyboard.add(but_2)
            keyboard.add(but_3)
            keyboard.add(but_4)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваши кошельки:", reply_markup=keyboard)
        elif count == 4:
            result = db.return_all_info(call.message.chat.id)
            number_1 = result[0]['number']
            number_2 = result[1]['number']
            number_3 = result[2]['number']
            number_4 = result[3]['number']
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text=f'{number_1}', callback_data=f'{number_1}')
            but_2 = types.InlineKeyboardButton(
                text=f'{number_2}', callback_data=f'{number_2}')
            but_3 = types.InlineKeyboardButton(
                text=f'{number_3}', callback_data=f'{number_3}')
            but_4 = types.InlineKeyboardButton(
                text=f'{number_4}', callback_data=f'{number_4}')
            but_5 = types.InlineKeyboardButton(
                text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
            keyboard.add(but_1)
            keyboard.add(but_2)
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_5)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваши кошельки:", reply_markup=keyboard)
        elif count == 5:
            result = db.return_all_info(call.message.chat.id)
            number_1 = result[0]['number']
            number_2 = result[1]['number']
            number_3 = result[2]['number']
            number_4 = result[3]['number']
            number_5 = result[4]['number']
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text=f'{number_1}', callback_data=f'{number_1}')
            but_2 = types.InlineKeyboardButton(
                text=f'{number_2}', callback_data=f'{number_2}')
            but_3 = types.InlineKeyboardButton(
                text=f'{number_3}', callback_data=f'{number_3}')
            but_4 = types.InlineKeyboardButton(
                text=f'{number_4}', callback_data=f'{number_4}')
            but_5 = types.InlineKeyboardButton(
                text=f'{number_5}', callback_data=f'{number_5}')
            but_6 = types.InlineKeyboardButton(
                text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
            keyboard.add(but_1)
            keyboard.add(but_2)
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_5)
            keyboard.add(but_6)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваши кошельки:", reply_markup=keyboard)
        elif count == 6:
            result = db.return_all_info(call.message.chat.id)
            number_1 = result[0]['number']
            number_2 = result[1]['number']
            number_3 = result[2]['number']
            number_4 = result[3]['number']
            number_5 = result[4]['number']
            number_6 = result[5]['number']
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text=f'{number_1}', callback_data=f'{number_1}')
            but_2 = types.InlineKeyboardButton(
                text=f'{number_2}', callback_data=f'{number_2}')
            but_3 = types.InlineKeyboardButton(
                text=f'{number_3}', callback_data=f'{number_3}')
            but_4 = types.InlineKeyboardButton(
                text=f'{number_4}', callback_data=f'{number_4}')
            but_5 = types.InlineKeyboardButton(
                text=f'{number_5}', callback_data=f'{number_5}')
            but_6 = types.InlineKeyboardButton(
                text=f'{number_6}', callback_data=f'{number_6}')
            but_7 = types.InlineKeyboardButton(
                text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
            keyboard.add(but_1)
            keyboard.add(but_2)
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_5)
            keyboard.add(but_6)
            keyboard.add(but_7)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваши кошельки:", reply_markup=keyboard)
        elif count == 7:
            result = db.return_all_info(call.message.chat.id)
            number_1 = result[0]['number']
            number_2 = result[1]['number']
            number_3 = result[2]['number']
            number_4 = result[3]['number']
            number_5 = result[4]['number']
            number_6 = result[5]['number']
            number_7 = result[6]['number']
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text=f'{number_1}', callback_data=f'{number_1}')
            but_2 = types.InlineKeyboardButton(
                text=f'{number_2}', callback_data=f'{number_2}')
            but_3 = types.InlineKeyboardButton(
                text=f'{number_3}', callback_data=f'{number_3}')
            but_4 = types.InlineKeyboardButton(
                text=f'{number_4}', callback_data=f'{number_4}')
            but_5 = types.InlineKeyboardButton(
                text=f'{number_5}', callback_data=f'{number_5}')
            but_6 = types.InlineKeyboardButton(
                text=f'{number_6}', callback_data=f'{number_6}')
            but_7 = types.InlineKeyboardButton(
                text=f'{number_7}', callback_data=f'{number_7}')
            but_8 = types.InlineKeyboardButton(
                text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
            keyboard.add(but_1)
            keyboard.add(but_2)
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_5)
            keyboard.add(but_6)
            keyboard.add(but_7)
            keyboard.add(but_8)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваши кошельки:", reply_markup=keyboard)
        elif count == 8:
            result = db.return_all_info(call.message.chat.id)
            number_1 = result[0]['number']
            number_2 = result[1]['number']
            number_3 = result[2]['number']
            number_4 = result[3]['number']
            number_5 = result[4]['number']
            number_6 = result[5]['number']
            number_7 = result[6]['number']
            number_8 = result[7]['number']
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text=f'{number_1}', callback_data=f'{number_1}')
            but_2 = types.InlineKeyboardButton(
                text=f'{number_2}', callback_data=f'{number_2}')
            but_3 = types.InlineKeyboardButton(
                text=f'{number_3}', callback_data=f'{number_3}')
            but_4 = types.InlineKeyboardButton(
                text=f'{number_4}', callback_data=f'{number_4}')
            but_5 = types.InlineKeyboardButton(
                text=f'{number_5}', callback_data=f'{number_5}')
            but_6 = types.InlineKeyboardButton(
                text=f'{number_6}', callback_data=f'{number_6}')
            but_7 = types.InlineKeyboardButton(
                text=f'{number_7}', callback_data=f'{number_7}')
            but_8 = types.InlineKeyboardButton(
                text=f'{number_8}', callback_data=f'{number_8}')
            but_9 = types.InlineKeyboardButton(
                text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
            keyboard.add(but_1)
            keyboard.add(but_2)
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_5)
            keyboard.add(but_6)
            keyboard.add(but_7)
            keyboard.add(but_8)
            keyboard.add(but_9)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваши кошельки:", reply_markup=keyboard)
        elif count == 9:
            result = db.return_all_info(call.message.chat.id)
            number_1 = result[0]['number']
            number_2 = result[1]['number']
            number_3 = result[2]['number']
            number_4 = result[3]['number']
            number_5 = result[4]['number']
            number_6 = result[5]['number']
            number_7 = result[6]['number']
            number_8 = result[7]['number']
            number_9 = result[8]['number']
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text=f'{number_1}', callback_data=f'{number_1}')
            but_2 = types.InlineKeyboardButton(
                text=f'{number_2}', callback_data=f'{number_2}')
            but_3 = types.InlineKeyboardButton(
                text=f'{number_3}', callback_data=f'{number_3}')
            but_4 = types.InlineKeyboardButton(
                text=f'{number_4}', callback_data=f'{number_4}')
            but_5 = types.InlineKeyboardButton(
                text=f'{number_5}', callback_data=f'{number_5}')
            but_6 = types.InlineKeyboardButton(
                text=f'{number_6}', callback_data=f'{number_6}')
            but_7 = types.InlineKeyboardButton(
                text=f'{number_7}', callback_data=f'{number_7}')
            but_8 = types.InlineKeyboardButton(
                text=f'{number_8}', callback_data=f'{number_8}')
            but_9 = types.InlineKeyboardButton(
                text=f'{number_9}', callback_data=f'{number_9}')
            but_10 = types.InlineKeyboardButton(
                text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
            keyboard.add(but_1)
            keyboard.add(but_2)
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_5)
            keyboard.add(but_6)
            keyboard.add(but_7)
            keyboard.add(but_8)
            keyboard.add(but_9)
            keyboard.add(but_10)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваши кошельки:", reply_markup=keyboard)
        elif count == 10:
            result = db.return_all_info(call.message.chat.id)
            number_1 = result[0]['number']
            number_2 = result[1]['number']
            number_3 = result[2]['number']
            number_4 = result[3]['number']
            number_5 = result[4]['number']
            number_6 = result[5]['number']
            number_7 = result[6]['number']
            number_8 = result[7]['number']
            number_9 = result[8]['number']
            number_10 = result[9]['number']
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text=f'{number_1}', callback_data=f'{number_1}')
            but_2 = types.InlineKeyboardButton(
                text=f'{number_2}', callback_data=f'{number_2}')
            but_3 = types.InlineKeyboardButton(
                text=f'{number_3}', callback_data=f'{number_3}')
            but_4 = types.InlineKeyboardButton(
                text=f'{number_4}', callback_data=f'{number_4}')
            but_5 = types.InlineKeyboardButton(
                text=f'{number_5}', callback_data=f'{number_5}')
            but_6 = types.InlineKeyboardButton(
                text=f'{number_6}', callback_data=f'{number_6}')
            but_7 = types.InlineKeyboardButton(
                text=f'{number_7}', callback_data=f'{number_7}')
            but_8 = types.InlineKeyboardButton(
                text=f'{number_8}', callback_data=f'{number_8}')
            but_9 = types.InlineKeyboardButton(
                text=f'{number_9}', callback_data=f'{number_9}')
            but_10 = types.InlineKeyboardButton(
                text=f'{number_10}', callback_data=f'{number_10}')
            but_11 = types.InlineKeyboardButton(
                text='🌀 Добавить номер 🌀', callback_data="🌀 Добавить номер 🌀")
            keyboard.add(but_1)
            keyboard.add(but_2)
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_5)
            keyboard.add(but_6)
            keyboard.add(but_7)
            keyboard.add(but_8)
            keyboard.add(but_9)
            keyboard.add(but_10)
            keyboard.add(but_11)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваши кошельки:", reply_markup=keyboard)


@dp.callback_query_handler(lambda call: True)
async def answer(call: types.CallbackQuery, state: FSMContext):
    if call.data[:3] == 'del':
        keyboard = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(
            text='Да', callback_data=f'yes{call.data[3:]}')
        but_2 = types.InlineKeyboardButton(
            text='Нет', callback_data="Нет")
        but_3 = types.InlineKeyboardButton(
            text='Вернуться назад', callback_data=f"back{call.data[3:]}")
        keyboard.add(but_1)
        keyboard.add(but_2)
        keyboard.add(but_3)
        await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы уверенны?", reply_markup=keyboard, parse_mode='HTML')
    elif call.data[:3] == 'yes':
        try:
            db.delete_number(call.message.chat.id, call.data[3:])
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🗑 Номер был успешно удален из базы.\n\nНажмите /start и вы попадете в меню взаимодействия с кошельками.", parse_mode='HTML')
        except:
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ошибка!")
    elif call.data[:4] == 'edit':
        await dp.bot.send_message(call.message.chat.id, "Введите новый токен:", reply_markup=stop)
        async with state.proxy() as data:
            data["number"] = call.data[4:]
        await New_Token.Q1.set()
    elif call.data[:4] == 'send':
        await dp.bot.send_message(call.message.chat.id, "Введите номер получателя:\n(в международном формате и без +)", reply_markup=stop)
        result = db.return_numbers_info(call.message.chat.id, call.data[4:])
        token = result["token"]
        async with state.proxy() as data:
            data["number"] = call.data[4:]
            data["token"] = token
        await Send_Money.Q1.set()
    elif call.data[:4] == 'back':
        result = db.return_numbers_info(call.message.chat.id, call.data[4:])
        date = result["date"]
        token = result["token"]
        number = result["number"]
        try:
            api = QApi(token=token, phone=number)
            balance = str(api.balance[0])
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text='♻️ Обновить', callback_data=call.data[4:])
            but_2 = types.InlineKeyboardButton(
                text='Перевести деньги', callback_data=f"send{call.data[4:]}")
            but_3 = types.InlineKeyboardButton(
                text='Удалить кошелек', callback_data=f"del{call.data[4:]}")
            but_4 = types.InlineKeyboardButton(
                text='Изменить данные', callback_data=f"edit{call.data[4:]}")
            but_5 = types.InlineKeyboardButton(
                text='Назад', callback_data="Назад")
            keyboard.add(but_2)
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_1, but_5)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<a><b>Статус -</b> <i>Работает ✅</i>\n\n<b>Номер:</b>  <i>{number}</i>\n<b>Баланс:</b>  <i>{balance}</i> ₽\n<b>Дата добавления:</b>  <i>{date}</i></a>", reply_markup=keyboard, parse_mode='HTML')
        except aiogram.utils.exceptions.MessageNotModified:
            pass
        except:
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text='♻️ Обновить', callback_data=call.data[4:])
            but_3 = types.InlineKeyboardButton(
                text='Удалить кошелек', callback_data=f"del{call.data[4:]}")
            but_4 = types.InlineKeyboardButton(
                text='Изменить данные', callback_data=f"edit{call.data[4:]}")
            but_5 = types.InlineKeyboardButton(
                text='Назад', callback_data="Назад")
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_1, but_5)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<a><b>Статус -</b> <i>Не работает ❌</i>\n\n<b>Номер:</b>  <i>{number}</i>\n<b>Дата добавления:</b>  <i>{date}</i></a>", reply_markup=keyboard, parse_mode='HTML')
    elif call.data == 'Нет':
        await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="❗️Вы отменили действие.\n\nНажмите /start и вы попадете в меню взаимодействия с кошельками.", parse_mode='HTML')
    else:
        result = db.return_numbers_info(call.message.chat.id, call.data)
        date = result["date"]
        token = result["token"]
        number = result["number"]
        try:
            api = QApi(token=token, phone=number)
            balance = str(api.balance[0])
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text='♻️ Обновить', callback_data=call.data)
            but_2 = types.InlineKeyboardButton(
                text='Перевести деньги', callback_data=f"send{call.data}")
            but_3 = types.InlineKeyboardButton(
                text='Удалить кошелек', callback_data=f"del{call.data}")
            but_4 = types.InlineKeyboardButton(
                text='Изменить данные', callback_data=f"edit{call.data}")
            but_5 = types.InlineKeyboardButton(
                text='Назад', callback_data="Назад")
            keyboard.add(but_2)
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_1, but_5)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<a><b>Статус -</b> <i>Работает ✅</i>\n\n<b>Номер:</b>  <i>{number}</i>\n<b>Баланс:</b>  <i>{balance}</i> ₽\n<b>Дата добавления:</b>  <i>{date}</i></a>", reply_markup=keyboard, parse_mode='HTML')
        except aiogram.utils.exceptions.MessageNotModified:
            pass
        except:
            keyboard = types.InlineKeyboardMarkup()
            but_1 = types.InlineKeyboardButton(
                text='♻️ Обновить', callback_data=call.data)
            but_3 = types.InlineKeyboardButton(
                text='Удалить кошелек', callback_data=f"del{call.data}")
            but_4 = types.InlineKeyboardButton(
                text='Изменить данные', callback_data=f"edit{call.data}")
            but_5 = types.InlineKeyboardButton(
                text='Назад', callback_data="Назад")
            keyboard.add(but_3)
            keyboard.add(but_4)
            keyboard.add(but_1, but_5)
            await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<a><b>Статус -</b> <i>Не работает ❌</i>\n\n<b>Номер:</b>  <i>{number}</i>\n<b>Дата добавления:</b>  <i>{date}</i></a>", reply_markup=keyboard, parse_mode='HTML')


@dp.message_handler(state=Send_Money.Q1)
async def send_money_1(message: types.Message, state: FSMContext):
    try:
        if message.text == "❌ Отмена":
            await dp.bot.send_message(message.chat.id, "📍 Вы отменили действие.", reply_markup=start_button)
            await state.finish()
        else:
            async with state.proxy() as data:
                data["account"] = f"+{message.text}"
            await dp.bot.send_message(message.chat.id, "Введите сумму:", reply_markup=stop)
            await Send_Money.Q2.set()
    except:
        await dp.bot.send_message(message.chat.id, "❌ Ошибка!", reply_markup=start_button)
        await state.finish()


@dp.message_handler(state=Send_Money.Q2)
async def send_money_2(message: types.Message, state: FSMContext):
    try:
        if message.text == "❌ Отмена":
            await dp.bot.send_message(message.chat.id, "📍 Вы отменили действие.", reply_markup=start_button)
            await state.finish()
        else:
            async with state.proxy() as data:
                data["amount"] = message.text
            await dp.bot.send_message(message.chat.id, "Вы уверенны?", reply_markup=decision)
            await Send_Money.Q3.set()
    except:
        await dp.bot.send_message(message.chat.id, "❌ Ошибка!", reply_markup=start_button)
        await state.finish()


@dp.message_handler(state=Send_Money.Q3)
async def send_money_3(message: types.Message, state: FSMContext):
    try:
        if message.text == "❌ Отмена" or message.text != "Да":
            await dp.bot.send_message(message.chat.id, "📍 Вы отменили действие.", reply_markup=start_button)
        else:
            async with state.proxy() as data:
                account = data["account"]
                amount = data["amount"]
                token = data["token"]
                number = data["number"]
            api = QApi(token=token, phone=number)
            api.pay(account=f"{account}", amount=f"{amount}")
            await dp.bot.send_message(message.chat.id, "✅ Деньги были успешно отправлены!", reply_markup=start_button)
        await state.finish()
    except Exception as e:
        print(e)
        await dp.bot.send_message(message.chat.id, "❌ Ошибка!", reply_markup=start_button)
        await state.finish()


@dp.message_handler(state=Send_Money.Q1)
async def send_money_1(message: types.Message, state: FSMContext):
    try:
        if message.text == "❌ Отмена":
            await dp.bot.send_message(message.chat.id, "📍 Вы отменили действие.", reply_markup=start_button)
        else:
            async with state.proxy() as data:
                data["account"] = message.text
            await dp.bot.send_message(message.chat.id, "Введите сумму:", reply_markup=start_button)
        await state.finish()
    except:
        await dp.bot.send_message(message.chat.id, "❌ Ошибка!", reply_markup=start_button)
        await state.finish()


@dp.message_handler(state=New_Token.Q1)
async def edit_token(message: types.Message, state: FSMContext):
    try:
        if message.text == "❌ Отмена":
            await dp.bot.send_message(message.chat.id, "📍 Вы отменили действие.", reply_markup=start_button)
        else:
            async with state.proxy() as data:
                number = data["number"]
            db.edit_token(message.text, number, message.chat.id)
            await dp.bot.send_message(message.chat.id, "✅ Токен был успешно изменён!\n\nНажмите /start и вы попадете в меню взаимодействия с кошельками.", reply_markup=start_button)
        await state.finish()
    except:
        await dp.bot.send_message(message.chat.id, "❌ Ошибка!", reply_markup=start_button)
        await state.finish()


@dp.message_handler(state=New_Number.Q1)
async def add_number_2(message: types.Message, state: FSMContext):
    try:
        if message.text == "❌ Отмена":
            await dp.bot.send_message(message.chat.id, "📍 Вы отменили действие.", reply_markup=start_button)
            await state.finish()
        else:
            async with state.proxy() as data:
                data["number"] = f"+{str(message.text)}"
            await dp.bot.send_message(message.chat.id, "Введите токен:", reply_markup=stop)
            await New_Number.Q2.set()
    except:
        await dp.bot.send_message(
            message.chat.id, "❌ Ошибка!", reply_markup=start_button)
        await state.finish()


@dp.message_handler(state=New_Number.Q2)
async def add_number_3(message: types.Message, state: FSMContext):
    if message.text == "❌ Отмена":
        await dp.bot.send_message(message.chat.id, "📍 Вы отменили действие.", reply_markup=start_button)
        await state.finish()
    else:
        try:
            async with state.proxy() as data:
                number = data["number"]
            token = message.text
            api = QApi(token=token, phone=number)
            today = datetime.datetime.now()
            date = today.strftime("%Y-%m-%d")
            db.add_number(message.chat.id, token, number, date)
            result = int((db.return_numbers(message.chat.id))['numbers'])
            numbers = result + 1
            db.update_user_numbers(numbers, message.chat.id)
            await dp.bot.send_message(message.chat.id, "✅ Номер был успешно добавлен!\n\nНажмите /start и вы попадете в меню взаимодействия с кошельками.", reply_markup=start_button)
            await state.finish()
        except:
            await dp.bot.send_message(
                message.chat.id, "❌ Ошибка!", reply_markup=start_button)
            await state.finish()
