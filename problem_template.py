#!/usr/bin/env python3
'''

'''

import logging
import argparse
from EulerLibrary import Utilities

def arguments(parser):
    parser.add_argument('--number','-n',type=int,default=1000,
        help='')

if __name__ == '__main__':
    PARSED_ARGS = Utilities.initialize(arguments)
