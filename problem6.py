#!/usr/bin/env python3

start = 1
end = 100

sum_of_series = sum(range(start,end+1))
square_of_sums = sum_of_series * sum_of_series
sum_of_squares = sum([x*x for x in range(start,end+1)])

print("square_of_sums=%d, sum_of_squares=%d, difference=%d" %
    (square_of_sums,sum_of_squares,square_of_sums-sum_of_squares))
