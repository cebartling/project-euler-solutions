#!/usr/bin/env python3

def is_pythagorean_triplet(a, b, c):
    return (a ** 2) + (b ** 2) == (c ** 2) 

result = None

for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c = 1000 - a - b
        if c < b:
            break
        if is_pythagorean_triplet(a, b, c) and a + b + c == 1000:
            result = a * b * c

print('The product of Pythagorean triplet is {0}'.format(result))     
        