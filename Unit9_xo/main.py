from game import *

board = [i for i in range(1, 10)]

def main(board):
    count = 0
    win = False
    while not win:
        my_board(board)
        if count % 2 == 0:
           enter("X", board)
        else:
           enter("O", board)
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

if __name__ == '__main__':
    main(board)
