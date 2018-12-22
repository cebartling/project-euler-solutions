package main

import (
	"fmt"
)

func main() {
	foundPrimesCount := 0
	desiredPrimesFound := 10001
	num := 2

	for foundPrimesCount < desiredPrimesFound {
		isPrime := true
		for i := 2; i < num; i++ {
			if (num % i) == 0 {
				isPrime = false
				break
			}
		}
		if isPrime == true {
			foundPrimesCount++
			fmt.Printf("%d is a prime number\n", num)
		}
		num++
	}
}
