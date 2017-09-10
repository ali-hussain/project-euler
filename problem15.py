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

class PathFinder:
    def __init__(self,rows,columns):
        # Add 1 to increment from grid size to vertex num
        self._xx = rows+1
        self._yy = columns+1
        grid_dims = sorted([self._xx,self._yy],reverse=True)
        # Initialize memoization table with 0's
        self._memoization_table = [ [0]*(grid_dims[1]+1) for x in range(0,grid_dims[0])]
    def _find_paths(self,xx,yy):
        '''Take the dimensions of a grid and find number of paths through it. Use recursion'''
        if xx == 1 or yy == 1:
            return 1
        result = self._lookup_table(xx,yy)
        if result == 0:
            # No precalculated result, recurse
            result = self._find_paths(xx-1,yy)+self._find_paths(xx,yy-1)
            self._cache_result(xx,yy, result)
        return result
    def _lookup_table(self,xx,yy):
        grid_dims = sorted([xx,yy],reverse=True) # higher dimension first
        result = self._memoization_table[grid_dims[0]-1][grid_dims[1]-1]
        return result
    def _cache_result(self,xx,yy,res):
        grid_dims = sorted([xx,yy],reverse=True) # higher dimension first
        self._memoization_table[grid_dims[0]-1][grid_dims[1]-1] = res
    def find_num_paths(self):
        return self._find_paths(self._xx,self._yy)
if __name__ == '__main__':
    PARSED_ARGS = Utilities.initialize(arguments)
    finder = PathFinder(PARSED_ARGS.rows,PARSED_ARGS.columns)
    print(finder.find_num_paths())
