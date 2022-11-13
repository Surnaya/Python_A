"""Урок 2. Задача 2.
    Напишите программу, которая принимает на вход число N и выдает набор
    произведений чисел от 1 до N."""

# n = int(input('Введите число N: '))
# def fact(n):
#     p = 1
#     my_list = [1]
#     for i in range(2, n + 1):
#         p = p * i
#         my_list.append(p)
#     return my_list
# print(f'Произведения чисел от 1 до N  = {fact(n)}')

n = int(input('Введите число N: '))
def fact(n):
    p = 1
    for i in range(1, n + 1):
        p = p * i
        yield p
print(f'Произведения чисел от 1 до N  = {[i for i in fact(n)]}')
