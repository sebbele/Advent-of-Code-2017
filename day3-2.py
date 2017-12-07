# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

#input function for both python2.7 and 3
def getInput(prompt=''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

# What is the first value written that is larger than your puzzle input?

from pprint import pprint
from itertools import cycle
target = getInput('target: ')
target = int(target)

def generateRight():
    # generate right
    global grid
    global currentNum
    end_point = len(grid[0]) + 1
    for i in range(len(grid[0])):
        grid[-1].append(0)
    for i in range(1, end_point):
        actual_y = len(grid) - 1
        currentNum = sumNeighbors([actual_y, i])
        grid[-1][i] = sumNeighbors([actual_y, i])

def generateUpLeft():
    global grid
    global currentNum
    x_length = len(grid[0])
    y_height = len(grid)
    # generate right column
    current_y = -2
    for i in range(y_height):
        if i == y_height - 1:
            grid.insert(0, [0])
            continue
        grid[current_y].append(0)
        current_y -= 1
    # generate top row
    for i in range(len(grid[1]) - 1):
        grid[0].insert(0, 0)
    #insert values into right column
    x_length = len(grid[0])
    y_height = len(grid)
    x_pos = len(grid[0]) - 1
    y_start = len(grid) - 2
    for i in range( y_start, 0, -1):
        currentNum = sumNeighbors([i, x_pos])
        grid[i][x_pos] = sumNeighbors([i, x_pos])

    # insert values into top row
    for i in range( len(grid[0]) - 1, -1, -1):
        currentNum = sumNeighbors([0, i])
        grid[0][i] = sumNeighbors([0, i])
        
def generateDown():
    global grid
    global currentNum
    x_length = len(grid[0])
    y_height = len(grid)
    # generate left column
    for i in range(y_height):
        grid[i].insert(0, 0)
    grid.append([0])
    # insert values into new column
    for i in range(y_height + 1):
        currentNum = sumNeighbors([i, 0])
        grid[i][0] = sumNeighbors([i, 0])
    

def sumNeighbors(coords):
    neighbors = []
    # left
    try:
        x_coord = coords[1] - 1
        y_coord = coords[0]
        if x_coord >= 0 and y_coord >= 0:
            neighbors.append(grid[y_coord][x_coord])
    except:
        pass
    # right
    try:
        x_coord = coords[1] + 1
        y_coord = coords[0]
        if x_coord >= 0 and y_coord >= 0:
            neighbors.append(grid[y_coord][x_coord])
    except:
        pass
    # up
    try:
        y_coord = coords[0] - 1
        x_coord = coords[1]
        if x_coord >= 0 and y_coord >= 0:
            neighbors.append(grid[y_coord][x_coord])
    except:
        pass
    # down
    try:
        y_coord = coords[0] + 1
        x_coord = coords[1]
        if x_coord >= 0 and y_coord >= 0:
            neighbors.append(grid[y_coord][x_coord])
    except:
        pass
    # right up
    try:
        x_coord = coords[1] + 1
        y_coord = coords[0] - 1
        if x_coord >= 0 and y_coord >= 0:
            neighbors.append(grid[y_coord][x_coord])
    except:
        pass
    # left up
    try:
        x_coord = coords[1] - 1
        y_coord = coords[0] - 1
        if x_coord >= 0 and y_coord >= 0:
            neighbors.append(grid[y_coord][x_coord])
    except:
        pass
    # right down
    try:
        x_coord = coords[1] + 1
        y_coord = coords[0] + 1
        if x_coord >= 0 and y_coord >= 0:
            neighbors.append(grid[y_coord][x_coord])
    except:
        pass
    # left down
    try:
        x_coord = coords[1] - 1
        y_coord = coords[0] + 1
        if x_coord >= 0 and y_coord >= 0:
            neighbors.append(grid[y_coord][x_coord])
    except:
        pass
    #print("coords: ", coords, "neighbors: ", neighbors)
    return sum(neighbors)

def findIndex(number):
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
    return [targetY, targetX]

global funcList
funcList = [ generateRight, generateUpLeft, generateDown ]
global grid
grid = [[1]]
global currentNum
currentNum = 1

def generateGrid(target):
    pool = cycle(funcList)
    for f in pool:
        print("doing", f, "target:",target,"currentNum:",currentNum)
        f()
        if currentNum > target:
            break

generateGrid(target)
print("final grid:",grid)
print("current num:", currentNum)
