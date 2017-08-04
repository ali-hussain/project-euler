#!/usr/bin/env python3

def find_multiples(factors, start, end):
    multiples = []
    for number in range(start, end+1):
        for factor in factors:
            if number % factor == 0:
                multiples.append(number)
                break
    return multiples


multiples = find_multiples([3,5], 1, 999)
print( sum(multiples))
