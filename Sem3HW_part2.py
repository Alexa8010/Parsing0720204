# from clickhouse_driver import Client
# import json

# # Подключение к серверу ClickHouse
# client = Client('localhost')

# # Создание базы данных (если она не существует)
# client.execute('CREATE DATABASE IF NOT EXISTS books1')

# # Создание таблицы
# # Создание основной таблицы 'books'
# client.execute('''
# CREATE TABLE IF NOT EXISTS steam.books1 (
#     id UInt64,
#     Title String,
#     Price Float,
#     Rating String,
    
# ) ENGINE = MergeTree()
# ORDER BY id
# ''')

# print("Таблица создана успешно.")

# with open('Parsing_0720204/Seminar_3/books_data.json', 'r') as file:
#     data = json.load(file)

# d
# #     # Вставка данных о book
#     client.execute("""
#     INSERT INTO steam.books1 ( Title, Price,
#         Rating
#     ) VALUES""",
#     [()])

# print("Данные введены успешно.")

# # Проверка успешности вставки
# result = client.execute("SELECT * FROM town_cary.crashes")
# print("Вставленная запись:", result[0])

from clickhouse_driver import Client 
import json 
 
# Подключение к серверу ClickHouse 
client = Client('localhost') 
 
# Создание базы данных (если она не существует) 
client.execute('CREATE DATABASE IF NOT EXISTS steam') 
 
# Создание таблицы 
client.execute(''' 
CREATE TABLE IF NOT EXISTS steam.books1 (  
    Title String, 
    Price Float32, 
    Rating String
) ENGINE = MergeTree() 
ORDER BY id 
''') 
 
print("Таблица 'books1' создана успешно.") 
 
# Чтение данных из JSON-файла
with open('Parsing_0720204/Seminar_3/books_data.json', 'r') as file: 
    data = json.load(file) 
 
# Вставка данных о книгах
for item in data:
    title = item.get('Title', '')
    price = item.get('Price', 0.0)
    rating = item.get('Rating', '')
    
client.execute("INSERT INTO steam.books1 (Title, Price, Rating) VALUES (%s, %s, %s)", (title, price, rating))

print("Данные успешно вставлены в таблицу 'books1'.")