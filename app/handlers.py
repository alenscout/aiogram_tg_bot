from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests
import app.keyboards as kb
import app.urls as url
import app.functions as fn

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
    result = await fn.service_way_data(callback, url.onex_usa_url)
    await callback.message.edit_text(result, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()

@router.callback_query(F.data == 'onex_way')
async def handle_onex_way(callback: CallbackQuery):
    result = await fn.service_way_data(callback, url.onex_way_url)
    await callback.message.edit_text(result, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()
    
@router.callback_query(F.data == 'onex_kg')
async def onex_gdocs_data(callback: CallbackQuery):
    result = await fn.service_way_data(callback, url.onex_kg_url)
    await callback.message.edit_text(result, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()



# Shipper
@router.callback_query(F.data == 'shipper_way')
async def handle_shipper_way(callback: CallbackQuery):
    result = await fn.shipper_way_data(callback, url.shipper_way_url)
    await callback.message.edit_text(result, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()
    
@router.callback_query(F.data == 'shipper_useradd')
async def shipper_useradd(callback: CallbackQuery):
    await callback.message.edit_text("Добавить пользователя")



# LifeShop
@router.callback_query(F.data == 'lifeshop_way')
async def handle_lifeshop_way(callback: CallbackQuery):
    result = await fn.service_way_data(callback, url.lifeshop_way_url)
    await callback.message.edit_text(result, parse_mode=ParseMode.MARKDOWN)
    await callback.answer()
    
# Exchanger

class ExchangeState(StatesGroup):
    waiting_for_amount = State()

@router.callback_query(lambda c: c.data == "exchanger")
async def ask_amount(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Введите число для обмена:")
    await state.set_state(ExchangeState.waiting_for_amount)

@router.message(ExchangeState.waiting_for_amount)
async def process_amount(message: types.Message, state: FSMContext):
    try:
        # Получаем текст сообщения и убираем пробелы
        user_input = message.text.strip()
        print(f"Ввод пользователя: '{user_input}'")  # Отладка

        # Преобразуем в целое число
        amount = int(user_input)
        print(f"Преобразованное число: {amount}")  # Отладка

        # Проверяем, что число положительное
        if amount <= 0:
            raise ValueError("Число должно быть положительным.")

        # Если все ок, формируем ссылку
        link = f"http://13.50.17.4:8000/api/v1/drop?amount={amount}"
        print(f"Сформированная ссылка: {link}")  # Отладка

        # Выполняем запрос
        response = requests.get(link)
        print(f"HTTP-статус ответа: {response.status_code}")  # Отладка

        if response.status_code == 200:
            data = response.json()
            print(f"Полученные данные: {data}")  # Отладка

            # Проверка наличия данных в ключе "data"
            if "data" in data and len(data["data"]) > 0:
                exchange_info = data["data"][0]
                print(f"Информация о обмене: {exchange_info}")  # Отладка

                # Проверяем, что строка в нужном формате
                if isinstance(exchange_info, str):
                    # Разбиваем строку на две части: долларов и курса
                    parts = exchange_info.split("\n")
                    if len(parts) >= 2:
                        dollars = parts[0].split(":")[1].strip()  # Получаем сумму в долларах
                        ruble_rate = parts[1].split(":")[1].strip()  # Получаем курс рубля

                        # Формируем сообщение для пользователя
                        message_text = f"Вы получите: *{dollars}*\nКурс рубля: `{ruble_rate}`"
                        await message.answer(message_text, parse_mode=ParseMode.MARKDOWN)
                    else:
                        await message.answer("Неверный формат данных в ответе.")
                else:
                    await message.answer("Полученные данные не в строковом формате.")
            else:
                await message.answer("Ответ не содержит данных для обработки.")
        else:
            await message.answer(f"Ошибка при запросе данных: {response.status_code}")

    except ValueError as e:
        print(f"Ошибка ValueError: {e}")  # Отладка
        await message.answer("Введите корректное положительное число.")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")  # Отладка
        await message.answer(f"Произошла ошибка: {e}")
    finally:
        await state.clear()

    
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

