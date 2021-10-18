from aiogram.dispatcher.filters.state import StatesGroup, State


class New_Number(StatesGroup):

    Q1 = State()
    Q2 = State()


class New_Token(StatesGroup):

    Q1 = State()


class Send_Money(StatesGroup):

    Q1 = State()
    Q2 = State()
    Q3 = State()
