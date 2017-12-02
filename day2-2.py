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
spreadsheet = []
while True:
    try:
        line = getInput()
    except EOFError:
        break
    spreadsheet.append(line)

result = []
for line in spreadsheet:
    values = line.split()
    values.sort(key=int)
    for num1 in values:
         for num2 in values:
            num1 = int(num1)
            num2 = int(num2)
            if num1 == num2:
                continue
            if num1 % num2 == 0:
                result.append(num1 // num2)

print(sum(result))
