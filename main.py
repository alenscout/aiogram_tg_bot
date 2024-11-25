import logging
import asyncio,requests,os
from app.handlers import router
from config import TOKEN
from aiogram import Bot, Dispatcher

bot = Bot(token=TOKEN) 
dp = Dispatcher()
 
# Логика для Public ip
env_path = "/home/ubuntu/aiogram_tg_bot/.env"
response = requests.get("https://ifconfig.me")
public_ip = response.text.strip()

# Чтение файла .env и запись публичного IP
with open(env_path, "w") as f:
    f.write(f"IP_ADDRESS={public_ip}\n")   
    
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
    