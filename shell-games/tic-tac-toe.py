#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time
import os

'''
board index position

    0 | 1 | 2
    --|---|--
    3 | 4 | 5
    --|---|--
    6 | 7 | 8
'''
board = [' ' for i in range(1, 10)]
ten_s = '          '


def welcome_print():
    welcome = ' Welcome to Tic-Tac-Toe Game by PitPietro '
    print_title_message(welcome)

    print(ten_s, 'Number system is given below:', end='\n\n')
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print_board(numbers)
    print(ten_s, 'Let\'s start the game!', end='\n\n')


def get_terminal_dim():
    rows, columns = os.popen('stty size', 'r').read().split()
    return [rows, columns]


def get_player_input():
    while True:
        try:
            p_input = int(input('Enter a number: ')) - 1
        except ValueError:
            print(ten_s, '~/ You must insert a number')
        except KeyboardInterrupt:
            print(ten_s, '~/ Bye bye!')
            exit(0)
        else:
            if -1 < p_input < 9:
                break
            else:
                print(ten_s, '~/ Number out of range: it must be between 1 and 9')
    if board[p_input] == ' ':
        board[p_input] = 'X'
        return True
    else:
        print(ten_s, '~/ The number is already taken or does not exist')
        return False


def get_computer_move():
    # list of empty board's fields
    empty = []
    for i, place in enumerate(board):
        if place == ' ':
            empty.append(i)
    # check if there are any empty fields
    if empty:
        place = random.choice(empty)
        print(ten_s, '~/ Computer turn')
        print(ten_s, '________________', end='\n\n')
        board[place] = '0'
        return True
    else:
        print(ten_s, '~/ Computer says: No move left! That\'s a tie #')
        return False


def check_game_status():
    empty = [i for i in board if i == ' ']
    if not empty:
        print_title_message('Game over')
    win_boards = [
        [0, 1, 2],
        [0, 4, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 4, 6],
        [2, 5, 8],
        [3, 4, 5],
        [6, 7, 8],
    ]
    # check winning boards of the current game status
    for x, y, z in win_boards:
        if win_boards[x] != ' ' and win_boards[x] == win_boards[y] and win_boards[y] == win_boards[z]:
            if win_boards[x] == 'O':
                print(ten_s, '~/ Computer wins!')
            else:
                print(ten_s, '~/ You win!')
            exit(0)
    return


def print_current_status():
    current_status = ' Current status of the board '
    print_title_message(current_status)
    print_board(board)


def print_title_message(msg):
    cols = get_terminal_dim()[1]
    half_w_len = (int(cols) - len(msg)) // 2
    print_symbol('#', int(cols))
    print()
    print_symbol('=', half_w_len)
    print(msg, end='')
    print_symbol('=', half_w_len)
    print_symbol('#', int(cols))
    print(end='\n\n')


def print_board(n_list):
    line_l = ' {} | {} | {}'
    dashes = ' --------- '
    half_l_len = (int(get_terminal_dim()[1]) - len(line_l)) // 2

    msg = print_symbol_return(' ', half_l_len) + line_l + '\n' + \
          print_symbol_return(' ', half_l_len) + dashes + '\n' + \
          print_symbol_return(' ', half_l_len) + line_l + '\n' + \
          print_symbol_return(' ', half_l_len) + dashes + '\n' + \
          print_symbol_return(' ', half_l_len) + line_l
    print(msg.format(*n_list))
    print(end='\n\n')


def print_symbol(symbol, number):
    for i in range(number):
        print(symbol, end='')


def print_symbol_return(symbol, number):
    msg = ''
    for i in range(number):
        msg += symbol
    return msg


def tic_tac_toe_game():
    welcome_print()
    while True:
        while True:
            user_input = get_player_input()
            if user_input:
                break
        print_current_status()
        check_game_status()
        get_computer_move()
        print_current_status()
        check_game_status()


tic_tac_toe_game()
