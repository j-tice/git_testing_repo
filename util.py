#!/usr/bin/env python3

def nth_power(n, power=2):
    '''calculates power power for numbers up to and including n, defaulting to a power of 2
    args:
        power: power by which we raise the numbers, default of 2
        n: highest number in list of numbers, including n'''
    return [i**power for i in range(n+1)]

print(nth_power(10, 4))
print(nth_ power(10))
