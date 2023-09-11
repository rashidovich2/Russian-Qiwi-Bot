# - *- coding: utf- 8 - *-

import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from data import db
from loader import dp
from keyboards.inline.users.inline_key import start, moves
from keyboards.default.users.default_key import start_button


db.init_db()

with open("joined.txt", "r") as all_users_file:
    all_users = {line.strip() for line in all_users_file}


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if str(message.chat.id) not in all_users:
        first_name = str(message.from_user.first_name)
        last_name = str(message.from_user.last_name)
        user_id = int(message.chat.id)
        today = datetime.datetime.now()
        date = today.strftime("%Y-%m-%d")
        all_users_file = open("joined.txt", "a")
        all_users_file.write(str(message.chat.id) + "\n")
        all_users.add(str(message.chat.id))
        db.add_user(first_name, last_name, date, user_id, 0)
        await dp.bot.send_message(message.chat.id, "У вас еще нет активированных кошельков.", reply_markup=start)
        await dp.bot.send_message(message.chat.id, "ᅠ", reply_markup=start_button)
    else:
        number = int((db.return_numbers(message.chat.id))['numbers'])
        if number == 0:
            await dp.bot.send_message(message.chat.id, "У вас еще нет активированных кошельков.", reply_markup=start)
        else:
            count = int((db.return_user_numbers(message.chat.id))['COUNT(*)'])
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
