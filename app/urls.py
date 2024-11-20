import requests
# Путь к файлу .env
env_path = "/home/alen/aiogram_tg_bot/aiogram_tg_bot/.env"
response = requests.get("https://ifconfig.me")
public_ip = response.text.strip()

# Чтение файла .env и запись публичного IP
with open(env_path, "w") as f:
    f.write(f"SERVER_IP={public_ip}\n")

print(f"Public IP: {public_ip}")

# Onex URLS
ip = public_ip
compress = 'http://' + ip + ":8000/"
api = 'api/v1/'

onex_way_url = ip + api + "onex_on_the_way"
onex_usa_url = ip + api + 'onex_at_warehouse'
onex_kg_url = ip + api + 'onex_ready'

# Shipper URLS
shipper_way_url = ip + api + 'shipper'

# LifeShop URLS
lifeshop_way_url = ip + api + 'lifeshop'
