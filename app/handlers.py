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
    await callback.answer("Был выбран пункт Сервис")
    await callback.message.edit_text('Выберите желаемый сервис', reply_markup=kb.services)
    
@router.callback_query(F.data == 'onex')
async def onex(callback: CallbackQuery):
    await callback.answer("Был выбран Onex")
    await callback.message.edit_text("Вы выбрали Onex. Выберите пункт:", reply_markup=kb.onex_menu)
    
@router.callback_query(F.data == 'shipper')
async def shipper(callback: CallbackQuery):
    await callback.answer("Был выбран Shipper")
    await callback.message.edit_text("Вы выбрали Shipper. Выберите пункт:", reply_markup=kb.shipper_menu)

# Обработчики для пунктов Onex
@router.callback_query(F.data == 'onex_option1')
async def onex_option1(callback: CallbackQuery):
    await callback.answer("Был выбран пункт 1 Onex")
    await callback.message.edit_text("Вы выбрали пункт 1 для Onex.")

@router.callback_query(F.data == 'onex_option2')
async def onex_option2(callback: CallbackQuery):
    await callback.answer("Был выбран пункт 2 Onex")
    await callback.message.edit_text("Вы выбрали пункт 2 для Onex.")

# Обработчики для пунктов Shipper
@router.callback_query(F.data == 'shipper_option1')
async def shipper_option1(callback: CallbackQuery):
    await callback.answer("Был выбран пункт 1 Shipper")
    await callback.message.edit_text("Вы выбрали пункт 1 для Shipper.")

@router.callback_query(F.data == 'shipper_option2')
async def shipper_option2(callback: CallbackQuery):
    await callback.answer("Был выбран пункт 2 Shipper")
    await callback.message.edit_text("Вы выбрали пункт 2 для Shipper.")
    
@router.callback_query(F.data == 'backtomain')
async def back_to_main(callback: CallbackQuery):
    await callback.answer("Возвращаемся назад")
    await callback.message.edit_text("Вы вернулись в главное меню", reply_markup=kb.main)

