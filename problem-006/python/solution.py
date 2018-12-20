#!/usr/bin/env python3

sum_of_squares = 0
sqaure_of_sum = 0
start = 1
end = 100

for i in range(start, end + 1):
    sum_of_squares += i * i
    sqaure_of_sum += i

sqaure_of_sum = sqaure_of_sum * sqaure_of_sum

print('The sum of squares is {0}. The sqaures of sum is {1}. The difference is {2}'.format(
    sum_of_squares, sqaure_of_sum, sqaure_of_sum - sum_of_squares))
