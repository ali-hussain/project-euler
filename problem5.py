#!/usr/bin/env python3

from EulerLibrary.PrimeFactors import PrimeFactors

FLOOR = 1
CEIL = 20

# Get prime factors of all numbers
factors_list = []
for num in range(FLOOR,CEIL):
    factors_list.append(PrimeFactors.get_prime_factors(num))

# Get factors of the result
result_factors  = {}
for factors in factors_list:
    for prime in factors.keys():
        if result_factors.get(prime,0) < factors[prime]:
            result_factors[prime] = factors[prime]

# Get results from the factors
print( PrimeFactors.get_number(result_factors) )
