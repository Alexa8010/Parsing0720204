'''Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе. https://www.mongodb.com/ https://www.mongodb.com/products/compass
Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с помощью Buautiful Soup в MongoDB и создайте базу данных и коллекции для их хранения.
Поэкспериментируйте с различными методами запросов.
Зарегистрируйтесь в ClickHouse.
Загрузите данные в ClickHouse и создайте таблицу для их хранения.'''

import json
from pymongo import MongoClient

# Подключение к серверу MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Выбор базы данных и коллекции
db = client['steam']
collection = db['books1']

# Чтение файла JSON
with open('Parsing_0720204/Seminar_3/books_data.json', 'r') as file:
    data = json.load(file)


# print(data)

# # Если data - это список, обращаемся к элементам по индексу
# first_element = data[0]  # Получаем первый элемент списка
# print(first_element)

# Функция разделения данных на более мелкие фрагменты
def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

# Разделение данных на фрагменты по 50 записей в каждом
chunk_size = 50
data_chunks = list(chunk_data(data, chunk_size))

# Вставка фрагментов в коллекцию MongoDB
for chunk in data_chunks:
    collection.insert_many(chunk)

print("Данные успешно вставлены.")
