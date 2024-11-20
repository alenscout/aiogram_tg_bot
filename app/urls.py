import os
# Путь к файлу .env
env_path = "/home/ubuntu/aiogram_tg_bot/.env"

server_ip = None
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.startswith("SERVER_IP="):  # Проверяем только нужную переменную
                server_ip = line.strip().split('=', 1)[1]
                break

# Onex URLS
ip = server_ip
compress = 'http://' + ip + ":8000/"
api = 'api/v1/'

onex_way_url = ip + api + "onex_on_the_way"
onex_usa_url = ip + api + 'onex_at_warehouse'
onex_kg_url = ip + api + 'onex_ready'

# Shipper URLS
shipper_way_url = ip + api + 'shipper'

# LifeShop URLS
lifeshop_way_url = ip + api + 'lifeshop'
