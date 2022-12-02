import imp
import exp


def tel_menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')
        print('2. Поиск по фамилии')
        print('3. Поиск по имени')
        print('0. Выход из меню')
        numb = int(input('Выберите пункт меню... '))
        if numb == 1:
            imp.wrt_data(imp.inp_data())
        elif numb == 2:
            exp.surname_search()
        elif numb == 3:
            exp.name_search()
        elif numb == 0:
            break
        else:
            print('некорректный ввод')
