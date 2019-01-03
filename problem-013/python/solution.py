#!/usr/bin/env python3

import os
import time

start = time.time()

path = os.path.dirname(os.path.abspath(__file__))
data_filename = os.path.join(path, 'data.txt')

summation = 0

with open(data_filename, 'r') as file:
    summation = sum([int(val) for val in file])  

print('The summation of 100 50-digit numbers is {0}.'.format(summation))
first_ten_digits = str(summation)[0:10]
print('The first 10 digits of the summation is {0}.'.format(first_ten_digits))
end = time.time()

print('Elapsed time of execution: {0} seconds'.format(end - start))

