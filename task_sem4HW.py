'''Выберите веб-сайт с табличными данными, который вас интересует.
Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

Ваш код должен включать следующее:

Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
Комментарии для объяснения цели и логики кода.

Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.'''

# Импорт необходимых библиотек
import requests
from lxml import html
from pymongo import MongoClient
import time
import pandas as pd
import csv

# Определение целевого URL
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

# Отправка HTTP GET запроса на целевой URL с пользовательским заголовком User-Agent
response = requests.get(url, headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

# Парсинг HTML-содержимого ответа с помощью библиотеки lxml
tree = html.fromstring(response.content)
# print(response.status_code) 
# 200

#  Использование выражения XPath для выбора всех строк таблицы в пределах таблицы с классом 'wikitable'
table_rows = tree.xpath("//table[@class='wikitable sortable sticky-header sort-under mw-datatable col2left col6left']/tbody/tr")
# print(table_rows)

# Предлагаю вариант посмотреть где пустые строки
# columns = table_rows[5].xpath(".//td/text()") 
# i=0
# for col in columns:
#     print(str(i)+"   ")
#     print(col)
#     i=i+1


data = []
for row in table_rows[4:]:
    columns = row.xpath(".//td/text()")
    data.append({
        'Country' : row.xpath(".//td[2]/a/text()")[0].strip(),
        'Population':  columns[2].strip().replace(',', ''),
        #'Population':  int(columns[2].strip().replace(',', '')) if columns[2].strip() else None,
        'Percentage of world': columns[3].strip(),
        'Date': row.xpath(".//td[5]/span/text()")[0].strip(),
        'Source': columns[5].strip()
})


#print(data)
df = pd.DataFrame(data)
df['Population'] = pd.to_numeric(df['Population'], errors='coerce')
print(df.info())

# print(df.loc[df['Country'] == 'France'])
df.to_csv('Population.csv')