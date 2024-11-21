from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Сервис', callback_data='service')],
                                             [InlineKeyboardButton(text='Команды', callback_data='commands')],
                                             [InlineKeyboardButton(text='Обмен', callback_data='exchanger')]])

commands = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='/help - Список доступных команд', callback_data='c_help')],
                                             [InlineKeyboardButton(text='/start - Начать работу бота', callback_data='c_start')],
                                             [InlineKeyboardButton(text='/list - Список доступных сервисов', callback_data='c_list')],
                                             [InlineKeyboardButton(text='⬅️Назад', callback_data='backtomain')]])

services = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Onex', callback_data='onex')],
                                             [InlineKeyboardButton(text='Shipper', callback_data='shipper')],
                                             [InlineKeyboardButton(text='LifeShop', callback_data='lifeshop')],
                                             [InlineKeyboardButton(text='Google Docs', callback_data='gdocs')],
                                             [InlineKeyboardButton(text='⬅️Назад', callback_data='backtomain')]])


# Клавиатура для Onex
onex_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='На складе в Америке', callback_data='onex_usa')],
    [InlineKeyboardButton(text='В пути', callback_data='onex_way')],
    [InlineKeyboardButton(text='В Кыргызстане', callback_data='onex_kg')],
    [InlineKeyboardButton(text='⬅️Назад', callback_data='backtoservices')]   
])

# Клавиатура для Shipper
shipper_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='В пути', callback_data='shipper_way')],
    [InlineKeyboardButton(text='Добавить пользователя', callback_data='shipper_useradd')],
    [InlineKeyboardButton(text='⬅️Назад', callback_data='backtoservices')]
])

# Клавиатура для LifeShop
lifeshop_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='В пути', callback_data='lifeshop_way')],
    [InlineKeyboardButton(text='⬅️Назад', callback_data='backtoservices')]
])

# Клавиатура для Google Docs
gdocs_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Записать все посылки', callback_data='gdocs_write')],
    [InlineKeyboardButton(text='что-то еще', callback_data='gdocs_smth')],
    [InlineKeyboardButton(text='⬅️Назад', callback_data='backtoservices')]
])


# services = ['Onex', 'Shipper']

# async def inline_services():
#     keyboard = InlineKeyboardBuilder()
#     for service in services:
#         keyboard.add(InlineKeyboardButton(text=service, callback_data=f'service_{service}'))
#     return keyboard.adjust(2).as_markup()