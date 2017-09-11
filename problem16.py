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
