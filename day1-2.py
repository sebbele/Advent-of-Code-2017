#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

#input function for both python2.7 and 3
def getInput(prompt=''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

captcha = getInput('captcha string: ')

def main(input):
    result = []
    input_str = str(input)
    string_len = len(input_str)
    jump_len = len(input_str) // 2

    for i in range(len(input_str)):
        current_pos = i
        next_pos = i + jump_len
        next_pos = int(next_pos % string_len)
        print(current_pos, next_pos)
        if input_str[next_pos] == input_str[current_pos]:
            result.append(int(input_str[i]))
    return sum(result)

print(main(captcha))
