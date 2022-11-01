"""Реализуйте алгоритм перемешивания списка."""

from random import randint

my_list = [el for el in input()]
list_rand = [my_list[randint(0, len(my_list)-1)] for i in range(len(my_list))]
print(my_list)
print(list_rand)