import json
import menu


def all_data():
    with open("sales.json", encoding='utf-8') as f:
        list_all = []
        sales = json.load(f)
        for item in sales:
            for i in item['cars']:
                cars_sales = item['manager']['last_name'] + ' ' + item['manager']['first_name'] + ' ' + i[
                    'color'] + ' ' + i['model'] + ' ' + i['maker'] + ' ' + str(i['year']) + ' ' + str(i['price'])
                list_all.append(cars_sales)
        return list_all


def all_employee():
    with open("sales.json", encoding='utf-8') as f:
        list_empl = []
        sales = json.load(f)
        for item in sales:
            name_empl = item['manager']['last_name'] + ' ' + item['manager']['first_name']
            list_empl.append(name_empl)
        return list_empl


def all_sum():
    with open("sales.json", encoding='utf-8') as f:
        list_sum = []
        sales = json.load(f)
        for item in sales:

            for i in item['cars']:
                sales_sum = i['price']
                list_sum.append(sales_sum)
        my_sum = sum(list_sum)
        return my_sum


def empl_sum():
    with open("sales.json", encoding='utf-8') as f:
        all_empl_sum = []
        sales = json.load(f)
        for item in sales:
            empl = item['manager']['last_name'] + ' ' + item['manager']['first_name']
            cars_sum = []
            for i in item['cars']:
                c = i['price']
                cars_sum.append(c)
            emp_sum= str(sum(cars_sum))
            empl = empl + ' ' + emp_sum
            all_empl_sum.append(empl)
        return all_empl_sum


def surname_search():
    my_search = menu.wind_2().label
    result = []
    with open("sales.json", encoding='utf-8') as f:
        sales = json.load(f)
        for item in sales:
            if item['manager']['last_name'] == my_search:
                for i in item['cars']:
                    cars_empl = i['color'] + ' ' + i['model'] + ' ' + i['maker'] + ' ' + str(i['year']) + ' ' + str(i['price'])
                    result.append(cars_empl)
                return result
            else:
                return f'Сотрудник {my_search}  не найден'
