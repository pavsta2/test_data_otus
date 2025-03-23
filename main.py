""" Модуль для сериализации тестовых данных и их преобразования. Домашнее задание
по уроку "Работа с тестовыми данными" """
import json
from collections import deque
from csv import DictReader

# Открываем исходный json-файл и записываем его в переменную users
with open('users.json', 'r') as f:
    users = json.load(f)

# Составляем список лишних ключей словаря, описывающего пользователя
keys_to_remove = list(users[0].keys())
keys_to_remove.remove('name')
keys_to_remove.remove('gender')
keys_to_remove.remove('address')
keys_to_remove.remove('age')

# Проходим по всем словарям и удаляем лишние ключи вместе со значениями
for row in users:
    for key in keys_to_remove:
        row.pop(key)
    # Дополнительно добавляем в каждый словарь элемент 'books'
    row['books'] = []

# Открываем исходный csv-файл
with open('books.csv', 'r') as f:
    books = DictReader(f)
    # Переносим все словари-книги в список словарей books_list
    books_list = []
    for row in books:
        books_list.append(row)

# Прохоимся по всем книгам-словарям и удаляем лишний элемент с ключем 'Publisher'
for book in books_list:
    del book['Publisher']

# Создаем объект очереди из книг
q = deque(books_list)
# Создаем счетчик для того, чтобы в случае выдачи книг всем юзерам из списка,
# начать выдавать дальше с начала списка
COUNT = 0
# Записываем книги в словарь пользователя в массив с ключом 'books'
while q:
    if COUNT > (len(users)-1):
        COUNT = 0
    users[COUNT]['books'].append(q.popleft())
    COUNT += 1

# Преобразуем массив users в result.json
with open('result.json', 'w') as f:
    json.dump(users, f, indent=2)
