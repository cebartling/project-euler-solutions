#!/usr/bin/env python

smallest = 1
found = False

while (not found):
    for i in range(2, 11):
        if smallest % i != 0:
            smallest += 1 
            break
    else:
        found = True

print '{0} is the lowest number divisible by numbers 1 through 20.'.format(smallest)