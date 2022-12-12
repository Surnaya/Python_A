x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b

def sum():
    return x + y

def dif():
    return x - y

def mult():
    return x * y

def div():
    try:
        return x / y
    except ZeroDivisionError:
        return 'На 0 делить нельзя'