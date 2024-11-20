import requests,os

response = requests.get("https://ifconfig.me")
public_ip = response.text.strip()

# Путь к файлу .env
env_path = '/home/alen/aiogram_tg_bot/aiogram_tg_bot/.env'

# Чтение файла .env и запись публичного IP
with open(env_path, "w") as f:
    f.write(f"SERVER_IP={public_ip}\n")

print(f"Public IP: {public_ip}")