from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет. Используй команду /help для списка команд, либо выбери команду в меню", reply_markup=kb.main)

@router.message(Command('help'))
async def help(message: Message):
    await message.answer('Список команд: /help, /start, /list')

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

# Onex
@router.callback_query(F.data == 'onex_usa')
async def onex_option1(callback: CallbackQuery):
    await callback.message.edit_text("В Америке")

@router.callback_query(F.data == 'onex_way')
async def onex_option2(callback: CallbackQuery):
    await callback.message.edit_text("В пути")
    
@router.callback_query(F.data == 'onex_gdocs')
async def onex_option2(callback: CallbackQuery):
    await callback.message.edit_text("Загрузить в GDocs")

# Shipper
@router.callback_query(F.data == 'shipper_usa')
async def shipper_option1(callback: CallbackQuery):
    await callback.message.edit_text("В Америке")

@router.callback_query(F.data == 'shipper_way')
async def shipper_option2(callback: CallbackQuery):
    await callback.message.edit_text("В пути")
    
@router.callback_query(F.data == 'shipper_gdocs')
async def shipper_option2(callback: CallbackQuery):
    await callback.message.edit_text("Загрузить в GDocs")

''' Кнопки назад '''    
    
@router.callback_query(F.data == 'backtomain')
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text("Привет. Используй команду /help для списка команд, либо выбери команду в меню", reply_markup=kb.main)

@router.callback_query(F.data == 'backtoservices')
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text("Выберите желаемый сервис", reply_markup=kb.services)
