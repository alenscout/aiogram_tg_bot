from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Каталог')],
#     [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
# ])

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Сервис', callback_data='service')],
                                             [InlineKeyboardButton(text='Команды', callback_data='commands')]])
