#!/usr/bin/env python3
'''
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?
'''
import logging
import argparse
import os
from EulerLibrary import Utilities

def arguments(parser):
    parser.add_argument('--input','-i',type=str,default='resources/problem11-grid.txt',help='input file')
    parser.add_argument('--number','-n',type=int,default='4',help='Number to multiply')

def readGrid(file_path):
    input_file = open(file_path,'r')
    row_strings = [x.replace('\n','') for x in input_file.readlines()]
    grid = [[int(y) for y in x.split()] for x in row_strings]
    return grid

def printGrid(grid):
    for row in grid:
        for element in row:
            print('%02d'%element,end=' ')
        print('')

if __name__ == '__main__':
    PARSED_ARGS = Utilities.initialize(arguments)
    grid = readGrid(PARSED_ARGS.input)
    printGrid(grid)
