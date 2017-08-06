#!/usr/bin/env python3

from EulerLibrary import Utilities
import logging
import argparse

if __name__ == '__main__':
    def arguments(parser):
        parser.add_argument('--input','-i',type=str,default='resources/problem8-inputstring.txt',help='input file')
        parser.add_argument('--number','-n',type=int,default='13',help='Number to multiply')

    PARSED_ARGS = Utilities.initialize(arguments)
    number = PARSED_ARGS.number
    input_string = ''
    with open(PARSED_ARGS.input,'r') as input_file:
        input_string += input_file.read().replace('\n','')
    non_zero_strings = input_string.split('0')
    # Find the max_product
    max_product = 0
    for number_string in non_zero_strings:
        for str_index in range(len(number_string)-number+1):
            product = 1
            for char_index in range(number):
                product = product * int(number_string[str_index+char_index])
            if product > max_product:
                max_product = product
    print(max_product)
