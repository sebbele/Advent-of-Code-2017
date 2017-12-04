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

print('Enter/paste content. Ctrl-D to save. ', end='')
pw_list = []
while True:
    try:
        line = getInput()
    except EOFError:
        break
    pw_list.append(line)

ok_passphrases = 0

for line in pw_list:
    this_row = line.split()
    last_word = len(this_row) - 1
    current_word = 0
    for word in this_row:
        if this_row.count(word) != 1:
            continue
        elif current_word != last_word:
            current_word += 1
        elif current_word == last_word:
            ok_passphrases += 1

print("acceptable passphrases: ",  ok_passphrases)
