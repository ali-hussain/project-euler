#!/usr/bin/env python3

CEIL = 999
FLOOR = 10

def palindrome(num):
    num_string = str(num)
    for index in range(0, int(len(num_string)/2)):
        if num_string[index] != num_string[-1-index]:
            return False
    return True

largest_palindrome = 0
for first in reversed(range(FLOOR, CEIL+1)):
    for second in reversed(range( first, CEIL+1)):
        product = first * second
        if palindrome(product):
            if product > largest_palindrome:
                largest_palindrome = product
            else:
                break
print(largest_palindrome, "is the largest palindrome that is a product of numbers from", FLOOR, "to", CEIL)
