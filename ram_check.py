from time import sleep
import psutil
import requests


# Лимит оперативной памяти в %
LIMIT_RAM_PERCENT = 55
TIMEOUT_CHECK = 2
API_URL = "https://your.api/url"


def send_alert(current_ram):
    data = {
        "message": "High RAM usage!!!",
        "current_ram": current_ram,
    }
    try:
        requests.post(API_URL, data=data)
    except requests.exceptions.ConnectionError:
        print(f"Не удалось подключиться к {API_URL}")
    

total_ram = psutil.virtual_memory().total
while True:
    ram_info = psutil.virtual_memory()
    available_ram = ram_info.available
    current_percent = available_ram/total_ram*100
    used_percent = 100 - current_percent
    if used_percent > LIMIT_RAM_PERCENT:
        print(f"Alert!!! Занято {used_percent:.2f}% оперативной памяти!!!")
        send_alert(used_percent)
    else:
        print(f"Доступно {available_ram/1_000_000_000:.2f}GB ({current_percent:.2f}%) оперативки")
    sleep(TIMEOUT_CHECK)
