package main

import "fmt"

func factorial(n uint) uint {
	// Factorial - n!
	if n <= 1 {
		return n
	}

	return n * factorial(n-1)
}

func summer(n uint) uint {
	if n <= 1 {
		return n
	} else {
		return n + summer(n-1)
	}
}

func main() {
	fmt.Println(factorial(7)) // 5040
	fmt.Println(summer(5))    // 15
}
