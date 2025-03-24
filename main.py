""" Модуль для сериализации тестовых данных и их преобразования. Домашнее задание
по уроку "Работа с тестовыми данными" """
import json
from collections import deque
from csv import DictReader

# Открываем исходный json-файл и записываем его в переменную users
with open('users.json', 'r') as f:
    users = json.load(f)

# Создаем новый список календарей с юзерами в нужном формате
users_new = []
for user in users:
    users_new.append({
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    })

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
# Записываем книги в словарь пользователя в элемент с ключом 'books'
while q:
    if COUNT > (len(users)-1):
        COUNT = 0
    users_new[COUNT]['books'].append(q.popleft())
    COUNT += 1

# Преобразуем массив users_new в result.json
with open('result.json', 'w') as f:
    json.dump(users_new, f, indent=2)
