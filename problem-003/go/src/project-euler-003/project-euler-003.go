package main

import (
	"fmt"
)

func main() {
	n := 600851475143
	i := 2
	for i*i < n {
		for (n % i) == 0 {
			n = n / i
		}
		i++
	}
	fmt.Printf("Solution: %d\n", n)
}
