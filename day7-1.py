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
user_input = []
while True:
    try:
        line = getInput()
    except EOFError:
        break
    user_input.append(line)

class Program:
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.neighbors = []
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

program_list = []

def readData(input):
    data_list = input.split()
    name = data_list[0]
    weight = data_list[1][1:-1]
    program_list.append(Program(name, weight))
    if len(data_list) > 2:
        for nei in range(3, len(data_list)):
            neighbor_name = data_list[nei].strip(',')
            program_list[-1].add_neighbor(neighbor_name)

def nameToIndex(query):
    global program_list
    for program in range(len(program_list)):
        if program_list[program].name == query:
            return program

def allNeighbors():
    global program_list
    all_neighbors = []
    for program in program_list:
        for neighbor in program.neighbors:
            all_neighbors.append(neighbor)
    return all_neighbors

def findBottom():
    global program_list
    candidates = []
    candidates_neighbors = []
    all_neighbors = allNeighbors()
    for item in program_list:
        if len(item.neighbors) > 0:
            candidates.append(item.name)
            candidates_neighbors.append(item.neighbors)
    for candidate in candidates:
        if candidate not in all_neighbors:
            bottom = candidate
    print("bottom program is",bottom)

for line in user_input:
    readData(line)

findBottom()
