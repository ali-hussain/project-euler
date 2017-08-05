#!/usr/bin/env python3
from EulerLibrary.Factors import PrimeFactors

number = 600851475143
prime_factors = PrimeFactors.get_prime_factors(number)
print(max(prime_factors.keys()))
