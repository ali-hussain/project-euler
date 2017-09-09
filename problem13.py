#!/usr/bin/env python3
'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''

import logging
import argparse
import os
from EulerLibrary import Utilities
from EulerLibrary.Factors import get_all_factors

def arguments(parser):
    parser.add_argument('--input','-i',type=str,default='resources/problem13.txt',help='File with input numbers')
    parser.add_argument('--digits','-d',type=int,default='10',help='Number of digits to print')

def get_numbers(filename):
    input_file = open(filename,'r')
    row_strings = [x.replace('\n','') for x in input_file.readlines()]
    input_file.close()
    values = [int(row) for row in row_strings]
    return values

if __name__ == '__main__':
    PARSED_ARGS = Utilities.initialize(arguments)
    numbers = get_numbers(PARSED_ARGS.input)
    result = sum(numbers)
    string_result = str(result)
    print(string_result[0:PARSED_ARGS.digits])
