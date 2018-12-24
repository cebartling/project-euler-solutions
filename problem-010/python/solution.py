#!/usr/bin/env python3

import math
import time

start = time.time()

result = 0
num = 2
limit = 2000000

print('Calculating...')
while num < limit:
    if num > 2 and num % 2 != 0: 
        max_div = math.floor(math.sqrt(num))
        for i in range(2, 1 + max_div):
            if (num % i) == 0:
                break
        else:
            result += num
    num += 1

end = time.time()

print('Summation of primes below 2,000,000: {0}'.format(result)) 
print('Elapsed time of execution: {0} seconds'.format(end - start))
