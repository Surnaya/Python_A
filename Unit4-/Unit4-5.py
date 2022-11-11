"""Даны два файла, в каждом из которых находится запись многочлена.
   Задача - сформировать файл, содержащий сумму многочленов."""

with open('unit_poly1.txt', 'r') as data:
    poly1 = data.readlines()
with open('unit_poly2.txt', 'r') as data:
    poly2 = data.readlines()

print(f"Первый многочлен {poly1}")
print(f"Второй многочлен {poly2}")


def lst_in_dict(poly):
    lst = []
    for el in poly:
        a = ''
        for i in el:
            if i.isdigit():
                a += i
            elif a != '':
                lst.append(int(a))
                a = ''
    dict = {key: val for key, val in enumerate(lst[::-1])}

    for key, value in list(dict.items()):
        if key != 0 and key % 2 == 0:
            del dict[key]
    return dict

dict1 = lst_in_dict(poly1)
dict2 = lst_in_dict(poly2)

result_dict = dict1
for key, value in dict2.items():
    if key in dict1:
        result_dict[key] += value
    else:
        result_dict.update({key: value})

result_list = []
result_poly = ''
for value in result_dict.values():
    result_list.append(value)
for i, val in enumerate(result_list[::-1]):
    if (len(result_list) - 1 - i) == 1:
        result_poly += f'{val}*x + '
    elif (len(result_list) - 1 - i) == 0:
        result_poly += f'{val} = 0'
    else:
        result_poly += f'{val}*x^{len(result_list) - 1 - i}  + '
print(f'Сумма многочленов {result_poly}')
