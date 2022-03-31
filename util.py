#!/usr/bin/env python3

def nth_power(n, power):
    '''calculates power power for numbers up to and including n'''
    return [i**power for i in range(n+1)]

print(nth_power(10, 4))
    
