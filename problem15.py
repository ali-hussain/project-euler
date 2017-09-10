#!/usr/bin/env python3
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''
import logging
import argparse
import os
from EulerLibrary import Utilities
from EulerLibrary.Factors import get_all_factors

def arguments(parser):
    parser.add_argument('--rows','-r',type=int,default=20,help='Number of rows in grid')
    parser.add_argument('--columns','-c',type=int,default=20,help='Number of columns in grid')

if __name__ == '__main__':
    PARSED_ARGS = Utilities.initialize(arguments)
