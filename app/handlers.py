from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
import app.keyboards as kb
import app.urls as url
import app.functions as fn
import asyncio

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет. Используй команду /help для списка команд, либо выбери команду в меню", reply_markup=kb.main)

@router.message(Command('help'))
async def help(message: Message):
    await message.answer('Вот список доступных команд:', reply_markup=kb.commands)

@router.message(Command('list'))
async def list(message: Message):
    await message.answer('Список доступных сервисов на данный момент:', reply_markup=kb.services)       

@router.callback_query(F.data == 'commands')
async def callback_help(callback: CallbackQuery):
    await callback.message.edit_text('Выберите команду', reply_markup=kb.commands)
    
@router.callback_query(F.data == 'c_start')
async def callback_help(callback: CallbackQuery):
    await start(callback.message)
    await callback.message.delete()
    await callback.answer()

@router.callback_query(F.data == 'c_help')
async def callback_help(callback: CallbackQuery):
    await help(callback.message)
    await callback.message.delete()
    await callback.answer()

@router.callback_query(F.data == 'c_list')
async def callback_help(callback: CallbackQuery):
    await list(callback.message)
    await callback.message.delete()
    await callback.answer()

# Сервисы
@router.callback_query(F.data == 'service')
async def service(callback: CallbackQuery):
    await callback.message.edit_text('Выберите желаемый сервис', reply_markup=kb.services)
    
@router.callback_query(F.data == 'onex')
async def onex(callback: CallbackQuery):
    await callback.answer("Выбран Onex")
    await callback.message.edit_text("Вы выбрали Onex. Выберите пункт:", reply_markup=kb.onex_menu)
    
@router.callback_query(F.data == 'shipper')
async def shipper(callback: CallbackQuery):
    await callback.answer("Выбран Shipper")
    await callback.message.edit_text("Вы выбрали Shipper. Выберите пункт:", reply_markup=kb.shipper_menu)

@router.callback_query(F.data == 'lifeshop')
async def shipper(callback: CallbackQuery):
    await callback.answer("Выбран LifeShop")
    await callback.message.edit_text("Вы выбрали LifeShop. Выберите пункт:", reply_markup=kb.lifeshop_menu)

@router.callback_query(F.data == 'gdocs')
async def shipper(callback: CallbackQuery):
    await callback.answer("Выбран Google Docs")
    await callback.message.edit_text("Вы выбрали Google Docs. Выберите пункт:", reply_markup=kb.gdocs_menu)



# Onex
@router.callback_query(F.data == 'onex_usa')
async def handle_onex_usa(callback: CallbackQuery):
    result = await fn.onex_way_data(callback, url.onex_usa_url)
    await callback.message.edit_text(result)
    await callback.answer()

@router.callback_query(F.data == 'onex_way')
async def handle_onex_way(callback: CallbackQuery):
    result = await fn.service_way_data(callback, url.onex_way_url)
    await callback.message.edit_text(result)
    await callback.answer()
    
@router.callback_query(F.data == 'onex_kg')
async def onex_gdocs_data(callback: CallbackQuery):
    await asyncio.sleep(10)
    await callback.message.edit_text("В Кыргызстане")



# Shipper
@router.callback_query(F.data == 'shipper_way')
async def handle_shipper_way(callback: CallbackQuery):
    result = await fn.shipper_way_data(callback, url.shipper_way_url)
    await callback.message.edit_text(result)
    await callback.answer()
    
@router.callback_query(F.data == 'shipper_useradd')
async def shipper_useradd(callback: CallbackQuery):
    await callback.message.edit_text("Добавить пользователя")



# LifeShop
@router.callback_query(F.data == 'lifeshop_way')
async def handle_lifeshop_way(callback: CallbackQuery):
    result = await fn.service_way_data(callback, url.lifeshop_way_url)
    await callback.message.edit_text(result)
    await callback.answer()
    

    
# Google Docs
@router.callback_query(F.data == 'gdocs_write')
async def lifeshop_option1(callback: CallbackQuery):
    await callback.message.edit_text("Записать все посылки")
    
@router.callback_query(F.data == 'gdocs_smth')
async def lifeshop_option3(callback: CallbackQuery):
    await callback.message.edit_text("что-то еще")
    
    
    
''' Кнопки назад '''    
    
@router.callback_query(F.data == 'backtomain')
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text("Привет. Используй команду /help для списка команд, либо выбери команду в меню", reply_markup=kb.main)

@router.callback_query(F.data == 'backtoservices')
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text("Выберите желаемый сервис", reply_markup=kb.services)
    
''' Обработка текстовых сообщений'''

@router.message(F.text)
async def handle_text_message(message: Message):
    user_text = message.text.lower()

    if user_text in ['привет', 'салам']:
        await message.answer(f"Еще раз привет, используй команду /start или меню для работы со мной.")
    
    elif user_text in ['список команд', 'команды']:
        await message.answer('Список команд: /help, /start')
    
    else:
        await message.answer("Не знаю такую команду, проверьте на правильность написания. Используйте /help или меню.")

