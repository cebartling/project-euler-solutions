#!/usr/bin/env python

sum = 2
first_term = 1
second_term = 2
sum_terms = first_term + second_term
while sum_terms < 4000000:
    first_term = second_term
    second_term = sum_terms
    sum_terms = first_term + second_term
    if sum_terms % 2 == 0:
        sum += sum_terms   
print 'Sum: {0}'.format(sum)

