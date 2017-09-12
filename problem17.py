#!/usr/bin/env python3
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
'''

import logging
import argparse
import inflect
import re
from EulerLibrary import Utilities

def arguments(parser):
    parser.add_argument('--number','-n',type=int,default=1000,
        help='Highest number we want to go to')

def strip_nonalpha(word_num):
    return strip_nonalpha.regex_pattern.sub('',word_num)
strip_nonalpha.regex_pattern = re.compile('[^a-zA-Z]')

if __name__ == '__main__':
    PARSED_ARGS = Utilities.initialize(arguments)
    p = inflect.engine()
    word_nums = []
    processed_word_nums = []
    for number in range(1,PARSED_ARGS.number+1): # Problem asks for inclusive
        word_num = p.number_to_words(number)
        word_nums.append(word_num)
        processed_word_num = strip_nonalpha(word_num)
        processed_word_nums.append(processed_word_num)
    print( sum([len(num_string) for num_string in processed_word_nums]))
