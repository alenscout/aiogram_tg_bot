from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
])

settings = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='YouTube' , url='https://youtube.com')]])
