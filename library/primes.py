#!/usr/local/bin/python3
import math

class PrimeCalculator:
    known_primes = [2] # Initialize with first prime, because of how calc_more_primes is written

    def __init__(self):
        self.count = 0

    def is_prime(num):
        for prime in PrimeCalculator.known_primes:
            if num%prime == 0:
                return False
            if math.sqrt(num) < prime:
                break
        return True

    def calc_more_primes():
        num = PrimeCalculator.known_primes[-1] + 1
        while not PrimeCalculator.is_prime(num):
            num +=1
        PrimeCalculator.known_primes.append(num)

    def get_prime(num):
        # Precalculate all required primes
        while(len(PrimeCalculator.known_primes) <= num):
            PrimeCalculator.calc_more_primes()
        # return correct prime
        return PrimeCalculator.known_primes[num]

    def __iter__(self):
        return self

    def __next__(self):
        result = PrimeCalculator.get_prime(self.count)
        self.count +=1
        return result


if __name__ == "__main__":
    testbench_primes = [2,3,5,7,11,13,17,19,23,29,31]
    primes1 = PrimeCalculator()
    print("Starting sequential test")
    for num in range (0,5):
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
