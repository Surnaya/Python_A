"""Создайте программу для игры в ""Крестики-нолики""."""

board = [i for i in range(1, 10)]

def my_board(board):                        # функция, рисующая игровое поле 3х3
    print('=' * 13)
    for i in range(3):
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
        print('=' * 13)

def index_win(board):                       # проверка выигрышных комбинаций
    my_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for el in my_win:
        if board[el[0]] == board[el[1]] == board[el[2]]:
            return board[el[0]]
    return False

def enter(gamer):                    # принимает ввод пользователя
    chek = False
    while not chek:
        numb = int(input(f'Ваш ход {gamer}. Введите число от 1 до 9'))
        if 1 <= numb <= 9:
            if (str(board[numb - 1]) not in 'XO'):
                board[numb - 1] = gamer
                chek = True
            else:
                print('Эта клетка занята')
        else:
            print('Некорректный ввод. Введите число от 1 до 9.')

def main(board):                     #главная функция
    count = 0
    win = False
    while not win:
        my_board(board)
        if count % 2 == 0:
           enter("X")
        else:
           enter("O")
        count += 1
        if count > 4:
           if index_win(board):
              print(f'Поздравляю, {index_win(board)}, ты выиграл!')
              win = True
              break
        if count == 9:
            print('Ничья!')
            break
    my_board(board)
main(board)
