import requests
from aiogram.types import CallbackQuery


async def service_way_data(callback: CallbackQuery, url: str):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json().get("data", [])
        
        result = " "
        for item in data:
            parts = item.split(" - ")
            if len(parts) == 3:
                _, name, price = parts
                result += f"Товар: {name}\n \nЦена(в 💲): {price}\n\n"
        
        return result if result else "Данные пусты"
    else:
        return "Error"