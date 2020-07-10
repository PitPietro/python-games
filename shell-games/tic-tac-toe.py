#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time
import os


def welcome_print():
    welcome = ' Welcome to Tic-Tac-Toe Game by PitPietro '
    w_len = len(welcome)
    cols = get_terminal_dim()[1]
    tot_len = int(cols) - w_len
    half_len = tot_len // 2
    print_hash(int(cols))
    print()
    print_hash(half_len)
    print(welcome, end='')
    print_hash(half_len + 1)
    print()


def get_terminal_dim():
    rows, columns = os.popen('stty size', 'r').read().split()
    return [rows, columns]


def tic_tac_toe_game():
    welcome_print()


def print_hash(number):
    for i in range(number):
        print('#', end='')


tic_tac_toe_game()
