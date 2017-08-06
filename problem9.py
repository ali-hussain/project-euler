#!/usr/bin/env python3

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
def check_triplet(c,a,b):
    if c*c == a*a + b*b:
        return True
    else:
        return False

# c > a and c > b
# a + b + c < 1000
target_sum = 1000
for c_val in range(int(target_sum/3)+1,target_sum-1):
    for a_val in range(1,int(target_sum/3)+1):
        b_val = target_sum - a_val - c_val
        if check_triplet(c_val,a_val,b_val):
            print('%d,%d,%d and a Pythagorean triples with product %d' %
                   (c_val,b_val,a_val,c_val*b_val*a_val))
