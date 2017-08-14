#!/usr/bin/env python3
import math

class PrimeCalculator:
    _known_primes = [2] # Initialize with first prime, because of how calc_more_primes is written

    @classmethod
    def _divisible_by_known_prime(cls, num):
        for prime in cls._known_primes:
            if num%prime == 0:
                return False
            if math.sqrt(num) < prime:
                break
        return True

    @classmethod
    def _calc_more_primes(cls):
        num = cls._known_primes[-1] + 1
        while not cls._divisible_by_known_prime(num):
            num +=1
        cls._known_primes.append(num)

    @classmethod
    def get_prime(cls,num):
        # Precalculate all required primes
        while(len(cls._known_primes) <= num):
            cls._calc_more_primes()
        # return correct prime
        return cls._known_primes[num]

    class UnboundedIterator:
        def __init__(self):
            self._count = 0
        def __iter__(self):
            return self
        def __next__(self):
            result = PrimeCalculator.get_prime(self._count)
            self._count +=1
            return result

    class NumPrimesIterator:
        def __init__(self, first, second=None):
            if second is None:
                start = 0
                end = first
            else:
                start = first
                end = second
            if(start > end):
                raise ValueError
            self._start = start
            self._current = start
            self._end = end
        def __iter__(self):
            return self
        def __next__(self):
            if self._current == self._end:
                raise StopIteration
            result = PrimeCalculator.get_prime(self._current)
            self._current +=1
            return result

    # Iterate over primes in a range floor to ceil, ceil is not included
    class RangePrimesIterator:
        def __init__(self, first, second = None):
            if second is None:
                floor = 0
                ceil = first
            else:
                floor = first
                ceil = second
            if(floor > ceil):
                raise ValueError
            self._unbound_iter  = PrimeCalculator.UnboundedIterator()
            self._floor = floor
            self._ceil = ceil
        def __iter__(self):
            return self
        def __next__(self):
            result = self._unbound_iter.__next__()
            while result < self._floor:
                result = self._unbound_iter.__next__()
            if result >= self._ceil:
                raise StopIteration
            return result

if __name__ == "__main__":
    testbench_primes = [2,3,5,7,11,13,17,19,23,29,31]
    primes1 = PrimeCalculator()
    test_pause = 5
    print("Starting sequential test")
    for num in range (0,test_pause):
        test_prime = testbench_primes[num]
        res_prime = next(primes1)
        print("Got %d expected %d"%(res_prime,test_prime),end='')
        if res_prime == test_prime:
            print(" ... Passed")
        else:
            print(" ... Failed!")
            quit(-1)
    print("Starting direct call to get_prime test in reverse sequence")
    for num in reversed(range(0,len(testbench_primes))):
        test_prime = testbench_primes[num]
        res_prime = PrimeCalculator.get_prime(num)
        print("Got %d expected %d"%(res_prime,test_prime),end='')
        if res_prime == test_prime:
            print(" ... Passed")
        else:
            print(" ... Failed!")
            quit(-1)
    print("Starting second iterator test")
    primes2 = PrimeCalculator()
    for idx,res_prime in enumerate(primes2):
        if idx >= len(testbench_primes):
            break
        test_prime = testbench_primes[idx]
        print("Got %d expected %d"%(res_prime,test_prime),end='')
        if res_prime == test_prime:
            print(" ... Passed")
        else:
            print(" ... Failed!")
            quit(-1)
    print("Starting test to continue first iterator")
    for iteration,res_prime in enumerate(primes1):
        idx = iteration + test_pause
        if idx >= len(testbench_primes):
            break
        test_prime = testbench_primes[idx]
        print("Got %d expected %d"%(res_prime,test_prime),end='')
        if res_prime == test_prime:
            print(" ... Passed")
        else:
            print(" ... Failed!")
            quit(-1)
