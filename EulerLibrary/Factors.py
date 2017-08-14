#!/usr/bin/env python3

import math
import itertools
import functools
from .Primes import PrimeCalculator

def get_prime_factors(num):
    '''Get prime factors for a number, in a hash listing factor, and number of times'''
    prime_factors = {}
    primes = PrimeCalculator.UnboundedIterator()
    num_divided = num
    for prime in primes:
        # This deifnition does include the number itself if the number is prime
        if prime > num_divided:
            break
        while num_divided % prime == 0:
            prime_factors[prime] = prime_factors.get(prime,0)+1
            num_divided = num_divided/prime
        # End when >sqrt, self and 1 are not prime factors
    return prime_factors
def get_number_from_prime_factors(prime_factors):
    '''Given the prime factors hash return the nunmber'''
    result = 1
    for prime in prime_factors:
        for num in range(0,prime_factors[prime]):
            result = result*prime
    return result
def get_all_factors(num):
    '''Get all factors for a number in a list. Guarantee uniqueness'''
    prime_factors = get_prime_factors(num)
    rolled_out_prime_factors = []
    for key in prime_factors.keys():
        rolled_out_prime_factors.extend([key]*prime_factors[key])
    # Initialize with 1
    all_factors  = [1]
    if num != 1:
        # Insert self, if not 1
        all_factors.append(num)
    # Insert combos of prime factors
    for length in range(1,len(rolled_out_prime_factors)):
        combinations_prime_factors = itertools.combinations(rolled_out_prime_factors,length)
        for combination in combinations_prime_factors:
            product = functools.reduce(lambda x,y: x*y, combination)
            try:
                all_factors.index(product)
            except ValueError:
                all_factors.append(product)
    return sorted(all_factors)
