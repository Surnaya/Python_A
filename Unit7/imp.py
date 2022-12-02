import csv


def inp_data():
    my_data = []
    name = input('Введите фамилию ')
    my_data.append(name)
    surname = input('Введите имя ')
    my_data.append(surname)
    tel_numb = input('Введите номер телефона ')
    my_data.append(tel_numb)
    return my_data


def wrt_data(my_data):
    with open('example.csv', 'a', newline='') as tel_book:
        writer = csv.writer(tel_book, delimiter=",", lineterminator="\r")
        writer.writerows([my_data])
    print('Спасибо, данные записаны')
