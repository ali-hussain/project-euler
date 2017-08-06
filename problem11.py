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
    # To view the grid use:
    # printGrid(grid)
    # Get the result
    max_product = 0
    number = PARSED_ARGS.number
    if number <=0:
        raise ValueError
    grid_height = len(grid)
    grid_width = len(grid[0])
    # Traverse rows
    row_product_grid = [[[] for x in range(grid_width-number+1)] for y in range(grid_height) ]
    for row in range(grid_height):
        for column in range(grid_width-number+1):
            product = 1
            for offset in range(number):
                product = product * grid[row][column+offset]
            row_product_grid[row][column] = product
            if product > max_product:
                max_product = product
    # Traverse columns
    column_product_grid = [[[] for x in range(grid_width)] for y in range(grid_height-number+1) ]
    for column in range(grid_width):
        for row in range(grid_height-number+1):
            product = 1
            for offset in range(number):
                product = product * grid[row+offset][column]
            column_product_grid[row][column] = product
            if product > max_product:
                max_product = product
    # Traverse diagonals
    diagonal1_product_grid = [[[] for x in range(grid_width-number+1)] for y in range(grid_height-number+1) ]
    for row in range(grid_height-number+1):
        for column in range(grid_width-number+1):
            product = 1
            for offset in range(number):
                product = product * grid[row+offset][column+offset]
            diagonal1_product_grid[row][column] = product
            if product > max_product:
                max_product = product
    diagonal2_product_grid = [[[] for x in range(grid_width-number+1)] for y in range(grid_height-number+1) ]
    for row in range(number-1,grid_height):
        for column in range(grid_width-number+1):
            product = 1
            for offset in range(number):
                product = product * grid[row-offset][column+offset]
            diagonal2_product_grid[row-number+1][column] = product
            if product > max_product:
                max_product = product
    print(max_product)
