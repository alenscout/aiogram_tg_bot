import requests
from aiogram.types import CallbackQuery

# функция в основном для Onex
async def service_way_data(callback: CallbackQuery, url: str):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json(ensure_ascii = False).get("data", [])
        
        result = ""
        for item in data:
            parts = item.split(" - ")
            if len(parts) == 3:
                number, name, price = parts
                result += f"Трэк: {number}\nТовар: {name}\nЦена: {price}\n\n"
        
        return result if result else "Данные пусты"
    else:
        return "Error"