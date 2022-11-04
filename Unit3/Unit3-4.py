"""Напишите программу, которая будет преобразовывать десятичное число в двоичное."""

num = int(input('Введите число: '))
num_dub = []
while num > 0:
    a = num % 2
    num_dub.append(a)
    num = num // 2

new_num = num_dub[::-1]
new_num = ''.join([str(i) for i in new_num])

print(f'В двоичной системе = {new_num}')
