#!/usr/bin/env python3
import random

def choose(n, k, memo={(0,0): 1}):
    t = (n,k)
    if t in memo:
        return memo[t]
    if n == 0 or k > n:
        return 0
    if k == 0:
        return 1
    if k > n//2:
        return choose(n, n-k)
    val = choose(n-1, k-1) + choose(n-1, k)
    memo[t] = val
    return val



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

