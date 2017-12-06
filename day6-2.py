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

import operator
import copy
from pprint import pprint

user_input = getInput('Enter/paste content: ')
user_input = user_input.split()
user_input = list(map(int, user_input))
print("working with initial state:",user_input)

def redistribute(list):
    working_copy = copy.deepcopy(list)
    mem_dict['history'].append(working_copy)
    index, value = max(enumerate(list), key=operator.itemgetter(1))
    list[index] = 0
    while value != 0:
        index = getNextIndex(list, index)
        list[index] += 1
        value -= 1
    mem_dict['current'] = list

def getNextIndex(list, index):
    if len(list) - 1 > index:
        index += 1
    else:
        index = 0
    return index

def loopFinder(dict):
    if dict['current'] in dict['history']:
        return False
    else:
        return True

def main(user_input):
    redist_count = 1
    global mem_dict
    mem_dict = { 'current' : user_input, 'history' : [] }
    redistribute(mem_dict['current'])
    while loopFinder(mem_dict):
        redistribute(mem_dict['current'])
        redist_count += 1
    print("Cycle count:", redist_count)
    looking_for = copy.deepcopy(mem_dict['current'])
    redistribute(mem_dict['current'])
    next_occurrence = 1
    while mem_dict['current'] != looking_for:
        redistribute(mem_dict['current'])
        next_occurrence += 1
    print("Next occurrence after", next_occurrence, "cycles")



main(user_input)
