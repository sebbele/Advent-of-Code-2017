#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import operator

#input function for both python2.7 and 3
def getInput(prompt=''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

print('Enter/paste content. Ctrl-D to save. ', end='')
user_input = []
while True:
    try:
        line = getInput()
    except EOFError:
        break
    user_input.append(line)

def getVariables(list):
    return_dict = {}
    for var in list:
        return_dict[var.split()[0]] = 0
    return return_dict

def testHighestNumber(number):
    global highestNumber
    if number > highestNumber:
        highestNumber = number

def handleInstructions(list):
    global variables
    for line in list:
        target, direction, diff, start, var1, check, var2 = line.split()
        var1 = 'variables[\'' + var1 + '\']'
        condition = ' '.join([var1, check, var2])
        if (eval(condition)):
            if direction == 'inc':
                variables[target] += int(diff)
                testHighestNumber(variables[target])
            elif direction == 'dec':
                variables[target] -= int(diff)
                testHighestNumber(variables[target])

def main():
    global variables
    global highestNumber
    highestNumber = 0
    variables = {}
    variables = getVariables(user_input)
    handleInstructions(user_input)
    print(max(variables.iteritems(), key=operator.itemgetter(1)))
    print('highest held number during operation:',highestNumber)

main()
