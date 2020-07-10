#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time
import os


def welcome_print():
    welcome = ' Welcome to Tic-Tac-Toe Game by PitPietro '
    cols = get_terminal_dim()[1]
    half_w_len = (int(cols) - len(welcome)) // 2
    ten_s = ' '
    for i in range(10):
        ten_s += ' '
    print_hash(int(cols))
    print()
    print_hash(half_w_len)
    print(welcome, end='')
    print_hash(half_w_len)
    print(end='\n\n')
    print(ten_s, 'Number system is given below:', end='\n\n')
    line_l = ' 1 | 2 | 3 '
    dashes = ' --------- '
    half_l_len = (int(cols) - len(line_l)) // 2
    print_spaces(half_l_len)
    print(line_l)
    print_spaces(half_l_len)
    print(dashes)
    print_spaces(half_l_len)
    print(' 4 | 5 | 6 ')
    print_spaces(half_l_len)
    print(dashes)
    print_spaces(half_l_len)
    print(' 7 | 8 | 9 ', end='\n\n')



def get_terminal_dim():
    rows, columns = os.popen('stty size', 'r').read().split()
    return [rows, columns]


def tic_tac_toe_game():
    welcome_print()


def print_hash(number):
    for i in range(number):
        print('#', end='')


def print_spaces(number):
    for i in range(number):
        print(' ', end='')


tic_tac_toe_game()
