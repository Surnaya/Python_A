# считывает строку, введенную пользователем и разбивает на отдельные переменные

def op(string):
    if 'j' not in string:
        some_list = string.split()
        a = int(some_list[0])   #первое число
        b = int(some_list[2])   #второе число
        oprt = some_list[1]     #оператор
        return a, b, oprt       #вернет данные в виде кортежа
    else:
        some_list = string.split()
        a1 = some_list[0]
        a2 = ''.join(some_list[1:3])[:-1]
        b1 = some_list[4]
        b2 = ''.join(some_list[5:])[:-1]
        oprt = some_list[3]
        a = complex(int(a1), int(a2))
        b = complex(int(b1), int(b2))
        return a, b, oprt