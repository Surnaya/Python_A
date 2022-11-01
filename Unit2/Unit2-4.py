"""Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся
в файле file.txt в одной строке одно число."""

from random import randint

n = int(input('N: '))
my_list = [randint(-n, n) for i in range(1, n)]

with open('text.txt', 'w') as f:
    f.write(str([randint(1, n - 1) for i in range(n)]))

list_index = []
with open('text.txt', 'r') as f:
    for line in f:
        list_index.append(line)

count=1
for el in list_index:
    count *= my_list[el]

print(count)