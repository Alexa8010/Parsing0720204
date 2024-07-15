import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json

def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    base_url = 'http://books.toscrape.com/'

    books_data = []

    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title']
        price = float(article.find('p', class_='price_color').text[1:].replace('£', ''))
        rating = article.find('p', class_='star-rating')['class'][1]

        book_info = {
            'Title': title,
            'Price': price,
            'Rating': rating
        }

        books_data.append(book_info)

    return books_data

def save_data_to_json(books_data, filename='books_data.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(books_data, file, indent=4)

def main():
    base_url = 'http://books.toscrape.com/'
    all_books_data = []

    for i in range(1, 3):
        url = f'{base_url}catalogue/page-{i}.html'
        books_data = scrape_books(url)
        all_books_data.extend(books_data)

    df = pd.DataFrame(all_books_data)
    print(df.head(3))

    save_data_to_json(all_books_data)

if __name__ == '__main__':
    main()