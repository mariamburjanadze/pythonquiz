import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

page_index = 1
while page_index < 6:
    url = f'https://alta.ge/notebooks-page-{page_index}.html'
    request = requests.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    section = soup.find('div', class_='grid-list')

    all_product_names = section.find_all('div', class_='ty-grid-list__item-name')
    all_product_prices = section.find_all('span', class_='ty-price-num')

    all_product_names_list = [i.text.strip().replace('\n', '') for i in all_product_names]
    all_product_prices_list = [i.text.strip().replace('\n', '') for i in all_product_prices]

    index = 0
    all_products = {}

    while index < len(all_product_prices_list):
        all_products[all_product_names_list[index]] = [all_product_prices_list[index]]
        index += 1

    file = open('file.csv', 'a')
    file_writer = csv.writer(file)
    for i in all_products.keys():
        file_writer.writerow([i, all_products[i]])
    sleep(5)
    page_index += 1