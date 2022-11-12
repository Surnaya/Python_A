"""Напишите программу, удаляющую из текста все слова, содержащие ""абв""."""

my_text = input().split()
del_text = 'абв'

new_text = [i for i in my_text if del_text not in i]
print(' '.join(new_text))
