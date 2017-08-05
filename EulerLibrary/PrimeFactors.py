#!/usr/bin/env python3

import math
from .PrimeCalculator import PrimeCalculator

class PrimeFactors:
    def get_prime_factors(num):
        prime_factors = {}
        primes = PrimeCalculator()
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
    def get_number(prime_factors):
        result = 1
        for prime in prime_factors:
            for num in range(0,prime_factors[prime]):
                result = result*prime
        return result

if __name__ == "__main__":
    factors = []
    for num in range(1,20):
        result = PrimeFactors.get_prime_factors(num)
        factors.append(result)
        print("Prime factors for %d are:" % num)
        print(result)
    for num in range(1,20):
        result = PrimeFactors.get_number(factors[num-1])
        print("When recreating number expected %d got %d"%(num, result),end='')
        if num == result:
            print(" ... Passed")
        else:
            print(" ... Failed!")
            quit(-1)
