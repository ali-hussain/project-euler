#!/usr/bin/env python3
'''
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)

'''

import logging
import argparse
from EulerLibrary import Utilities

def arguments(parser):
    parser.add_argument('--input_file','-i',type=str,default='resources/problem18.txt',
        help='Input file with pyramid')

class PyramidMaxPathFinder:
    def __init__(self,file_name):
        self._parse_input_file(file_name)
        self._find_max_path()
    def _parse_input_file(self,file_name):
        input_file = open(file_name,'r')
        row_strings = [x.replace('\n','') for x in input_file.readlines()]
        self._pyramid = [[int(y) for y in x.split()] for x in row_strings]
        # print('Parsed pyramid:')
        # PyramidMaxPathFinder._print_pyramid(self._pyramid)
    def _find_max_path(self):
        self._max_subpath_pyramid = [[]]*len(self._pyramid)
        # Leaf node values themselves are the max path
        self._max_subpath_pyramid[-1]=self._pyramid[-1]
        # For all other rows the max path self + greater of the two reachable values
        for row in reversed(range(0,len(self._pyramid)-1)):
            max_row = []
            for column in range(0,len(self._pyramid[row])):
                max_subpath = self._pyramid[row][column]+max(
                                    self._max_subpath_pyramid[row+1][column],
                                    self._max_subpath_pyramid[row+1][column+1])
                max_row.append(max_subpath)
            self._max_subpath_pyramid[row]=max_row
        # print('Max subpaths calculated:')
        # PyramidMaxPathFinder._print_pyramid(self._max_subpath_pyramid)
    @staticmethod
    def _print_pyramid(pyramid):
        top_string = str(pyramid[0][0])
        for row in pyramid:
            for value in row:
                print('{0:{1}}'.format(value,len(top_string)),end=' ')
            print('')
    def get_max_path(self):
        return self._max_subpath_pyramid[0][0]

if __name__ == '__main__':
    PARSED_ARGS = Utilities.initialize(arguments)
    finder = PyramidMaxPathFinder(PARSED_ARGS.input_file)
    print('Calculated max path {}'.format(finder.get_max_path()))
