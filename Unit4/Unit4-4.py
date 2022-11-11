"""Задана натуральная степень k. Сформировать случайным образом
   список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

  Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0"""

from random import randint

k = int(input("Введите натуральную степень k = "))

my_list = [randint(0, 101) for i in range(k+1)]
poly = ''

for i, val in enumerate(my_list[::-1]):
    if (len(my_list) - 1 - i) == 1:
        poly += f'{val}*x + '
    elif (len(my_list) - 1 - i) == 0:
        poly += f'{val} = 0'
    else:
        poly += f'{val}*x^{len(my_list) - 1 - i}  + '
print(poly)

with open('unit_poly.txt', 'w') as data:
    data.write(poly)

