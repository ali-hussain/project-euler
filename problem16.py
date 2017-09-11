#!/usr/bin/env python3
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

import logging
import argparse
from EulerLibrary import Utilities

def arguments(parser):
    parser.add_argument('--exponent','-e',type=int,default=1000,help='Power of 2 we want to calculate all digits for')

if __name__ == '__main__':
    PARSED_ARGS = Utilities.initialize(arguments)
    result = 1
    for index in range(0,PARSED_ARGS.exponent):
        result = result * 2
    string_result = str(result)
    result_digits = [int(x) for x in string_result]
    print("2^%d has digits with sum %d"%(PARSED_ARGS.exponent,sum(result_digits)))
