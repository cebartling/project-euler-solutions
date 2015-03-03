package main

import (
	"fmt"
)

func main() {
	sum := 2
	firstTerm := 1
	secondTerm := 2
	sumTerms := (firstTerm + secondTerm)
	for ; sumTerms < 4000000; {
	    firstTerm = secondTerm
	    secondTerm = sumTerms
	    sumTerms = firstTerm + secondTerm
	    if (sumTerms % 2) == 0 {
	    	sum += sumTerms
	    }
	}
	fmt.Printf("Sum: %d\n", sum)
}
