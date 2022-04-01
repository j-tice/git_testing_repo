#!/usr/bin/env python3

def nth_power(n, fn = lambda x: x**3):
    '''calculates power for numbers up to and including n, default power is 3'''
    return [fn(i) for i in range(n+1)]

print(nth_power(10))
    
