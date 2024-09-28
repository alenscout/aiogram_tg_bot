from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Используй команду /help для списка команд, либо выбери команду в меню")

@router.message(Command('help'))
async def help(message: Message):
    await message.answer('Список команд: /help, /start, /list')