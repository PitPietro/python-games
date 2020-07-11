#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time
import os

board = [' ' for i in range(1, 10)]
ten_s = '          '


def welcome_print():
    welcome = ' Welcome to Tic-Tac-Toe Game by PitPietro '
    cols = get_terminal_dim()[1]
    half_w_len = (int(cols) - len(welcome)) // 2
    print_symbol('#', int(cols))
    print()
    print_symbol('#', half_w_len)
    print(welcome, end='')
    print_symbol('#', half_w_len)
    print(end='\n\n')
    print(ten_s, 'Number system is given below:', end='\n\n')
    line_l = ' 1 | 2 | 3 '
    dashes = ' --------- '
    half_l_len = (int(cols) - len(line_l)) // 2
    print_symbol(' ', half_l_len)
    print(line_l)
    print_symbol(' ', half_l_len)
    print(dashes)
    print_symbol(' ', half_l_len)
    print(' 4 | 5 | 6 ')
    print_symbol(' ', half_l_len)
    print(dashes)
    print_symbol(' ', half_l_len)
    print(' 7 | 8 | 9 ', end='\n\n')
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


def print_current_status():
    welcome = ' Current status of the board '
    cols = get_terminal_dim()[1]
    half_w_len = (int(cols) - len(welcome)) // 2
    print_symbol('#', int(cols))
    print()
    print_symbol('#', half_w_len)
    print(welcome, end='')
    print_symbol('#', half_w_len)
    print(end='\n\n')

    line_l = ' {} | {} | {}'
    dashes = ' --------- '
    half_l_len = (int(cols) - len(line_l)) // 2

    msg = print_symbol_return(' ', half_l_len) + line_l + '\n' + \
          print_symbol_return(' ', half_l_len) + dashes + '\n' + \
          print_symbol_return(' ', half_l_len) + line_l + '\n' + \
          print_symbol_return(' ', half_l_len) + dashes + '\n' + \
          print_symbol_return(' ', half_l_len) + line_l
    print(msg.format(*board))

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
    print_current_status()
    welcome_print()


tic_tac_toe_game()
