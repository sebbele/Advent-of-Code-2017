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
    string_len = len(input_str) - 1
    for i in range(len(input_str)):
        current_pos = i
        if current_pos != string_len:
            next_pos = current_pos + 1
        else:
            next_pos = 0
        if input_str[next_pos] == input_str[current_pos]:
            result.append(int(input_str[i]))
    return sum(result)

print(main(captcha))
