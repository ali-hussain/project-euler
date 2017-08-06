#!/usr/bin/env python3

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
from EulerLibrary.Primes import PrimeCalculator
max_prime = 2_000_000
#max_prime = 10
primes_iterator = PrimeCalculator.RangePrimesIterator(max_prime)
result = sum(primes_iterator)
print(result)
