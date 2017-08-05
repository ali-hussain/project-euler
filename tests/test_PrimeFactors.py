#!/usr/bin/env python3
# Standard libraries to import for unit tests
import sys
import unittest
try:
    sys.path.index('..')
except ValueError:
    sys.path.append('..')

from EulerLibrary.Factors import PrimeFactors

class TestPrimeFactors(unittest.TestCase):
    preset_factors = {1: {},
                      2: {2: 1},
                      3: {3: 1},
                      4: {2: 2},
                      5: {5: 1},
                      6: {2: 1, 3: 1},
                      7: {7: 1},
                      8: {2: 3},
                      9: {3: 2},
                      10: {2: 1, 5: 1},
                      11: {11: 1},
                      12: {2: 2, 3: 1},
                      13: {13: 1},
                      14: {2: 1, 7: 1},
                      15: {3: 1, 5: 1},
                      16: {2: 4},
                      17: {17: 1},
                      18: {2: 1, 3: 2},
                      19: {19: 1},
                      20: {2: 2, 5: 1}}

    def test_known_primes(self):
        for num in range(1,21):
            result = PrimeFactors.get_prime_factors(num)
            self.assertEqual(result,TestPrimeFactors.preset_factors[num],
                            msg="%s did not match golden values of %s for number %d" %
                                (str(result),str(TestPrimeFactors.preset_factors[num]),num))

    def test_factor_recreate(self):
        for num in range(1,200):
            prime_factors = PrimeFactors.get_prime_factors(num)
            result = PrimeFactors.get_number(prime_factors)
            self.assertEqual(result,num,msg="Failed for number %d with factors %s and result %d" %
                                            (num,str(prime_factors),result))

if __name__ == '__main__':
    unittest.main()
