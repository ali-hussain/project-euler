#!/usr/bin/env python3
# Standard libraries to import for unit tests
import sys
import os
import unittest
import importlib
try:
    sys.path.index('..')
except ValueError:
    sys.path.append('..')

from EulerLibrary import Primes
from EulerLibrary.Primes import PrimeCalculator

class TestCalculatePrimes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        importlib.reload(Primes)
        from EulerLibrary.Primes import PrimeCalculator

    def test_KnownPrimes(self):
        # Test against list of known primes <100k
        # Load test_primes
        test_primes = []
        file_path = os.path.join(os.path.dirname('__file__'),'resources','primes-to-100k.txt')
        with open(file_path,'r') as primes_file:
            prime_str = primes_file.readline().replace('\n','')
            test_primes.append(int(prime_str))
        # Generate primes
        prime_iterator = PrimeCalculator.RangePrimesIterator(100_000)
        for index,result in enumerate(prime_iterator):
            self.assertEqual(result,test_primes[index],
                        msg='Failure at index %d' % index)
        selfassertEqual(index == len(test_primes),msg='Some primes are missing')
if __name__ == '__main__':
    unittest.main()
