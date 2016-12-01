#!/usr/bin/env python3

import itertools

seen = set()
count = 0

def orbit(x):
    return set(x[i:] + x[:i] for i in range(len(x)))

for paint in itertools.product([1, 2, 3], repeat=8):
    if paint not in seen:
        seen.update(orbit(paint))
        count += 1

print(count)

