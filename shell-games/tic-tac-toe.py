#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time
import os

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
    p_input = int(input('Enter a number: ')) - 1
    if board[p_input] == ' ':
        board[p_input] = 'X'
        return True
    else:
        print(ten_s, ' The number is already taken or does not exist')
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
        print(ten_s, '# Computer turn #')
        board[place] = '0'
        return True
    else:
        print(ten_s, '# Computer says: No move left! That\'s a tie #')
        return False


def print_current_status():
    current_status = ' Current status of the board '
    print_title_message(current_status)
    print_board(board)


def print_title_message(msg):
    cols = get_terminal_dim()[1]
    half_w_len = (int(cols) - len(msg)) // 2
    print_symbol('#', int(cols))
    print()
    print_symbol('#', half_w_len)
    print(msg, end='')
    print_symbol('#', half_w_len)
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
    print_current_status()


tic_tac_toe_game()
