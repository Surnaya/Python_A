"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах."""

with open('text.txt', 'w') as f:
    f.write('ffffffhhhhyyyttrrrssss')

my_str = ''
with open('text.txt', 'r') as f:
    for line in f:
        my_str += line

encoding_str = ''

i = 0
while i < len(my_str):
    count = 1
    while i + 1 < len(my_str) and my_str[i] == my_str[i + 1]:
        count = count + 1
        i = i + 1
    encoding_str += str(count) + my_str[i]
    i = i + 1
print(encoding_str)

with open('rle_text.txt', 'w') as f:
    f.write(encoding_str)

