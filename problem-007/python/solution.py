#!/usr/bin/env python3

found_primes_count = 0
desired_primes_found = 10001
num = 2

while found_primes_count < desired_primes_found:
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        found_primes_count += 1
        print(num, "is a prime number")
    num += 1