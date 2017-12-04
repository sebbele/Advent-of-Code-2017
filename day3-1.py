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

import pprint

def generateRight(grid, currentNum, steps):
    for i in range(steps):
        grid[-1].append(currentNum)
        currentNum += 1
    return grid, currentNum, steps

def generateUp(grid, currentNum, steps):
    currentY = -2
    for i in range(steps):
        if i == steps - 1:
            grid.insert(0, [currentNum])
            currentNum += 1
            continue
        grid[currentY].append(currentNum)
        currentY -= 1
        currentNum += 1
    steps += 1
    return grid, currentNum, steps

def generateLeft(grid, currentNum, steps):
    for i in range(steps):
        grid[0].insert(0, currentNum)
        currentNum += 1
    return grid, currentNum, steps

def generateDown(grid, currentNum, steps):
    currentY = 1
    for i in range(steps):
        if i == steps - 1:
            grid.append([currentNum])
            currentNum += 1
            continue
        grid[currentY].insert(0, currentNum)
        currentY += 1
        currentNum += 1
    steps += 1
    return grid, currentNum, steps

def findIndex(grid, number):
    currentX = 0
    done = False
    while not done:
        for y in range(len(grid)):
            try:
                targetX = grid[y].index(number)
                targetY = y
                done = True
            except ValueError:
                continue
    return [targetX, targetY]

funcList = [ generateRight, generateUp, generateLeft, generateDown ]

def generateGrid(target):
    grid = [[1]]
    steps = 1
    currentNum = 2
    while currentNum < target:
        for f in funcList:
            grid, currentNum, steps = f(grid, currentNum, steps)
    return grid

target = 289326

grid = generateGrid(target)
origin = findIndex(grid, 1)
target = findIndex(grid, target)
manhattan_distance = abs(origin[0]-target[0]) + abs(origin[1]-target[1])
print("Manhattan Distance: ", manhattan_distance)
