import csv


def surname_search():
    surname = input('Введите фамилию ')
    result = []
    with open("example.csv", encoding='utf-8') as tel_book:
        book_reader = csv.reader(tel_book, delimiter=",")
        for row in book_reader:
            if row[0] == surname:
                result.append(row)

    if result == []:
        print('Абонент не найден')
    else:
        print(f'Найден абонент {result[0][0]} {result[0][1]} - номер телефона {result[0][2]}')


def name_search():
    name = input('Введите имя ')
    result = []
    with open("example.csv", encoding='utf-8') as tel_book:
        book_reader = csv.reader(tel_book, delimiter=",")
        for row in book_reader:
            if row[1] == name:
                result.append(row)

    if not result:
        print('Абонент не найден')
    else:
        print(f'Найден абонент {result[0][0]} {result[0][1]} - номер телефона {result[0][2]}')
