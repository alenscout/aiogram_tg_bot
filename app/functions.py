import requests
from aiogram.types import CallbackQuery
    
# тест функция общая
async def service_way_data(callback: CallbackQuery, url: str):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json().get("data", [])
        
        # Проверка на пустоту (включая пустой словарь)
        if not data or all(isinstance(item, dict) and not item for item in data):
            return "Данные пусты"
        
        result = ""
        for item in data:
            if isinstance(item, str):
                parts = item.split(" - ")
                if len(parts) == 3:
                    number, name, price = parts
                    result += f"Трэк: {number}\nТовар: {name}\nЦена: {price}\n\n"
            else:
                # Если вдруг формат данных будет другим
                result += "Запись содержит неподдерживаемый формат данных\n\n"
        
        return result if result else "Данные пусты"
    else:
        return "Error"


# функция в основном для Onex **старый вариант(на lifeshop выдавал ошибку)**
# async def onex_way_data(callback: CallbackQuery, url: str):
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json().get("data", [])
        
#         result = ""
#         for item in data:
#             parts = item.split(" - ")
#             if len(parts) == 3:
#                 number, name, price = parts
#                 result += f"Трэк: {number}\nТовар: {name}\nЦена: {price}\n\n"
        
#         return result if result else "Данные пусты"
#     else:
#         return "Error"

# функция для LifeShop(рабочая как для onex, так и для lifeshop)
# async def lifeshop_way_data(callback: CallbackQuery, url: str):
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json().get("data", [])
        
#         # Проверка на пустоту (включая пустой словарь)
#         if not data or all(isinstance(item, dict) and not item for item in data):
#             return "Данные пусты"
        
#         result = ""
#         for item in data:
#             if isinstance(item, str):
#                 parts = item.split(" - ")
#                 if len(parts) == 3:
#                     number, name, price = parts
#                     result += f"Трэк: {number}\nТовар: {name}\nЦена: {price}\n\n"
#             else:
#                 # Если в будущем данные будут иного формата
#                 result += "Запись содержит неподдерживаемый формат данных\n\n"
        
#         return result if result else "Данные пусты"
#     else:
#         return "Error"