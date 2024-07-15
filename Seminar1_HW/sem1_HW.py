"""
Сценарий Foursquare
Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию 
(например, кофейни, музеи, парки и т.д.).
Используйте API Foursquare для поиска заведений в указанной категории.
Получите название заведения, его адрес и рейтинг для каждого из них.
Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.
"""

'''
Сценарий Foursquare
Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию 
(например, кофейни, музеи, парки и т.д.).
Используйте API Foursquare для поиска заведений в указанной категории.
Получите название заведения, его адрес и рейтинг для каждого из них.
Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.
'''


import requests
import json

# Ваши учетные данные API
client_id = "__"
client_secret = "__"

# Конечная точка API
endpoint = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = input("Введите название города: ")

category = input('Введите интересующую категорию: ')
params = {
    "limit": 10,
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": category,
    "fields": "name,location,rating"
}

headers = {
"Accept": "application/json",
"Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

response = requests.get(endpoint, params=params, headers=headers)

# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос API!")
    data = json.loads(response.text) # Парсим JSON-ответ в словарь Python
    venues = data["results"] # Получаем список мест из данных ответа
    for venue in venues: # Проходимся по каждому месту в списке
        print("Название:", venue["name"])
        try:
            print("Адрес:", venue["location"]["address"])
            print("Рейтинг:", venue["rating"])
        except Exception:
            print("Адрес заведения не найден!")
            print("Рейтинг не найден")

        print("\n")

else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)