#!/usr/bin/env python

largest_palindrome = 0
first_factor = 0
second_factor = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        current = i * j
        if (str(current) == str(current)[::-1]) and (current > largest_palindrome):
            first_factor = i
            second_factor = j
            largest_palindrome = current

print '{0} created by multiplying {1} and {2}.'.format(largest_palindrome, first_factor, second_factor)