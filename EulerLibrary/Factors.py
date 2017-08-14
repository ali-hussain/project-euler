#!/usr/bin/env python3

import math
import itertools
from .Primes import PrimeCalculator

class Factorize:
    @staticmethod
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
    @staticmethod
    def get_number_from_prime_factors(prime_factors):
        '''Given the prime factors hash return the nunmber'''
        result = 1
        for prime in prime_factors:
            for num in range(0,prime_factors[prime]):
                result = result*prime
        return result
    @staticmethod
    def get_all_factors(num):
        '''Get all factors for a number in a list. Guarantee uniqueness'''
        prime_factors = PrimeFactors.get_prime_factors(num)
        rolled_out_prime_factors = []
        for key in prime_factors.keys():
            rolled_out_prime_factors.extend([key]*prime_factors[key])
        combination_sprime_factors = itertools.combinations(rolled_out_prime_factors)
        all_factors  = [1,num]
        for combination in permuted_prime_factors:
            product = reduce(lambda x,y: x*y, combination)
            try:
                all_factors.index(product)
            except ValueError:
                all_factors.append(product)
        return all_factors
