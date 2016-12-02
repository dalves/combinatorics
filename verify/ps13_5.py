#!/usr/bin/env python3
import random

def is_close(n):
    v = random.getrandbits(2*n)
    return bin(v).count('1') == n

def p_close(n, trials):
    return sum(is_close(n) for i in range(trials)) / trials

if __name__ == '__main__':

    for exp in range(20):
        n = 2**exp
        trials = min(2**24, 2**(34 - exp))
        print(exp, n, trials, p_close(n, trials), sep='\t')

