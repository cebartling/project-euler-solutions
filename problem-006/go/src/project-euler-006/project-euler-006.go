package main

import (
	"fmt"
)

func main() {
	sumOfSquares := 0
	sqaureOfSum := 0
	for i := 1; i <= 100; i++ {
		sumOfSquares += i * i
		sqaureOfSum += i
	}
	sqaureOfSum = sqaureOfSum * sqaureOfSum

	fmt.Printf("The sum of squares is %d. The sqaures of sum is %d. The difference is %d.\n",
		sumOfSquares, sqaureOfSum, sqaureOfSum-sumOfSquares)
}
