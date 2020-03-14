import json
import os

current_path = os.getcwd()
print(current_path)
path = 'C:\\Users\\User\PycharmProjects\Homework-5\homework_14_parser_html_\dict_rent_apartments.json'

try:
    with open(path, 'r', encoding='utf-8') as f:
        dict_rent_apartments = json.load(f)
        print(f'1 Словарь rent получен')
except FileNotFoundError:
    dict_rent_apartments = ''
    print(f'2 Ошибка в получении словаря')