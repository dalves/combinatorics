#!/usr/bin/env python3

import itertools

foods = 'turkey stuffing cornbread salad1 salad2 dessert1 dessert2 dessert3'.split()
valid = 0
for cardinality in range(len(foods) + 1):
    for meal in itertools.combinations(foods, cardinality):
        if not (any('dessert' in x for x in c) and not any('salad' in x for x in c)):
            valid+= 1

print(valid)



