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

print('Enter/paste content: Ctrl-D to save. ', end='')
instructions = []
while True:
    try:
        line = getInput()
    except EOFError:
        break
    instructions.append(line)
instructions = list(map(int, instructions))

def makeMove(instructions, currentStep, jumps):
    try:
        jumpLen = instructions[currentStep]
        nextMove = currentStep + jumpLen
    except IndexError:
        pass
    instructions[currentStep] += 1
    jumps += 1
    return instructions, nextMove, jumps

goal = len(instructions)
currentStep = 0
jumps = 0
while currentStep < goal:
    instructions, currentStep, jumps = makeMove(instructions, currentStep, jumps)
print("jumps:", jumps)
