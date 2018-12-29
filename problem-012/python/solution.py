#!/usr/bin/env python3

import time
from math import sqrt

start = time.time()

def count_factors(triangle_number):
    """Return the number of factors of `triangle_number`"""
    count = 2 * sum(triangle_number % i == 0 for i in range(1, int(sqrt(triangle_number)) + 1))
    if int(sqrt(triangle_number))**2 == triangle_number:
        count -= 1
    return count


desired_divisors_count = 500
current_triangle_number = 0
current_natural_number = 1
done = False

while not done:
    current_triangle_number += current_natural_number
    current_natural_number += 1
    divisors_count = count_factors(current_triangle_number)
    if divisors_count >= desired_divisors_count:
        done = True

end = time.time()
print('The first triangle number with {0} divisors is {1}.'.format(desired_divisors_count, current_triangle_number))
print('Elapsed time of execution: {0} seconds'.format(end - start))

