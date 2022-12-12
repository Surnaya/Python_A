import json

def my_board(board):                        # функция, рисующая игровое поле 3х3
    print('=' * 13)
    for i in range(3):
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
        print('=' * 13)

def index_win(board):
    with open('init.json', 'r') as f:
        my_win = json.load(f)                      # проверка выигрышных комбинаций
    for el in my_win:
        if board[el[0]] == board[el[1]] == board[el[2]]:
            return board[el[0]]
    return False

def enter(gamer, board):                    # принимает ввод пользователя
    chek = False
    while not chek:
        numb = int(input(f'Ваш ход {gamer}. Введите число от 1 до 9 '))
        if 1 <= numb <= 9:
            if (str(board[numb - 1]) not in 'XO'):
                board[numb - 1] = gamer
                chek = True
            else:
                print('Эта клетка занята')
        else:
            print('Некорректный ввод. Введите число от 1 до 9.')