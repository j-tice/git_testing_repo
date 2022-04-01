#!/usr/bin/env python3

import numpy as np

def nth_power(n, fn = lambda x: x**3):
    '''calculates power for numbers up to and including n, default power is 3'''
    return [fn(i) for i in range(n+1)]

def sigmoid(x, scale=1):
    return 1/(1 + np.exp(-scale * x))

print(nth_power(10))
print(sigmoid(0.0))
