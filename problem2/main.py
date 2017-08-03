#!/usr/local/bin/python3
max_num = 4_000_000
fibonacci_numbers = [1,1]

while True:
    fib = fibonacci_numbers[-1]+fibonacci_numbers[-2]
    if fib > max_num:
        break
    fibonacci_numbers.append(fib)

print(sum([x for x in fibonacci_numbers if x%2==0]))
