#!/usr/bin/env python3
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

import logging
import argparse
import os
from EulerLibrary import Utilities
from EulerLibrary.Factors import get_all_factors

def arguments(parser):
    parser.add_argument('--limit','-l',type=int,default=1_000_000,help='Largest starting number for sequence')

def generate_sequence(number):
    ''' Genereate a Collatz sequence for a number'''
    result = [number]
    while number != 1: # Assuming we won't create new math and discover cycles
        if number%2 == 0:
            # even
            number = number / 2
        else:
            # odd
            number = 3 * number + 1
        result.append(number)

if __name__ == '__main__':
    PARSED_ARGS = Utilities.initialize(arguments)
