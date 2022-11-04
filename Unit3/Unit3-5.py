"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов."""

def fibonacci(k):
    fib1 = fib2 = 1
    for i in range(k):
        yield fib1
        fib1, fib2 = fib2, fib1+ fib2

def fibonacci_neg(k):
    fib_neg1 = 1
    fib_neg2 = -1
    for i in range(k):
        yield fib_neg1
        fib_neg1, fib_neg2 = fib_neg2, fib_neg1 - fib_neg2

k = int(input('Задайте число k '))

my_list = list(fibonacci(k))
my_list_neg = list(fibonacci_neg(k))[::-1]
my_fibo = my_list_neg + [0] + my_list
print(my_fibo)


