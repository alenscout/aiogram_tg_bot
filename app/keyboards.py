from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Каталог')],
#     [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
# ])

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Сервис', callback_data='service')],
                                             [InlineKeyboardButton(text='Команды', callback_data='commands')]])

services = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Onex', callback_data='onex')],
                                             [InlineKeyboardButton(text='Shipper', callback_data='shipper')],
                                             [InlineKeyboardButton(text='Назад', callback_data='backtomain')]])

# Клавиатура для Onex
onex_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пункт 1 Onex', callback_data='onex_option1')],
    [InlineKeyboardButton(text='Пункт 2 Onex', callback_data='onex_option2')]
])

# Клавиатура для Shipper
shipper_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пункт 1 Shipper', callback_data='shipper_option1')],
    [InlineKeyboardButton(text='Пункт 2 Shipper', callback_data='shipper_option2')]
])




# services = ['Onex', 'Shipper']

# async def inline_services():
#     keyboard = InlineKeyboardBuilder()
#     for service in services:
#         keyboard.add(InlineKeyboardButton(text=service, callback_data=f'service_{service}'))
#     return keyboard.adjust(2).as_markup()