# Onex URLS
def load_ip_from_env(filename=".env"):
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("IP_ADDRESS="):
                return line.split("=", 1)[1].strip()

ip = load_ip_from_env()
compress = f"http://{ip}:8000/"
api = 'api/v1/'

onex_way_url = compress + api + "onex_on_the_way"
onex_usa_url = compress + api + 'onex_at_warehouse'
onex_kg_url = compress + api + 'onex_ready'

# Shipper URLS
shipper_way_url = compress + api + 'shipper'

# LifeShop URLS
lifeshop_way_url = compress + api + 'lifeshop'
