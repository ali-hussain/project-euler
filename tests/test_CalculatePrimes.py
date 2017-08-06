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
        file_path = os.path.join(os.path.dirname('__file__'),'resources','primes-to-100k.txt')
        primes_file = open(file_path,'r')
        test_primes = [int(x.replace('\n','')) for x in primes_file.readlines()]
        # Generate primes
        prime_iterator = PrimeCalculator.RangePrimesIterator(100_000)
        for index,result in enumerate(prime_iterator):
            self.assertLess(index,len(test_primes),msg='Did not stop generating primes after %d'%index)
            self.assertEqual(result,test_primes[index],
                        msg='Failure at index %d' % index)
        self.assertEqual(index,len(test_primes)-1,msg='Some primes are missing')

if __name__ == '__main__':

    unittest.main()
