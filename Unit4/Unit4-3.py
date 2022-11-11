"""Задайте последовательность чисел. Напишите программу, которая
    выведет список неповторяющихся элементов исходной последовательности."""

my_list = list(map(int, input().split()))
res_list = []

for num in my_list:
    if num not in res_list:
        res_list.append(num)
    else:
        res_list.pop()


print(res_list)