#!/usr/bin/env python3

import math
from PrimeCalculator import PrimeCalculator

class PrimeFactors:
    def get_prime_factors(num):
        prime_factors = {}
        primes = PrimeCalculator()
        for prime in primes:
            if prime > num/2:
                break
            num_divided = num
            while num_divided % prime == 0:
                prime_factors[prime] = prime_factors.get(prime,0)+1
                num_divided = num_divided/prime
            # End when >sqrt, self and 1 are not prime factors
        return prime_factors

if __name__ == "__main__":
    for num in range(1,20):
        result = PrimeFactors.get_prime_factors(num)
        print("Prime factors for %d are:" % num)
        print(result)
