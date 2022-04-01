#!/usr/bin/env python3

def nth_power(n, fn = lambda x: x**2):
    '''calculates power power for numbers up to and including n'''
    return [fn(i) for i in range(n+1)]

print(nth_power(10))
    
