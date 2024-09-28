import logging
import asyncio

from app.handlers import router
from config import TOKEN
from aiogram import Bot, Dispatcher


#Первичная логика бота 
bot = Bot(token=TOKEN) 
dp = Dispatcher()
        
    
''' Запуск бота '''

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
    