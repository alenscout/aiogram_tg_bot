import os, requests
# Путь к файлу .env
env_path = "/home/ubuntu/aiogram_tg_bot/.env"

# Попробуем получить IP из .env
if os.path.exists(env_path):
    with open(env_path, "r") as f:
        lines = f.readlines()
        # Ищем строку с SERVER_IP
        for line in lines:
            if line.startswith("SERVER_IP="):
                public_ip = line.split('=')[1].strip()
                break
        else:
            # Если IP не найден, получаем его с помощью ifconfig.me
            response = requests.get("https://ifconfig.me")
            public_ip = response.text.strip()
            # Записываем новый IP в .env
            with open(env_path, "a") as f:
                f.write(f"SERVER_IP={public_ip}\n")
else:
    # Если файл .env не существует, создаем его и записываем IP
    response = requests.get("https://ifconfig.me")
    public_ip = response.text.strip()
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
